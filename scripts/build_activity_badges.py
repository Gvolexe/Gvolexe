"""Build the selected achievement badges from the same Metrics data as the profile."""

import argparse
from pathlib import Path
import xml.etree.ElementTree as ET


ICONS = {
    "Worker": "org", "Polyglot": "lang", "Forker": "fork", "Contributor": "pr",
    "Member": "member", "Developer": "repo", "Stargazer": "star", "Follower": "follow",
}


def classes(element):
    return element.get("class", "").split()


def find_class(element, name):
    return next((node for node in element.iter() if name in classes(node)), None)


def text(element):
    return " ".join("".join(element.itertext()).split()) if element is not None else ""


def parse_achievements(source):
    root = ET.fromstring(source)
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError("Metrics source is not an SVG")
    results = []
    for achievement in root.iter():
        if "achievement" not in classes(achievement):
            continue
        title = find_class(achievement, "title")
        if title is None:
            raise ValueError("Achievement title missing")
        name = " ".join([title.text or "", *(child.tail or "" for child in title)]).strip().capitalize()
        rank = text(find_class(title, "prefix"))
        count = text(find_class(title, "value"))
        description = text(find_class(achievement, "text"))
        tier = next((tier for tier in ["s", "a", "b", "c"] if tier in classes(achievement)), None)
        if not name or not count or not description or tier is None:
            raise ValueError("Incomplete achievement data")
        results.append({"name": name, "rank": rank, "count": count, "text": description,
                        "tier": tier, "icon": ICONS.get(name, "star")})
    if not results or len({item["name"] for item in results}) != len(results):
        raise ValueError("Missing or duplicate achievements")
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("assets"))
    args = parser.parse_args()
    from pixel_badges import render_badges

    achievements = parse_achievements(args.source.read_bytes())
    renders = {"activity-badges.svg": render_badges(achievements, "wide"),
               "activity-badges-mobile.svg": render_badges(achievements, "narrow")}
    for name, svg in renders.items():
        if ET.fromstring(svg).tag != "{http://www.w3.org/2000/svg}svg":
            raise ValueError(f"Invalid output: {name}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, svg in renders.items():
        target = args.output_dir / name
        temporary = target.with_suffix(".svg.tmp")
        temporary.write_text(svg, encoding="utf-8")
        temporary.replace(target)
    print(f"Rendered {len(achievements)} achievements from Metrics in desktop and mobile layouts.")


if __name__ == "__main__":
    main()

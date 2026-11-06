"""Refresh the profile card while retaining the last valid SVG on outages."""

import re
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


URL = (
    "https://github-contribution-stats.vercel.app/api?username=Gvolexe"
    "&limit=5&theme=dark&combine_all_yearly_contributions=true"
)
TARGET = Path(__file__).resolve().parents[1] / "assets/contribution-stats.svg"


def refresh():
    for attempt in range(3):
        try:
            request = urllib.request.Request(URL, headers={"User-Agent": "Gvolexe-profile-card-refresh"})
            with urllib.request.urlopen(request, timeout=30) as response:
                content = response.read(1_000_001)
            if not 1000 <= len(content) <= 1_000_000:
                raise ValueError("Unexpected card size")
            root = ET.fromstring(content)
            text = " ".join(root.itertext())
            if root.tag != "{http://www.w3.org/2000/svg}svg":
                raise ValueError("Response is not an SVG")
            if "Contribution Stats" not in text or re.search(
                r"Something went wrong|Could not fetch|rate limit|Application error",
                text,
                re.IGNORECASE,
            ):
                raise ValueError("Source returned an error card")
            if any(element.tag.rsplit("}", 1)[-1] == "script" for element in root.iter()):
                raise ValueError("Unexpected script in SVG")
            TARGET.parent.mkdir(parents=True, exist_ok=True)
            pending = TARGET.with_suffix(".svg.tmp")
            pending.write_bytes(content)
            pending.replace(TARGET)
            print("Contribution card refreshed successfully.")
            return
        except (OSError, ValueError, ET.ParseError) as error:
            print(f"Attempt {attempt + 1} failed: {error}")
            if attempt < 2:
                time.sleep(3)
    if TARGET.exists():
        print("::warning::Source unavailable; retaining the last working contribution card.")
    else:
        raise SystemExit("No valid contribution card available.")


if __name__ == "__main__":
    refresh()

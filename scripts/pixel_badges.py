"""Render the Pixel arcade achievement badges as a self-contained SVG.

    from pixel_badges import render_badges
    svg = render_badges(items, mode="wide")   # or mode="narrow"

Each item is a dict with string fields:
    tier   's' | 'a' | 'b' | 'c'   (source tier, sets the colour)
    rank   source rank prefix, e.g. 'Master'; may be empty
    name   achievement name, e.g. 'Worker'
    count  value exactly as Metrics shows it, e.g. '442'
    text   description exactly as Metrics shows it
    icon   'org' | 'lang' | 'fork' | 'pr' | 'member' | 'repo' | 'star' | 'follow'

Values are drawn as given: nothing is computed, rounded or added. Labels use a
custom 5x7 bitmap font drawn as rectangles; a label with a character the font
lacks is set in a monospace font instead, so no character is dropped. Icons
are pixelarticons (MIT) from assets/icons/pixelarticons, read on first use.
Standard library only; importing the module reads no files.
"""

import html
import math
import re
from pathlib import Path
import xml.etree.ElementTree as ET

__all__ = ["render_badges"]

ICON_DIR = Path(__file__).resolve().parent.parent / "assets" / "icons" / "pixelarticons"
ICON_FILES = {
    "org": "building", "lang": "code", "fork": "git-branch", "pr": "git-pull-request",
    "member": "calendar", "repo": "book-open", "star": "star", "follow": "user-plus",
}
FALLBACK_ICON = "star"

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

TIER_COLOURS = {"s": "#ff5d7e", "a": "#ffc93c", "b": "#b28dff", "c": "#4fc3ff"}
BACKGROUND, PANEL, NAME_COLOUR, TEXT_COLOUR = "#0e1020", "#15172c", "#f2f3ff", "#a7abc9"

LAYOUTS = {"wide": (4, 720), "narrow": (2, 360)}
PAD, GAP, ROW_GAP = 12, 10, 10
TEXT_TOP, LINE_HEIGHT, TEXT_SIZE = 152, 12, 9.5
MONO_ADVANCE = 0.6  # monospace glyph advance in em

# 5x7 bitmap font: seven rows of five bits per glyph. Lowercase is drawn as uppercase.
FONT = {
    "A": "01110 10001 10001 11111 10001 10001 10001", "B": "11110 10001 10001 11110 10001 10001 11110",
    "C": "01110 10001 10000 10000 10000 10001 01110", "D": "11110 10001 10001 10001 10001 10001 11110",
    "E": "11111 10000 10000 11110 10000 10000 11111", "F": "11111 10000 10000 11110 10000 10000 10000",
    "G": "01110 10001 10000 10111 10001 10001 01111", "H": "10001 10001 10001 11111 10001 10001 10001",
    "I": "01110 00100 00100 00100 00100 00100 01110", "J": "00111 00010 00010 00010 00010 10010 01100",
    "K": "10001 10010 10100 11000 10100 10010 10001", "L": "10000 10000 10000 10000 10000 10000 11111",
    "M": "10001 11011 10101 10101 10001 10001 10001", "N": "10001 10001 11001 10101 10011 10001 10001",
    "O": "01110 10001 10001 10001 10001 10001 01110", "P": "11110 10001 10001 11110 10000 10000 10000",
    "Q": "01110 10001 10001 10001 10101 10010 01101", "R": "11110 10001 10001 11110 10100 10010 10001",
    "S": "01111 10000 10000 01110 00001 00001 11110", "T": "11111 00100 00100 00100 00100 00100 00100",
    "U": "10001 10001 10001 10001 10001 10001 01110", "V": "10001 10001 10001 10001 10001 01010 00100",
    "W": "10001 10001 10001 10101 10101 10101 01010", "X": "10001 10001 01010 00100 01010 10001 10001",
    "Y": "10001 10001 01010 00100 00100 00100 00100", "Z": "11111 00001 00010 00100 01000 10000 11111",
    "0": "01110 10001 10011 10101 11001 10001 01110", "1": "00100 01100 00100 00100 00100 00100 01110",
    "2": "01110 10001 00001 00010 00100 01000 11111", "3": "11111 00010 00100 00010 00001 10001 01110",
    "4": "00010 00110 01010 10010 11111 00010 00010", "5": "11111 10000 11110 00001 00001 10001 01110",
    "6": "00110 01000 10000 11110 10001 10001 01110", "7": "11111 00001 00010 00100 01000 01000 01000",
    "8": "01110 10001 10001 01110 10001 10001 01110", "9": "01110 10001 10001 01111 00001 00010 01100",
    " ": "00000 00000 00000 00000 00000 00000 00000",
    ".": "00000 00000 00000 00000 00000 01100 01100", ",": "00000 00000 00000 00000 01100 00100 01000",
    "-": "00000 00000 00000 11111 00000 00000 00000", "+": "00000 00100 00100 11111 00100 00100 00000",
    "/": "00001 00001 00010 00100 01000 10000 10000", ":": "00000 01100 01100 00000 01100 01100 00000",
    "'": "00100 00100 01000 00000 00000 00000 00000", "!": "00100 00100 00100 00100 00100 00000 00100",
    "?": "01110 10001 00001 00010 00100 00000 00100", "#": "01010 01010 11111 01010 11111 01010 01010",
    "%": "11000 11001 00010 00100 01000 10011 00011", "&": "01100 10010 10100 01000 10101 10010 01101",
    "(": "00010 00100 01000 01000 01000 00100 00010", ")": "01000 00100 00010 00010 00010 00100 01000",
    "_": "00000 00000 00000 00000 00000 00000 11111",
}

_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f\ud800-\udfff￾￿]")
_icon_cache = {}


def _num(value):
    text = f"{value:.2f}".rstrip("0").rstrip(".")
    return "0" if text == "-0" else text


def _esc(value):
    return html.escape(value, quote=True)


def _clean(value, field):
    """Normalise whitespace; replace characters XML cannot carry with U+FFFD."""
    if value is None:
        value = ""
    if not isinstance(value, str):
        raise TypeError(f"Achievement field '{field}' must be a string")
    return " ".join(_CONTROL.sub("�", value).split())


def _icon(key, x, y, size, colour):
    name = ICON_FILES.get(key, ICON_FILES[FALLBACK_ICON])
    if name not in _icon_cache:
        root = ET.parse(ICON_DIR / f"{name}.svg").getroot()
        paths = []
        for node in root.iter("{http://www.w3.org/2000/svg}path"):
            rule = node.get("fill-rule")
            paths.append(f'<path d="{_esc(node.get("d", ""))}"'
                         + (f' fill-rule="{_esc(rule)}"' if rule else "") + "/>")
        if not paths:
            raise ValueError(f"Icon has no paths: {name}.svg")
        _icon_cache[name] = (root.get("viewBox", "0 0 24 24"), "".join(paths))
    view_box, inner = _icon_cache[name]
    return (f'<svg x="{_num(x)}" y="{_num(y)}" width="{size}" height="{size}" '
            f'viewBox="{_esc(view_box)}" fill="{colour}" aria-hidden="true">{inner}</svg>')


def _pixel_width(text, scale):
    return len(text) * 6 * scale - scale


def _pixel_path(text, x0, y0, scale, colour):
    d = []
    for index, char in enumerate(text):
        gx = x0 + index * 6 * scale
        for row_index, row in enumerate(FONT[char].split()):
            col = 0
            while col < 5:
                if row[col] != "1":
                    col += 1
                    continue
                start = col
                while col < 5 and row[col] == "1":
                    col += 1
                run = (col - start) * scale
                d.append(f"M{_num(gx + start * scale)} {_num(y0 + row_index * scale)}"
                         f"h{_num(run)}v{_num(scale)}h-{_num(run)}z")
    return f'<path d="{"".join(d)}" fill="{colour}"/>' if d else ""


def _label(text, cx, top, scales, max_width, colour):
    """Centre a label in the bitmap font, shrinking to fit; fall back to monospace text."""
    upper = text.upper()
    if all(char in FONT for char in upper):
        for scale in scales:
            width = _pixel_width(upper, scale)
            if width <= max_width:
                x0 = cx - width // 2 if float(scale).is_integer() else round(cx - width / 2, 2)
                return _pixel_path(upper, x0, top, scale, colour)
    # Characters the bitmap font lacks, or too long even at the smallest scale.
    scale = scales[0]
    size = 10 * scale  # monospace caps are about 0.7em tall: matches the 7-row glyph height
    fit = ""
    if len(upper) * size * MONO_ADVANCE > max_width:
        fit = f' textLength="{_num(max_width)}" lengthAdjust="spacingAndGlyphs"'
    return (f'<text x="{_num(cx)}" y="{_num(top + 7 * scale)}" font-family="{MONO}" '
            f'font-size="{_num(size)}" font-weight="700" fill="{colour}" text-anchor="middle"'
            f'{fit}>{_esc(upper)}</text>')


def _wrap(text, max_width):
    limit = max(1, int(max_width / (TEXT_SIZE * MONO_ADVANCE)))
    lines, current = [], ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if len(candidate) <= limit or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def _text_line(line, cx, y, max_width):
    fit = ""
    if len(line) * TEXT_SIZE * MONO_ADVANCE > max_width:
        fit = f' textLength="{_num(max_width)}" lengthAdjust="spacingAndGlyphs"'
    return (f'<text x="{_num(cx)}" y="{_num(y)}" font-family="{MONO}" font-size="{TEXT_SIZE}" '
            f'fill="{TEXT_COLOUR}" text-anchor="middle"{fit}>{_esc(line)}</text>')


def _normalise(items):
    if isinstance(items, (str, bytes)) or not items:
        raise ValueError("render_badges needs a non-empty list of achievements")
    result = []
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            raise TypeError(f"Achievement {index} must be a dict")
        clean = {field: _clean(item.get(field), field)
                 for field in ("tier", "rank", "name", "count", "text", "icon")}
        if clean["tier"] not in TIER_COLOURS:
            raise ValueError(f"Achievement {index} has unknown tier {clean['tier']!r}")
        for field in ("name", "count", "text"):
            if not clean[field]:
                raise ValueError(f"Achievement {index} is missing '{field}'")
        result.append(clean)
    return result


def _summary(items):
    parts = [f"{(a['rank'] + ' ' + a['name']).strip()}, {a['count']}: {a['text']}" for a in items]
    return "Achievements. " + "; ".join(parts) + "."


def render_badges(items, mode="wide"):
    """Return the Pixel arcade badge sheet for ``items`` as a complete SVG string."""
    if mode not in LAYOUTS:
        raise ValueError("mode must be 'wide' or 'narrow'")
    items = _normalise(items)
    cols, width = LAYOUTS[mode]
    pid = f"pixel-badges-{mode}"
    cell = int((width - 2 * PAD - (cols - 1) * GAP) / cols)
    inner_width = cell - 16
    wrapped = [_wrap(a["text"], inner_width) for a in items]
    cell_height = TEXT_TOP + 2 + LINE_HEIGHT * max(2, *(len(lines) for lines in wrapped))
    rows = math.ceil(len(items) / cols)
    height = 2 * PAD + rows * cell_height + (rows - 1) * ROW_GAP

    out = [f'<rect width="{width}" height="{height}" fill="{BACKGROUND}"/>',
           f'<rect width="{width}" height="{height}" fill="url(#{pid}-scan)"/>',
           '<g shape-rendering="crispEdges">']
    hidden = []
    for index, (a, lines) in enumerate(zip(items, wrapped)):
        row, col = divmod(index, cols)
        in_row = min(cols, len(items) - row * cols)  # centre a partly filled last row
        offset = (width - (in_row * cell + (in_row - 1) * GAP)) // 2
        x = offset + col * (cell + GAP)
        y = PAD + row * (cell_height + ROW_GAP)
        colour = TIER_COLOURS[a["tier"]]
        cx = x + cell // 2  # whole pixels keep the bitmap labels crisp
        h = cell_height
        out.append(
            f'<rect x="{x + 4}" y="{y}" width="{cell - 8}" height="{h}" fill="{colour}"/>'
            f'<rect x="{x}" y="{y + 4}" width="{cell}" height="{h - 8}" fill="{colour}"/>'
            f'<rect x="{x + 6}" y="{y + 2}" width="{cell - 12}" height="{h - 4}" fill="{PANEL}"/>'
            f'<rect x="{x + 2}" y="{y + 6}" width="{cell - 4}" height="{h - 12}" fill="{PANEL}"/>'
            f'<rect x="{x + 6}" y="{y + 6}" width="{cell - 12}" height="62" fill="{colour}" fill-opacity=".1"/>')
        out.append(_icon(a["icon"], cx - 24, y + 13, 48, colour))
        if a["rank"]:
            out.append(_label(a["rank"], cx, y + 76, (2, 1.5), inner_width, colour))
        out.append(_label(a["name"], cx, y + 94, (2, 1.5), inner_width, NAME_COLOUR))
        out.append(_label(a["count"], cx, y + 114, (3, 2.5, 2), inner_width, colour))
        for line_index, line in enumerate(lines):
            out.append(_text_line(line, cx, y + TEXT_TOP + line_index * LINE_HEIGHT, inner_width))
        # Transparent copy of the bitmap labels so they can be selected and searched.
        hidden.append(f'<text x="{_num(cx)}" y="{y + 92}" font-family="{MONO}" font-size="12" '
                      f'fill="#000" fill-opacity="0" text-anchor="middle">'
                      f'{_esc((a["rank"] + " " + a["name"]).strip() + " " + a["count"])}</text>')
    out.append("</g>")
    out += hidden

    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" role="img" aria-labelledby="{pid}-title" '
            f'font-family="{SANS}"><title id="{pid}-title">{_esc(_summary(items))}</title>'
            f'<defs><pattern id="{pid}-scan" width="4" height="3" patternUnits="userSpaceOnUse">'
            f'<rect width="4" height="1" fill="#fff" fill-opacity=".035"/></pattern></defs>'
            f'{"".join(out)}</svg>\n')

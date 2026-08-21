"""Render the corrected Carl Webb research note as a reader-formatted PDF.

Requires ReportLab and the DejaVu font family at the standard Linux font path.
The Markdown source remains authoritative.
"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/reports/carl-webb-inscription-critical-assessment-2026-08-21.md"
OUTPUT = ROOT / "output/pdf/carl-webb-inscription-critical-assessment-2026-08-21.pdf"

INK = colors.HexColor("#202A3A")
MUTED = colors.HexColor("#647184")
BLUE = colors.HexColor("#2374A6")
LIGHT_BLUE = colors.HexColor("#EAF4FA")
PALE_BLUE = colors.HexColor("#F4F8FB")
RULE = colors.HexColor("#C8D7E2")
WARM = colors.HexColor("#FBFAF7")
WHITE = colors.white

pdfmetrics.registerFont(TTFont("DejaVuSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSerif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSerif-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSansMono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSansMono-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"))


def inline_markup(text: str) -> str:
    pattern = re.compile(r"(\*\*.+?\*\*|`.+?`|\*.+?\*|https?://\S+)")
    out: list[str] = []
    for part in pattern.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            out.append(f"<b>{escape(part[2:-2])}</b>")
        elif part.startswith("`") and part.endswith("`"):
            out.append(f"<font name='DejaVuSansMono'>{escape(part[1:-1])}</font>")
        elif part.startswith("*") and part.endswith("*"):
            out.append(escape(part[1:-1]))
        elif part.startswith("http://") or part.startswith("https://"):
            url = escape(part)
            label = escape(urlsplit(part).netloc.removeprefix("www."))
            out.append(f"<link href='{url}' color='#2374A6'>[{label}]</link>")
        else:
            out.append(escape(part))
    return "".join(out)


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="ReportLabel",
        fontName="DejaVuSans-Bold",
        fontSize=7.5,
        leading=9,
        textColor=BLUE,
        spaceAfter=4,
        tracking=1.4,
    )
)
styles.add(
    ParagraphStyle(
        name="ReportTitle",
        fontName="DejaVuSerif-Bold",
        fontSize=25,
        leading=27,
        textColor=INK,
        spaceAfter=7,
    )
)
styles.add(
    ParagraphStyle(
        name="ReportSubtitle",
        fontName="DejaVuSans",
        fontSize=11.5,
        leading=15,
        textColor=MUTED,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="H1Report",
        fontName="DejaVuSans-Bold",
        fontSize=14,
        leading=17,
        textColor=INK,
        spaceBefore=13,
        spaceAfter=7,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="H2Report",
        fontName="DejaVuSans-Bold",
        fontSize=10.7,
        leading=13,
        textColor=BLUE,
        spaceBefore=9,
        spaceAfter=4,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyReport",
        fontName="DejaVuSerif",
        fontSize=9.1,
        leading=12.6,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=6,
        splitLongWords=True,
    )
)
styles.add(
    ParagraphStyle(
        name="BodySmall",
        parent=styles["BodyReport"],
        fontSize=8.15,
        leading=10.8,
    )
)
styles.add(
    ParagraphStyle(
        name="BulletReport",
        parent=styles["BodyReport"],
        leftIndent=0,
        firstLineIndent=0,
        spaceAfter=2.5,
    )
)
styles.add(
    ParagraphStyle(
        name="TableHead",
        fontName="DejaVuSans-Bold",
        fontSize=7.8,
        leading=9.5,
        textColor=WHITE,
    )
)
styles.add(
    ParagraphStyle(
        name="TableBody",
        fontName="DejaVuSerif",
        fontSize=7.7,
        leading=10,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="Callout",
        fontName="DejaVuSerif-Bold",
        fontSize=10,
        leading=14,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="CodeReport",
        fontName="DejaVuSansMono-Bold",
        fontSize=8.8,
        leading=13,
        textColor=WHITE,
        leftIndent=0,
    )
)
styles.add(
    ParagraphStyle(
        name="SourceReport",
        fontName="DejaVuSerif",
        fontSize=7.8,
        leading=10.5,
        textColor=INK,
        splitLongWords=True,
    )
)


def draw_page(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(WARM)
    canvas.rect(0, 0, width, height, stroke=0, fill=1)
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.55)
    canvas.line(18 * mm, height - 13.5 * mm, width - 18 * mm, height - 13.5 * mm)
    canvas.setFont("DejaVuSans-Bold", 6.8)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, height - 10.7 * mm, "SOMERTON MAN RESEARCH NOTE")
    canvas.setFont("DejaVuSans", 6.8)
    canvas.drawRightString(width - 18 * mm, height - 10.7 * mm, "CORRECTED VERSION 2.0 | 21 AUGUST 2026")
    canvas.line(18 * mm, 13.5 * mm, width - 18 * mm, 13.5 * mm)
    canvas.setFont("DejaVuSans", 6.8)
    canvas.drawString(18 * mm, 9.8 * mm, "Critical assessment of the technical-lettering hypothesis")
    canvas.drawRightString(width - 18 * mm, 9.8 * mm, f"Page {doc.page}")
    canvas.restoreState()


def paragraph(text: str, style_name: str = "BodyReport") -> Paragraph:
    return Paragraph(inline_markup(text), styles[style_name])


def make_table(lines: list[str], usable_width: float) -> Table:
    rows: list[list[str]] = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    cols = len(rows[0])
    if cols == 2:
        widths = [34 * mm, usable_width - 34 * mm]
    else:
        widths = [usable_width / cols] * cols
    rendered = []
    for ridx, row in enumerate(rows):
        style = "TableHead" if ridx == 0 else "TableBody"
        rendered.append([paragraph(cell, style) for cell in row])
    table = Table(rendered, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), INK),
                ("BACKGROUND", (0, 1), (-1, -1), WHITE),
                ("GRID", (0, 0), (-1, -1), 0.45, RULE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PALE_BLUE]),
            ]
        )
    )
    return table


def render_markdown() -> list:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    story: list = []
    title = lines[0][2:]
    subtitle = lines[2][3:]
    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph("CORRECTED RESEARCH NOTE", styles["ReportLabel"]))
    story.append(Paragraph(escape(title), styles["ReportTitle"]))
    story.append(Paragraph(escape(subtitle), styles["ReportSubtitle"]))
    story.append(Table([[""]], colWidths=[174 * mm], rowHeights=[1.2 * mm], style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), BLUE)])))
    story.append(Spacer(1, 5 * mm))

    idx = 4
    metadata: list[list[Paragraph]] = []
    while idx < len(lines) and lines[idx].startswith("**"):
        raw = lines[idx]
        key, value = raw.split(":**", 1)
        key = key.replace("**", "").strip()
        metadata.append([paragraph(key, "TableHead"), paragraph(value.strip(), "TableBody")])
        idx += 1
    if metadata:
        meta = Table(metadata, colWidths=[35 * mm, 139 * mm], hAlign="LEFT")
        meta.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), INK),
            ("BACKGROUND", (1, 0), (1, -1), LIGHT_BLUE),
            ("GRID", (0, 0), (-1, -1), 0.4, RULE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        story.append(meta)
        story.append(Spacer(1, 4 * mm))

    current_section = ""
    first_exec_paragraph = False
    while idx < len(lines):
        line = lines[idx]
        if not line.strip():
            idx += 1
            continue
        if line.startswith("```"):
            idx += 1
            code: list[str] = []
            while idx < len(lines) and not lines[idx].startswith("```"):
                code.append(lines[idx])
                idx += 1
            idx += 1
            block = Preformatted("\n".join(code), styles["CodeReport"])
            panel = Table([[block]], colWidths=[174 * mm], style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), INK),
                ("BOX", (0, 0), (-1, -1), 0.6, INK),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]))
            story.extend([panel, Spacer(1, 6)])
            continue
        # The editable master retains a revision note, but it is repository
        # housekeeping rather than part of the reader-facing assessment.
        if line == "## Revision note":
            break

        if line.startswith("## "):
            current_section = line[3:].strip()
            story.append(Paragraph(escape(current_section), styles["H1Report"]))
            first_exec_paragraph = current_section == "Executive assessment"
            idx += 1
            continue
        if line.startswith("### "):
            story.append(Paragraph(inline_markup(line[4:].strip()), styles["H2Report"]))
            idx += 1
            continue
        if line.startswith("|"):
            table_lines: list[str] = []
            while idx < len(lines) and lines[idx].startswith("|"):
                table_lines.append(lines[idx])
                idx += 1
            story.extend([make_table(table_lines, 174 * mm), Spacer(1, 6)])
            continue
        if re.match(r"^- ", line):
            items: list[ListItem] = []
            while idx < len(lines) and re.match(r"^- ", lines[idx]):
                text = lines[idx][2:].strip()
                idx += 1
                while idx < len(lines) and lines[idx].startswith("  ") and lines[idx].strip():
                    text += " " + lines[idx].strip()
                    idx += 1
                items.append(ListItem(paragraph(text, "BulletReport"), leftIndent=10))
                while idx < len(lines) and not lines[idx].strip():
                    idx += 1
            story.append(ListFlowable(items, bulletType="bullet", start="circle", leftIndent=15, bulletFontName="DejaVuSans", bulletFontSize=6, spaceAfter=5))
            continue
        if re.match(r"^\d+\. ", line):
            items = []
            start_num = int(line.split(".", 1)[0])
            while idx < len(lines) and re.match(r"^\d+\. ", lines[idx]):
                text = re.sub(r"^\d+\.\s+", "", lines[idx]).strip()
                idx += 1
                while idx < len(lines) and lines[idx].startswith("   ") and lines[idx].strip():
                    text += " " + lines[idx].strip()
                    idx += 1
                style = "SourceReport" if current_section == "Sources" else "BulletReport"
                items.append(ListItem(paragraph(text, style), leftIndent=14))
                while idx < len(lines) and not lines[idx].strip():
                    idx += 1
            story.append(ListFlowable(items, bulletType="1", start=start_num, leftIndent=18, bulletFontName="DejaVuSans", bulletFontSize=7.5, spaceAfter=5))
            continue

        para_lines = [line.strip()]
        idx += 1
        while idx < len(lines):
            nxt = lines[idx]
            if not nxt.strip() or nxt.startswith(("## ", "### ", "|", "```")) or re.match(r"^(?:- |\d+\. )", nxt):
                break
            para_lines.append(nxt.strip())
            idx += 1
        text = " ".join(para_lines)
        style = "SourceReport" if current_section == "Sources" else "BodyReport"
        flow = paragraph(text, style)
        if first_exec_paragraph:
            callout = Table([[flow]], colWidths=[174 * mm], style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BLUE),
                ("LINEBEFORE", (0, 0), (0, 0), 3, BLUE),
                ("LEFTPADDING", (0, 0), (-1, -1), 11),
                ("RIGHTPADDING", (0, 0), (-1, -1), 11),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]))
            story.append(KeepTogether([callout, Spacer(1, 6)]))
            first_exec_paragraph = False
        else:
            story.append(flow)
    return story


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="Carl Webb and the Somerton Man inscription: a critical assessment",
        author="Somerton Man research repository",
        subject="Corrected research note on the technical-lettering hypothesis",
        creator="ReportLab",
        pageCompression=1,
        invariant=1,
    )
    doc.build(render_markdown(), onFirstPage=draw_page, onLaterPages=draw_page)
    print(OUTPUT)


if __name__ == "__main__":
    main()

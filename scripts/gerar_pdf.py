"""Gera o relatório de doc/pdf.md e suas figuras; dependências só de documentação."""
import html
import re
from pathlib import Path

import pymupdf
from reportlab.graphics import renderPDF, renderSVG
from reportlab.graphics.shapes import Drawing, Group, Line, Path as ShapePath, Circle, String, Rect
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "doc"
INK = colors.HexColor("#202020")
TEAL = colors.HexColor("#404040")
GRAY = colors.HexColor("#eeeeee")


def fontes():
    pdfmetrics.registerFontFamily("Times-Roman", normal="Times-Roman", bold="Times-Bold",
                                  italic="Times-Italic", boldItalic="Times-BoldItalic")


def texto(d, x, y, valor, tamanho=9, cor=INK):
    d.add(String(x, y, valor, fontName="Times-Roman", fontSize=tamanho, fillColor=cor))


def fio(d, pontos):
    for a, b in zip(pontos, pontos[1:]):
        d.add(Line(*a, *b, strokeColor=INK, strokeWidth=1.2))


def porta(d, tipo, x, y, entradas=2):
    p = ShapePath(strokeColor=TEAL, fillColor=colors.white, strokeWidth=1.4)
    if tipo == "NOT":
        p.moveTo(x, y - 9)
        p.lineTo(x, y + 9)
        p.lineTo(x + 20, y)
        p.closePath()
        d.add(p)
        d.add(Circle(x + 23, y, 3, strokeColor=TEAL, fillColor=colors.white))
        texto(d, x, y + 14, tipo, 8.5)
        return x + 26
    if tipo == "AND":
        p.moveTo(x, y - 18)
        p.lineTo(x, y + 18)
        p.lineTo(x + 18, y + 18)
        p.curveTo(x + 48, y + 18, x + 48, y - 18, x + 18, y - 18)
        p.closePath()
    else:
        p.moveTo(x, y - 18)
        p.curveTo(x + 12, y, x + 12, y, x, y + 18)
        p.curveTo(x + 25, y + 18, x + 38, y + 11, x + 47, y)
        p.curveTo(x + 38, y - 11, x + 25, y - 18, x, y - 18)
        p.closePath()
    d.add(p)
    for dy in ((-10, 10) if entradas == 2 else (-12, 0, 12)):
        fio(d, [(x - 8, y + dy), (x + (6 if tipo == "OR" else 0), y + dy)])
    texto(d, x + (15 if tipo == "OR" else 10), y - 3, tipo, 8.5)
    return x + (41 if tipo == "AND" else 47)


def diagrama():
    d = Drawing(510, 286)
    d.add(Rect(0, 0, 510, 286, fillColor=colors.white, strokeColor=None))
    texto(d, 10, 266, "F", 10)
    fio(d, [(24, 270), (402, 270)])
    texto(d, 412, 266, "Bloqueado", 10)
    texto(d, 10, 221, "F", 10)
    fio(d, [(24, 225), (60, 225)])
    nf = porta(d, "NOT", 60, 225)
    fio(d, [(nf, 225), (320, 225), (320, 215), (342, 215)])
    texto(d, 10, 191, "E", 10)
    fio(d, [(24, 195), (192, 195)])
    texto(d, 10, 151, "A", 10)
    texto(d, 10, 131, "P", 10)
    fio(d, [(24, 155), (82, 155)])
    fio(d, [(24, 135), (82, 135)])
    ap = porta(d, "AND", 90, 145)
    fio(d, [(ap, 145), (170, 145), (170, 175), (192, 175)])
    eo = porta(d, "OR", 200, 185)
    fio(d, [(eo, 185), (320, 185), (320, 195), (342, 195)])
    out = porta(d, "AND", 350, 205)
    fio(d, [(out, 205), (402, 205)])
    texto(d, 412, 201, "Autorizado", 10)
    d.add(Line(10, 118, 500, 118, strokeColor=GRAY))
    for label, y in (("F", 95), ("E", 65), ("A", 35), ("P", 5)):
        texto(d, 10, y - 3, label, 10)
        fio(d, [(24, y), (60, y)])
        fim = porta(d, "NOT", 60, y)
        if label == "F":
            fio(d, [(fim, y), (320, y), (320, 77), (342, 77)])
        elif label == "E":
            fio(d, [(fim, y), (342, y)])
        else:
            entrada = 30 if label == "A" else 10
            fio(d, [(fim, y), (160, y), (160, entrada), (192, entrada)])
    ao = porta(d, "OR", 200, 20)
    fio(d, [(ao, 20), (320, 20), (320, 53), (342, 53)])
    out = porta(d, "AND", 350, 65, entradas=3)
    fio(d, [(out, 65), (402, 65)])
    texto(d, 412, 61, "Adiado", 10)
    # Margem inferior para não cortar a ponta da última porta NOT.
    padded = Drawing(510, 306)
    grupo = Group(*d.contents)
    grupo.translate(0, 20)
    padded.add(grupo)
    return padded


def grafico():
    d = Drawing(510, 218)
    x0, y0, w, h = 45, 35, 425, 155
    d.add(Rect(0, 0, 510, 218, fillColor=colors.white, strokeColor=None))
    for c in (10, 30, 50, 70, 90):
        y = y0 + c / 100 * h
        d.add(Line(x0, y, x0+w, y, strokeColor=GRAY))
        texto(d, 18, y-3, str(c), 9.5)
    for t in (0, 2, 4, 8, 12, 16):
        x = x0 + t / 18 * w
        d.add(Line(x, y0, x, y0+h, strokeColor=GRAY))
        texto(d, x-4, 20, str(t), 9.5)
    fio(d, [(x0, y0+h), (x0, y0), (x0+w, y0)])
    texto(d, 8, 203, "Combustível (%)", 10)
    texto(d, 356, 3, "Espera (horas)", 10)
    reserva = y0 + 10/100*h
    d.add(Line(x0, reserva, x0+w, reserva, strokeColor=INK, strokeDashArray=[4, 3]))
    texto(d, 354, reserva+5, "Reserva: 10%", 9.5)
    for c0, cor in ((20, "#b85d36"), (50, "#157d87"), (90, "#375d96")):
        t = (c0 - 10) / 5
        x = x0 + t/18*w
        color = colors.HexColor(cor)
        d.add(Line(x0, y0+c0/100*h, x, reserva, strokeColor=color, strokeWidth=2))
        d.add(Circle(x, reserva, 3, fillColor=color, strokeColor=color))
        texto(d, x0+5, y0+c0/100*h+4, f"C(0)={c0}%", 9.5, color)
        texto(d, x-10, reserva-14, f"{int(t)} h", 9.5, color)
    return d


def salvar_figura(desenho, nome):
    renderSVG.drawToFile(desenho, str(DOC / f"{nome}.svg"))
    pdf = renderPDF.drawToString(desenho)
    with pymupdf.open(stream=pdf, filetype="pdf") as documento:
        documento[0].get_pixmap(matrix=pymupdf.Matrix(3, 3), alpha=False).save(DOC / f"{nome}.png")


def inline(s):
    s = html.escape(s).replace("–", "-").replace("—", "-")
    s = re.sub(r"\[([^]]+)\]\((https?://[^)]+)\)", r'<link href="\2" color="#303030"><u>\1</u></link>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r'<font face="Courier" size="8">\1</font>', s)
    s = re.sub(r"\bC0\b", "C<sub>0</sub>", s)
    s = re.sub(r"\bCmin\b", "C<sub>min</sub>", s)
    return re.sub(r"\bt_limite\b", "t<sub>limite</sub>", s)


def construir():
    fontes()
    salvar_figura(diagrama(), "image")
    salvar_figura(grafico(), "image-1")
    estilos = {
        "p": ParagraphStyle("p", fontName="Times-Roman", fontSize=10.5, leading=14,
                            textColor=INK, spaceAfter=7, alignment=TA_LEFT),
        "h1": ParagraphStyle("h1", fontName="Times-Bold", fontSize=22, leading=27,
                             textColor=INK, spaceAfter=15),
        "h2": ParagraphStyle("h2", fontName="Times-Bold", fontSize=15, leading=19,
                             textColor=TEAL, spaceAfter=12),
        "cell": ParagraphStyle("cell", fontName="Times-Roman", fontSize=9.5, leading=11.5,
                               textColor=INK),
        "caption": ParagraphStyle("caption", fontName="Times-Italic", fontSize=9,
                                  leading=10, textColor=INK, spaceAfter=8),
        "code": ParagraphStyle("code", fontName="Courier", fontSize=9, leading=12,
                               backColor=GRAY, borderPadding=8, spaceAfter=10),
        "eq": ParagraphStyle("eq", fontName="Times-Roman", fontSize=11, leading=16,
                             textColor=INK, spaceAfter=7, alignment=TA_CENTER),
    }
    story = []
    linhas = (DOC / "pdf.md").read_text().splitlines()
    largura = A4[0] - 88
    i = 0
    while i < len(linhas):
        s = linhas[i].strip()
        if not s:
            i += 1
            continue
        if s == "<!-- pagebreak -->":
            story.append(PageBreak())
        elif s.startswith("# ") or s.startswith("## "):
            nivel = "h1" if s.startswith("# ") else "h2"
            story.append(Paragraph(inline(s.lstrip("# ")), estilos[nivel]))
        elif re.fullmatch(r"\*\*(C\(t\)|t_limite) = .+\*\*", s):
            story.append(Paragraph(inline(s), estilos["eq"]))
        elif s.startswith("!["):
            match = re.fullmatch(r"!\[(.*?)\]\((.*?)\)", s)
            path = DOC / match[2]
            img = Image(str(path))
            largura_figura = min(largura, 440)
            img.drawHeight *= largura_figura / img.drawWidth
            img.drawWidth = largura_figura
            story.extend([img, Spacer(1, 5), Paragraph(inline(match[1]), estilos["caption"])])
        elif s.startswith("```"):
            code = []
            i += 1
            while not linhas[i].startswith("```"):
                code.append(html.escape(linhas[i]))
                i += 1
            story.append(Paragraph("<br/>".join(code), estilos["code"]))
        elif s.startswith("|"):
            rows = []
            while i < len(linhas) and linhas[i].startswith("|"):
                cells = [x.strip() for x in linhas[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", x) for x in cells):
                    rows.append([Paragraph(inline(x), estilos["cell"]) for x in cells])
                i += 1
            n = len(rows[0])
            ratios = {2: [0.32, 0.68], 3: [0.22, 0.39, 0.39],
                      4: [0.25, 0.14, 0.43, 0.18],
                      7: [0.20, 0.12, 0.09, 0.08, 0.10, 0.11, 0.20]}
            if "Integrante" in rows[0][0].getPlainText():
                ratios[n] = [0.34, 0.15, 0.51]
            table = Table(rows, colWidths=[largura*x for x in ratios.get(n, [1/n]*n)], repeatRows=1)
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), GRAY),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LINEBELOW", (0, 0), (-1, 0), 0.8, TEAL),
                ("LINEBELOW", (0, 1), (-1, -1), 0.3, GRAY),
            ]))
            story.extend([table, Spacer(1, 10)])
            continue
        else:
            paragraph = [s]
            while i+1 < len(linhas) and linhas[i+1].strip() and not linhas[i+1].startswith(("#", "|", "![", "```", "<!--")):
                i += 1
                paragraph.append(linhas[i].strip())
            story.append(Paragraph(inline(" ".join(paragraph)), estilos["p"]))
        i += 1

    def pagina(canvas, documento):
        canvas.setTitle("MGPEB - Relatório técnico | Missão Aurora Siger")
        canvas.setAuthor("Equipe PBL Fase 2 - Lorenzo, Davi, Eduardo, Gabriel e Guilherme")
        canvas.setStrokeColor(TEAL)
        canvas.line(44, A4[1]-35, A4[0]-44, A4[1]-35)
        canvas.setFont("Times-Roman", 8)
        canvas.setFillColor(INK)
        canvas.drawString(44, A4[1]-27, "FIAP - Atividade Integradora - Fase 2")
        canvas.drawString(44, 25, "Missão Aurora Siger - Grupo 2")
        canvas.drawRightString(A4[0]-44, 25, str(documento.page))

    output = DOC / "relatorio_mgpeb.pdf"
    SimpleDocTemplate(str(output), pagesize=A4, rightMargin=44, leftMargin=44,
                      topMargin=50, bottomMargin=44).build(story, onFirstPage=pagina, onLaterPages=pagina)
    with pymupdf.open(output) as pdf:
        if not 5 <= len(pdf) <= 10:
            raise ValueError(f"Relatório fora da faixa de 5–10 páginas: {len(pdf)}")
        print(f"Gerado {output.relative_to(ROOT)}: {len(pdf)} páginas")


if __name__ == "__main__":
    construir()

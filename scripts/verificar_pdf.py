"""Confere conteúdo/margens/links e renderiza cada página para revisão visual."""
import argparse
import tempfile
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]


def verificar(destino):
    destino.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(ROOT / "doc/relatorio_mgpeb.pdf") as pdf:
        assert len(pdf) == 8, f"Esperadas 8 páginas, encontradas {len(pdf)}"
        completo = "\n".join(p.get_text() for p in pdf)
        for rm in ("RM572772", "RM574229", "RM575361", "RM574746", "RM575889"):
            assert rm in pdf[0].get_text(), f"RM ausente da capa: {rm}"
        for termo in ("Bloqueado", "Autorizado", "Adiado", "ESG", "Anexo"):
            assert termo in completo, f"Conteúdo ausente: {termo}"
        assert "tlimite" in completo or "t_limite" in completo, "Fórmula de tempo limite ausente"
        assert "https://github.com/bkampdev/FIAP-PBL-FASE-2" in [
            link.get("uri") for link in pdf[0].get_links()
        ], "Link do repositório ausente da capa"
        for i, pagina in enumerate(pdf):
            assert pagina.get_text().strip(), f"Página {i+1} vazia"
            assert "\ufffd" not in pagina.get_text(), f"Caractere inválido na página {i+1}"
            for bloco in pagina.get_text("dict")["blocks"]:
                if bloco["type"] == 0:
                    for linha in bloco["lines"]:
                        for span in linha["spans"]:
                            x0, y0, x1, y1 = span["bbox"]
                            assert x0 >= 0 and y0 >= 0 and x1 <= pagina.rect.width and y1 <= pagina.rect.height, (
                                f"Texto fora da página {i+1}: {span['text']}"
                            )
            pagina.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False).save(
                destino / f"pagina-{i+1:02}.png"
            )
        assert pdf[2].get_images(), "Diagrama ausente"
        assert pdf[4].get_images(), "Gráfico ausente"
        print(f"PDF: 8 páginas, 5 RMs, diagrama/gráfico e links verificados; PNGs em {destino}")
        print("Abrir as oito imagens para conferir legibilidade, cortes, tabelas e expressões.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--saida", type=Path,
                        default=Path(tempfile.gettempdir()) / "fiap-pbl2-pdf-review")
    verificar(parser.parse_args().saida)

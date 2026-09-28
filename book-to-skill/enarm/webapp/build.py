#!/usr/bin/env python3
"""Empaqueta la app Repaso ENARM en archivos autocontenidos.

Genera en dist/:
  repaso-enarm.html  documento HTML completo: se abre con doble clic, sin
                     internet y sin servidor (apuntes, banco y código incluidos).
  artifact.html      la misma página sin <html>/<head>, para publicarla como
                     artifact de claude.ai.

Uso: python3 build.py
"""
import json
import pathlib
import re

AQUI = pathlib.Path(__file__).resolve().parent
REFS = AQUI.parent / "references"
DIST = AQUI / "dist"

ARCHIVOS = [
    "estrategia-examen.md", "ciencias-basicas.md", "neurologia-cardiologia.md",
    "neumologia-gastro.md", "endocrino-hemato-dermato.md",
    "nefro-urologia-ginecologia.md", "obstetricia-reumatologia.md",
    "psiquiatria-orl-geriatria-trauma.md",
]


def cargar_banco():
    banco, ids = [], set()
    for f in sorted((AQUI / "banco").glob("*.json")):
        for k, q in enumerate(json.loads(f.read_text(encoding="utf-8")), 1):
            q = dict(q)
            q.setdefault("id", f"{f.stem}-{k}")
            if q["id"] in ids:
                q["id"] = f"{f.stem}-{q['id']}"
            ids.add(q["id"])
            ok = (isinstance(q.get("opciones"), dict)
                  and all(q["opciones"].get(l) for l in "ABCD")
                  and q.get("correcta") in "ABCD" and len(q.get("correcta", "")) == 1)
            if not ok:
                print(f"  descartado (formato): {f.name} #{k}")
                continue
            banco.append(q)
    return banco


def main():
    apuntes = {f: (REFS / f).read_text(encoding="utf-8") for f in ARCHIVOS}
    banco = cargar_banco()
    datos = json.dumps({"apuntes": apuntes, "banco": banco}, ensure_ascii=False)
    datos = datos.replace("</", "<\\/")  # no cerrar el <script> antes de tiempo

    pagina = (AQUI / "index.html").read_text(encoding="utf-8")
    app = (AQUI / "app.js").read_text(encoding="utf-8")
    pagina = pagina.replace('<script id="enarm-data" type="application/json"></script>',
                            f'<script id="enarm-data" type="application/json">{datos}</script>')
    pagina = pagina.replace('<script src="app.js"></script>', f"<script>\n{app}</script>")
    assert "app.js" not in pagina.split("<script>")[0], "no se incrustó app.js"

    DIST.mkdir(exist_ok=True)
    (DIST / "artifact.html").write_text(pagina, encoding="utf-8")

    corte = pagina.index("</style>") + len("</style>")
    cabeza, cuerpo = pagina[:corte], pagina[corte:]
    completo = ("<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
                "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
                "<style>body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>\n"
                f"{cabeza}\n</head>\n<body>{cuerpo}\n</body>\n</html>\n")
    (DIST / "repaso-enarm.html").write_text(completo, encoding="utf-8")

    por = {}
    for q in banco:
        por[q["especialidad"]] = por.get(q["especialidad"], 0) + 1
    print(f"Banco: {len(banco)} reactivos")
    for e, n in sorted(por.items()):
        print(f"  {n:3}  {e}")
    for f in ("repaso-enarm.html", "artifact.html"):
        print(f"dist/{f}: {(DIST / f).stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()

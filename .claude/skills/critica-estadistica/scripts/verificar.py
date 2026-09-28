#!/usr/bin/env python3
"""Recalcula cifras que suelen reportarse de forma engañosa.

Solo usa la biblioteca estándar. Ejemplos:

    python verificar.py cambio 3 6
    python verificar.py proporcion 9 12
    python verificar.py diferencia 40 35 --n1 60 --n2 55
    python verificar.py raro 0.002 --n 1130
    python verificar.py descuentos 50 20
    python verificar.py indice 20,5 10,10
    python verificar.py ganancia 1.75 40
    python verificar.py rcv 2.5 5.0
    python verificar.py prestamo 6 12
"""

import argparse
import math
from statistics import NormalDist

Z95 = NormalDist().inv_cdf(0.975)


def wilson(x, n, z=Z95):
    p = x / n
    den = 1 + z**2 / n
    centro = (p + z**2 / (2 * n)) / den
    mitad = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / den
    return max(0.0, centro - mitad), min(1.0, centro + mitad)


def cmd_cambio(a):
    viejo, nuevo = a.viejo, a.nuevo
    print(f"De {viejo} a {nuevo}")
    print(f"  diferencia absoluta:     {nuevo - viejo:+g} (puntos, si son %)")
    if viejo:
        print(f"  cambio relativo:         {(nuevo - viejo) / viejo * 100:+.1f} %")
    if nuevo:
        print(f"  para volver a {viejo}:   {(viejo - nuevo) / nuevo * 100:+.1f} % "
              "sobre el valor nuevo")


def cmd_proporcion(a):
    lo, hi = wilson(a.x, a.n)
    print(f"{a.x}/{a.n} = {a.x / a.n * 100:.1f} %   IC 95 % (Wilson): "
          f"{lo * 100:.1f} % – {hi * 100:.1f} %")
    if a.n < 30:
        print("  Aviso: n < 30; reporta la fracción, no un porcentaje con decimales.")
    if a.x == 0:
        print(f"  Regla del 3: límite superior ≈ {3 / a.n * 100:.1f} %")


def cmd_diferencia(a):
    p1, p2 = a.p1 / 100, a.p2 / 100
    ee = math.sqrt(p1 * (1 - p1) / a.n1 + p2 * (1 - p2) / a.n2)
    d = p1 - p2
    z = d / ee if ee else float("inf")
    pval = 2 * (1 - NormalDist().cdf(abs(z)))
    print(f"{a.p1} % (n={a.n1}) vs {a.p2} % (n={a.n2})")
    print(f"  diferencia: {d * 100:+.1f} pp   IC 95 %: "
          f"{(d - Z95 * ee) * 100:+.1f} a {(d + Z95 * ee) * 100:+.1f} pp")
    print(f"  z = {z:.2f}   p ≈ {pval:.3f}")
    if abs(z) < Z95:
        print("  → No distinguible del azar con estos tamaños de muestra.")


def cmd_raro(a):
    if a.n:
        esperado = a.p * a.n
        print(f"Con incidencia {a.p * 100:g} % y n = {a.n}: se esperan "
              f"{esperado:.1f} casos.")
        if esperado < 10:
            print("  → Muy pocos eventos esperados; el estudio casi no puede "
                  "mostrar un efecto.")
    n_obj = math.ceil(a.eventos / a.p)
    print(f"Para esperar {a.eventos} eventos se necesitan n ≈ {n_obj} por grupo.")


def cmd_descuentos(a):
    factor = 1.0
    for d in a.porcentajes:
        factor *= 1 - d / 100
    suma = sum(a.porcentajes)
    print(f"Descuentos {' + '.join(f'{d:g} %' for d in a.porcentajes)}: "
          f"real {(1 - factor) * 100:.1f} % (no {suma:g} %)")


def _parse(s):
    return [float(v) for v in s.split(",")]


def cmd_indice(a):
    p0, p1 = _parse(a.periodo0), _parse(a.periodo1)
    if len(p0) != len(p1):
        raise SystemExit("Ambos periodos deben tener el mismo número de precios.")
    rel_0 = [b / x * 100 for x, b in zip(p0, p1)]
    rel_1 = [x / b * 100 for x, b in zip(p0, p1)]
    arit0 = sum(rel_0) / len(rel_0)
    arit1 = sum(rel_1) / len(rel_1)
    geo = math.exp(sum(math.log(r) for r in rel_0) / len(rel_0))
    print(f"Media aritmética, base periodo 0: {arit0:.1f}  "
          f"({arit0 - 100:+.1f} %)")
    print(f"Media aritmética, base periodo 1: periodo 0 = {arit1:.1f} "
          f"({arit1 - 100:+.1f} % respecto a hoy)")
    print(f"Media geométrica (cualquier base): {geo:.1f}  ({round(geo - 100, 9) + 0.0:+.1f} %)")


def cmd_ganancia(a):
    g = a.precio - a.costo
    print(f"Costo {a.costo:g}, precio {a.precio:g}, ganancia {g:g}")
    print(f"  sobre costo (markup):  {g / a.costo * 100:.1f} %")
    print(f"  sobre precio (margen): {g / a.precio * 100:.1f} %")


def cmd_rcv(a):
    rcv = math.sqrt(2) * Z95 * math.sqrt(a.cva**2 + a.cvi**2)
    print(f"CVa = {a.cva} %, CVi = {a.cvi} % → RCV (95 %, bilateral) = {rcv:.1f} %")
    print("  Cambios entre resultados seriados menores que esto no indican "
          "cambio real.")


def cmd_prestamo(a):
    # Cargo fijo "tasa_nominal por cada 100" sobre todo el principal,
    # pagado en `meses` cuotas iguales. Se resuelve la TIR mensual.
    principal = 100.0
    total = principal * (1 + a.tasa / 100 * a.meses / 12)
    cuota = total / a.meses

    def vp(r):
        return sum(cuota / (1 + r) ** k for k in range(1, a.meses + 1)) - principal

    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if vp(mid) > 0:
            lo = mid
        else:
            hi = mid
    anual = mid * 12
    efectiva = (1 + mid) ** 12 - 1
    print(f"'{a.tasa:g} por cada 100' anual, {a.meses} cuotas mensuales iguales")
    print(f"  tasa nominal anual real: {anual * 100:.1f} %   "
          f"efectiva anual: {efectiva * 100:.1f} %")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("cambio", help="puntos vs %% y recuperación")
    s.add_argument("viejo", type=float); s.add_argument("nuevo", type=float)
    s.set_defaults(f=cmd_cambio)

    s = sub.add_parser("proporcion", help="IC 95 %% de x/n")
    s.add_argument("x", type=int); s.add_argument("n", type=int)
    s.set_defaults(f=cmd_proporcion)

    s = sub.add_parser("diferencia", help="¿dos porcentajes difieren de verdad?")
    s.add_argument("p1", type=float); s.add_argument("p2", type=float)
    s.add_argument("--n1", type=int, required=True)
    s.add_argument("--n2", type=int, required=True)
    s.set_defaults(f=cmd_diferencia)

    s = sub.add_parser("raro", help="eventos esperados / n necesario")
    s.add_argument("p", type=float, help="incidencia como fracción (0.002)")
    s.add_argument("eventos", type=int, nargs="?", default=20)
    s.add_argument("--n", type=int)
    s.set_defaults(f=cmd_raro)

    s = sub.add_parser("descuentos", help="descuentos encadenados")
    s.add_argument("porcentajes", type=float, nargs="+")
    s.set_defaults(f=cmd_descuentos)

    s = sub.add_parser("indice", help="índice de precios según base y fórmula")
    s.add_argument("periodo0", help="precios separados por coma")
    s.add_argument("periodo1", help="precios separados por coma")
    s.set_defaults(f=cmd_indice)

    s = sub.add_parser("ganancia", help="markup vs margen")
    s.add_argument("costo", type=float); s.add_argument("precio", type=float)
    s.set_defaults(f=cmd_ganancia)

    s = sub.add_parser("rcv", help="valor de referencia de cambio (laboratorio)")
    s.add_argument("cva", type=float, help="CV analítico %%")
    s.add_argument("cvi", type=float, help="CV biológico intraindividual %%")
    s.set_defaults(f=cmd_rcv)

    s = sub.add_parser("prestamo", help="tasa real de un cargo 'por cada 100'")
    s.add_argument("tasa", type=float); s.add_argument("meses", type=int)
    s.set_defaults(f=cmd_prestamo)

    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()

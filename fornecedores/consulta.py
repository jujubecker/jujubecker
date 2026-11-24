#!/usr/bin/env python3
"""Consulta a base de precos (le todos os arquivos precos_*.csv da pasta).

Exemplos:
    python3 fornecedores/consulta.py --qtd 1000
    python3 fornecedores/consulta.py --qtd 5000 --tamanho GG
    python3 fornecedores/consulta.py --categoria rotulo --material BOPP
    python3 fornecedores/consulta.py --categoria rotulo --material BOPP --rotulo 5x5 --qtd 1000
"""

import argparse
import csv
import glob
import math
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

# Padrao de montagem de folha da skill faca-de-corte-m2
A3_L, A3_A = 29.7, 42.0      # cm
MARGEM = 0.7                 # cm em cada borda
ESPACO = 0.5                 # cm entre pecas


def carregar():
    linhas = []
    for caminho in sorted(glob.glob(os.path.join(BASE, "precos_*.csv"))):
        with open(caminho, newline="", encoding="utf-8") as fh:
            linhas.extend(csv.DictReader(fh))
    return linhas


def brl(valor):
    """Formata no padrao brasileiro: 1.234,56"""
    return f"{valor:,.2f}".translate(str.maketrans(",.", ".,"))


def na_faixa(row, qtd):
    if qtd is None:
        return True
    try:
        minimo = int(row["qtd_min"])
    except (ValueError, KeyError):
        return True
    if qtd < minimo:
        return False
    teto = (row.get("qtd_max") or "").strip()
    return not teto or qtd <= int(teto)


def contem(valor, filtro):
    return not filtro or filtro.lower() in (valor or "").lower()


def por_folha(larg, alt):
    """Quantas pecas de larg x alt cabem numa folha A3, testando os dois sentidos."""
    util_l = A3_L - 2 * MARGEM
    util_a = A3_A - 2 * MARGEM
    melhor = 0
    for l, a in ((larg, alt), (alt, larg)):
        if l > util_l or a > util_a:
            continue
        cols = math.floor((util_l + ESPACO) / (l + ESPACO))
        linhas = math.floor((util_a + ESPACO) / (a + ESPACO))
        melhor = max(melhor, cols * linhas)
    return melhor


def medida(texto):
    """Converte '5x5' ou '4,5x7' em (largura, altura) em cm."""
    try:
        l, a = texto.lower().replace(",", ".").split("x")
        return float(l), float(a)
    except ValueError:
        raise argparse.ArgumentTypeError("use o formato LARGURAxALTURA em cm, ex.: 5x5 ou 4,5x7")


def main():
    ap = argparse.ArgumentParser(description="Consulta precos de embalagens e etiquetas.")
    ap.add_argument("--qtd", type=int, help="quantidade desejada")
    ap.add_argument("--categoria", help="ex.: saco, sacola, rotulo")
    ap.add_argument("--tamanho", help="ex.: GG, G2, G1, M, A3")
    ap.add_argument("--material", help="ex.: BOPP, Couche, Kraft, Offset")
    ap.add_argument("--cores", help="ex.: 1/0, 4/0, digital")
    ap.add_argument("--fornecedor", help="filtra pelo nome do fornecedor")
    ap.add_argument(
        "--rotulo",
        type=medida,
        metavar="LxA",
        help="medida do rotulo em cm (ex.: 5x5): calcula quantos cabem na folha A3 "
        "e o custo por etiqueta",
    )
    args = ap.parse_args()

    todas = carregar()
    linhas = [
        r
        for r in todas
        if na_faixa(r, args.qtd)
        and contem(r.get("categoria"), args.categoria)
        and contem(r.get("tamanho"), args.tamanho)
        and contem(r.get("material"), args.material)
        and contem(r.get("cores_impressao"), args.cores)
        and contem(r.get("fornecedor"), args.fornecedor)
    ]

    if not linhas:
        print("Nenhum preco encontrado para esses filtros.")
        return 1

    linhas.sort(key=lambda r: float(r["preco_unit_brl"]))

    cab = f"{'Fornecedor':<20} {'Produto':<46} {'Preco':>9}  {'por':<10} {'Imp.':<12}"
    print(cab)
    print("-" * len(cab))
    for r in linhas:
        unit = float(r["preco_unit_brl"])
        print(
            f"{r['fornecedor'][:20]:<20} {r['produto'][:46]:<46} "
            f"{brl(unit):>9}  {r.get('unidade_venda', 'unidade'):<10} "
            f"{r['impostos_inclusos']:<12}"
        )

    # --- custo por etiqueta, a partir do preco da folha A3 ---
    if args.rotulo:
        larg, alt = args.rotulo
        cabem = por_folha(larg, alt)
        print()
        if not cabem:
            print(f"Um rotulo de {brl(larg)} x {brl(alt)} cm nao cabe numa folha A3.")
            print("Nesse caso o produto e cotado por m2, nao por folha.")
        else:
            print(
                f"Rotulo de {brl(larg)} x {brl(alt)} cm: cabem {cabem} por folha A3 "
                f"(margem de {MARGEM*10:.0f} mm, {ESPACO*10:.0f} mm entre pecas)."
            )
            print()
            area_peca = (larg + ESPACO) * (alt + ESPACO) / 1e4  # m2 ocupados por etiqueta

            for r in linhas:
                unidade = r.get("unidade_venda")
                preco = float(r["preco_unit_brl"])
                if unidade == "folha A3":
                    por_etiqueta = preco / cabem
                    base = f"{cabem} por folha"
                elif unidade == "m2":
                    por_etiqueta = preco * area_peca
                    base = f"{area_peca*1e4:.1f} cm2 por etiqueta"
                else:
                    continue
                extra = ""
                if args.qtd:
                    if unidade == "folha A3":
                        folhas = math.ceil(args.qtd / cabem)
                        extra = f"  {folhas} folhas = R$ {brl(folhas * preco)}"
                    else:
                        m2 = area_peca * args.qtd
                        extra = f"  {m2:.2f} m2 = R$ {brl(m2 * preco)}"
                print(
                    f"  {r['produto'][:44]:<44} {unidade:<9} R$ {brl(por_etiqueta):>7} /etiq "
                    f"({base}){extra}"
                )

            print()
            print(
                "Lembrete: por m2 voce nao paga a margem de 7 mm nem o retalho que sobra "
                "da folha.\n  O m2 sai mais barato em qualquer tamanho - confirmar so se "
                "a M2 cobra um minimo de m2."
            )

    # --- custo total, so para itens vendidos por unidade ---
    if args.qtd:
        unitarios = [r for r in linhas if r.get("unidade_venda", "unidade") == "unidade"]
        if unitarios:
            print()
            print(f"Custo total para {args.qtd:,} unidades:".replace(",", "."))
            for r in unitarios[:5]:
                total = float(r["preco_unit_brl"]) * args.qtd
                print(f"  {r['fornecedor'][:20]:<20} {r['produto'][:46]:<46} R$ {brl(total):>13}")

            ausentes = sorted({r["fornecedor"] for r in todas} - {r["fornecedor"] for r in linhas})
            if ausentes and not args.categoria:
                print()
                print(
                    "Sem preco para essa quantidade em: "
                    + ", ".join(ausentes)
                    + ". Alguns fornecedores cotam so quantidades fechadas - peca a cotacao exata."
                )
    return 0


if __name__ == "__main__":
    sys.exit(main())

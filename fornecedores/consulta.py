#!/usr/bin/env python3
"""Consulta a base de precos de embalagens.

Exemplos:
    python3 fornecedores/consulta.py --qtd 1000
    python3 fornecedores/consulta.py --qtd 5000 --tamanho GG
    python3 fornecedores/consulta.py --qtd 10000 --categoria saco --cores 1/0
"""

import argparse
import csv
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
PRECOS = os.path.join(BASE, "precos_embalagens.csv")


def carregar():
    with open(PRECOS, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def na_faixa(row, qtd):
    if qtd is None:
        return True
    try:
        minimo = int(row["qtd_min"])
    except (ValueError, KeyError):
        return True
    if qtd < minimo:
        return False
    teto = row.get("qtd_max", "").strip()
    return not teto or qtd <= int(teto)


def contem(valor, filtro):
    return not filtro or filtro.lower() in (valor or "").lower()


def brl(valor):
    """Formata um numero no padrao brasileiro: 1.234,56"""
    return f"{valor:,.2f}".translate(str.maketrans(",.", ".,"))


def main():
    ap = argparse.ArgumentParser(description="Consulta precos de embalagens por fornecedor.")
    ap.add_argument("--qtd", type=int, help="quantidade desejada (filtra a faixa de preco)")
    ap.add_argument("--categoria", help="ex.: saco, sacola, etiqueta")
    ap.add_argument("--tamanho", help="ex.: GG, G2, G1, M, M2")
    ap.add_argument("--cores", help="ex.: 1/0, 4/0")
    ap.add_argument("--fornecedor", help="filtra pelo nome do fornecedor")
    args = ap.parse_args()

    linhas = [
        r
        for r in carregar()
        if na_faixa(r, args.qtd)
        and contem(r["categoria"], args.categoria)
        and contem(r["tamanho"], args.tamanho)
        and contem(r["cores_impressao"], args.cores)
        and contem(r["fornecedor"], args.fornecedor)
    ]

    if not linhas:
        print("Nenhum preco encontrado para esses filtros.")
        return 1

    linhas.sort(key=lambda r: float(r["preco_unit_brl"]))

    cab = f"{'Fornecedor':<16} {'Produto':<38} {'Faixa':<14} {'Unit.':>8} {'Imp.':>12}"
    print(cab)
    print("-" * len(cab))
    for r in linhas:
        unit = float(r["preco_unit_brl"])
        print(
            f"{r['fornecedor']:<16} {r['produto'][:38]:<38} "
            f"{r['faixa_informada']:<14} {unit:>8.2f} {r['impostos_inclusos']:>12}"
        )

    if args.qtd:
        print()
        print(f"Custo total para {args.qtd:,} unidades:".replace(",", "."))
        for r in linhas[:5]:
            total = float(r["preco_unit_brl"]) * args.qtd
            print(f"  {r['fornecedor']:<16} {r['produto'][:38]:<38} R$ {brl(total):>13}")

        ausentes = sorted(
            {r["fornecedor"] for r in carregar()} - {r["fornecedor"] for r in linhas}
        )
        if ausentes:
            print()
            print(
                "Sem preco para essa quantidade em: "
                + ", ".join(ausentes)
                + ". Alguns fornecedores cotam apenas quantidades fechadas "
                "(500, 1.000, 5.000, 10.000) - peca a cotacao da quantidade exata."
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())

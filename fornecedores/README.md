# Base de fornecedores — embalagens, etiquetas e afins

Base de consulta para cotações de embalagens (sacos, sacolas), etiquetas e materiais
relacionados. Atualizada manualmente conforme chegam novas propostas.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `fornecedores.csv` | Cadastro dos fornecedores: CNPJ, contato, endereço, categorias atendidas |
| `precos_embalagens.csv` | Tabela de preços por produto e faixa de quantidade |
| `consulta.py` | Script de consulta: filtra e ordena preços por categoria, tamanho e quantidade |

## Como usar

```bash
python3 fornecedores/consulta.py --qtd 1000
```

```bash
python3 fornecedores/consulta.py --qtd 5000 --tamanho GG
```

## Dicionário de campos — `precos_embalagens.csv`

- **fornecedor_id** — chave que liga a `fornecedores.csv` (F001, F002, ...)
- **categoria** — `saco`, `sacola`, `etiqueta`, `fita`, etc.
- **produto / tamanho / medidas_cm** — identificação do item
- **material / gramatura** — Kraft 110g, Offset 150g, ...
- **cores_impressao** — `1/0` (uma cor, um lado), `4/0` (quatro cores, um lado), `sem impressão`
- **alca** — se tem alça e de que tipo
- **faixa_informada** — faixa de quantidade exatamente como o fornecedor passou
- **qtd_min / qtd_max** — faixa normalizada para cálculo (qtd_max vazio = sem limite)
- **preco_unit_brl** — preço por unidade em reais
- **impostos_inclusos** — `sim`, `nao` ou `a confirmar`
- **total_estimado_brl** — total da proposta para aquela quantidade, quando informado
- **data_cotacao / validade** — datas no formato ISO (AAAA-MM-DD)
- **referencia** — número da proposta ou origem do dado

## Situação atual

### F001 — Fornecedor 1 (a identificar)

Tabela de sacos em quatro tamanhos (GG, G2, G1, M), com desconto por volume:

| Tamanho | 500–999 | 1.000–9.999 | 10.000+ |
|---|---|---|---|
| GG | R$ 1,80 | R$ 1,60 | R$ 1,40 |
| G2 | R$ 1,60 | R$ 1,40 | R$ 1,20 |
| G1 | R$ 1,50 | R$ 1,30 | R$ 1,10 |
| M  | R$ 1,40 | R$ 1,30 | R$ 1,10 |

### F002 — Gráfica Olimac (Proposta 12716, 18/11/2026)

| Produto | 500 | 1.000 | 5.000 | 10.000 |
|---|---|---|---|---|
| SOS M2 — 1/0 cor, Kraft 110g, s/ alça | R$ 3,09 | R$ 2,23 | R$ 1,92 | R$ 1,88 |
| SOS M2 — 4/0 cores, Offset 150g, s/ alça | R$ 4,89 | R$ 3,55 | R$ 2,84 | R$ 2,76 |
| SOS GG c/ alça — 1/0 cor, Kraft 110g | R$ 3,49 | R$ 2,65 | R$ 2,36 | R$ 2,32 |
| SOS GG c/ alça — 4/0 cores, Offset 150g | R$ 5,39 | R$ 4,09 | R$ 3,43 | R$ 3,35 |

Medidas: M2 = 16,5x32,5x25,5 cm · GG = 30x32Ax19 cm
Acabamentos: corte/vinco, colagem de lateral e fundo com reforço; GG com aplicação de alça de papel.
Preços unitários com impostos embutidos.

## Pendências

1. **Identificar o F001** — nome, CNPJ e contato não registrados.
2. **Especificações técnicas do F001** — medidas de cada tamanho, material, gramatura,
   se o preço inclui impressão (e quantas cores), se tem alça. Sem isso a comparação com
   a Olimac não é válida: a diferença de 40% a 60% provavelmente reflete produtos diferentes,
   não vantagem de preço.
3. **Impostos no F001** — confirmar se o preço é com ou sem impostos. Na Olimac está embutido.
4. **Faixas sobrepostas no F001** — "500/1000" e "1.000/10.000" se encontram em 1.000;
   confirmar em qual faixa cai um pedido de exatamente 1.000 ou 10.000 unidades.
5. **Linha "G1 5000/1000"** — registrada como 500/1.000 por coerência com os outros tamanhos. Confirmar.
6. **Frete e prazo** — não informados por nenhum dos dois.
7. **Etiquetas** — nenhuma cotação ainda. Pedir para os dois.

## Observações contratuais (Olimac)

- Quantidade entregue pode oscilar ±10% — o custo real varia na mesma proporção.
- Tonalidade das cores pode oscilar ±10%.
- Validade da proposta: 7 dias a partir de 18/11/2026 (vence em 25/11/2026).
- Aprovação para entrega em dezembro: até 24/11/2026. Depois disso entra na grade de janeiro.
- Prazo de entrega e condição de pagamento: a combinar.

# Base de fornecedores — embalagens, etiquetas e afins

Base de consulta para cotações de embalagens (sacos, sacolas), etiquetas e materiais
relacionados. Atualizada manualmente conforme chegam novas propostas.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `fornecedores.csv` | Cadastro dos fornecedores: CNPJ, contato, endereço, categorias atendidas |
| `precos_embalagens.csv` | Preços de sacos e sacolas, por produto e faixa de quantidade |
| `precos_etiquetas.csv` | Preços de etiquetas e rótulos — mesmo esquema de colunas |
| `rotulos_aproveitamento.md` | Quantos rótulos cabem por m² e custo por etiqueta, de 3×3 a 7×7 |
| `consulta.py` | Script de consulta: lê todos os `precos_*.csv` e ordena por preço unitário |

## Como usar

```bash
python3 fornecedores/consulta.py --qtd 1000
```

```bash
python3 fornecedores/consulta.py --qtd 5000 --tamanho GG
```

```bash
python3 fornecedores/consulta.py --categoria rotulo --material BOPP
```

## Dicionário de campos — `precos_embalagens.csv`

- **fornecedor_id** — chave que liga a `fornecedores.csv` (F001, F002, ...)
- **categoria** — `saco`, `sacola`, `etiqueta`, `fita`, etc.
- **produto / tamanho / medidas_cm** — identificação do item (medidas em largura x altura x fundo)
- **material / gramatura** — Kraft 110g, Offset 150g, ...
- **cores_impressao** — `1/0` (uma cor, um lado), `4/0` (quatro cores, um lado), `sem impressão`
- **alca** — se tem alça e de que tipo
- **faixa_informada** — faixa de quantidade exatamente como o fornecedor passou
- **qtd_min / qtd_max** — faixa normalizada para cálculo (qtd_max vazio = sem limite)
- **unidade_venda** — a que o preço se refere: `unidade`, `folha A3` ou `m2`
- **preco_unit_brl** — preço em reais, na unidade indicada acima
- **impostos_inclusos** — `sim`, `nao` ou `a confirmar`
- **total_estimado_brl** — total da proposta para aquela quantidade, quando informado
- **data_cotacao / validade** — datas no formato ISO (AAAA-MM-DD)
- **referencia** — número da proposta ou origem do dado

## Fornecedores

### F001 — Embaré Kraft

Contato: WhatsApp (21) 99810-9745 e (21) 98387-6085 · Instagram [@embarekraft](https://instagram.com/embarekraft)

Linha de papel kraft em cinco tamanhos, cada um nas versões **sacola** (com alça torcida)
e **saco** (sem alça). Faz personalização com logo.

| Tamanho | Medidas (L x A x F) | Volume | 500–999 | 1.000–9.999 | 10.000+ |
|---|---|---|---|---|---|
| GG | 31 x 32 x 19 cm | 18,8 L | R$ 1,80 | R$ 1,60 | R$ 1,40 |
| G2 | 28 x 38 x 15 cm | 16,0 L | R$ 1,60 | R$ 1,40 | R$ 1,20 |
| G1 | 22 x 34 x 14 cm | 10,5 L | R$ 1,50 | R$ 1,30 | R$ 1,10 |
| M  | 22 x 32 x 12 cm |  8,4 L | R$ 1,40 | R$ 1,30 | R$ 1,10 |
| P  | 18 x 24 x 12 cm |  5,2 L | — | — | — |

Os preços acima foram passados como **saco** (sem alça). Preço do P e da versão sacola ainda não informados.

### F002 — Gráfica Olimac (Proposta 12716, 18/11/2026)

CNPJ 27.714.163/0001-92 · Rua Senador Alencar, 280 — São Cristóvão, Rio de Janeiro/RJ
· (21) 3253-0625 · contato@graficaolimac.com.br

| Produto | Medidas | Volume | 500 | 1.000 | 5.000 | 10.000 |
|---|---|---|---|---|---|---|
| SOS M2 — 1/0 cor, Kraft 110g, s/ alça | 16,5 x 32,5 x 25,5 | 13,7 L | R$ 3,09 | R$ 2,23 | R$ 1,92 | R$ 1,88 |
| SOS M2 — 4/0 cores, Offset 150g, s/ alça | 16,5 x 32,5 x 25,5 | 13,7 L | R$ 4,89 | R$ 3,55 | R$ 2,84 | R$ 2,76 |
| SOS GG c/ alça — 1/0 cor, Kraft 110g | 30 x 32 x 19 | 18,2 L | R$ 3,49 | R$ 2,65 | R$ 2,36 | R$ 2,32 |
| SOS GG c/ alça — 4/0 cores, Offset 150g | 30 x 32 x 19 | 18,2 L | R$ 5,39 | R$ 4,09 | R$ 3,43 | R$ 3,35 |

Acabamentos: corte/vinco, colagem de lateral e fundo com reforço; GG com aplicação de alça de papel
(kraft na versão 1/0, branca na 4/0). Preços unitários com impostos embutidos.

### F003 — M2 Flex / M2 Store (etiquetas e rótulos)

**Fornecedor padrão para etiquetas.** Impressão digital, cor 4/0.
Duas modalidades: **Meio Corte + Depilado em Folha** (preço fechado por folha A3) e
**Meio Corte + Depilado** (preço por m², com largura e altura informadas).
Não há desconto por faixa de quantidade — o preço é fixo e o total só multiplica.

**Regra padrão:** etiqueta = **rótulo de BOPP com impressão digital**.
Exceção única: **delivery**, quando especificado — aí é **etiqueta de papel**, porque precisa rasgar.

#### Folha A3 (só com mídia Adesivo Brilho)

| Papel | Por folha | Preço cheio |
|---|---|---|
| Couchê Brilho, sem laminação | R$ 3,91 | R$ 4,20 |
| Couchê Brilho + laminação | ~R$ 4,41 | — |
| **BOPP, sem laminação** | **R$ 4,65** | R$ 5,00 |
| BOPP + laminação | ~R$ 5,15 | — |

#### Por m²

| Papel / mídia | Por m² | Preço cheio |
|---|---|---|
| Couchê Brilho + Adesivo Brilho, sem laminação | R$ 34,41 | R$ 37,00 |
| Couchê Brilho, com laminação | R$ 38,41 | — |
| **BOPP** (Adesivo Brilho, Transparente Brilho ou Metalizada), sem laminação | **R$ 39,06** | R$ 42,00 |
| BOPP, com laminação | R$ 43,06 | — |

- **Laminação** brilho ou fosca: R$ 4,00/m², equivalente a R$ 0,50 por folha A3. Soma +1 dia útil.
- **Prazo**: 3 dias úteis, +1 com laminação. Algumas modalidades de frete somam mais 1 dia.
- **Promoção Black Friday GR 26** válida até **30/11/2026 às 23:59**. Depois disso valem os preços cheios.
- Dados levantados no **ambiente de homologação** — conferir com a tabela oficial antes de passar para revenda.

#### O m² sempre compensa mais que a folha A3

A comparação certa não é o preço da área da folha, e sim **o custo da etiqueta que sai dela**.

A folha A3 tem 0,12474 m², mas você paga ela inteira e só aproveita 0,11490 m²: os 7 mm de
margem em cada borda são área morta que entra no preço. No m² você informa largura e altura,
então não paga margem — só o espaço de 5 mm entre as peças. Somado ao retalho que sobra
quando a peça não preenche a folha, o m² ganha sempre:

| Rótulo | Cabem na A3 | R$/etiq. via folha | R$/etiq. via m² | m² é |
|---|---|---|---|---|
| 2 × 2 cm | 176 | R$ 0,0264 | R$ 0,0244 | 7,6% mais barato |
| 3 × 3 cm | 88 | R$ 0,0528 | R$ 0,0478 | 9,4% |
| 5 × 5 cm | 35 | R$ 0,1329 | R$ 0,1182 | 11,1% |
| 7 × 10 cm | 10 | R$ 0,4650 | R$ 0,3076 | 33,9% |
| 10 × 15 cm | 4 | R$ 1,1625 | R$ 0,6357 | 45,3% |
| 15 × 20 cm | 2 | R$ 2,3250 | R$ 1,2411 | 46,6% |

Quanto maior a peça, maior o desperdício da folha e maior a vantagem do m².

**Mesmo no melhor caso da folha** — 100% da área útil ocupada, zero sobra — o m² sairia
R$ 4,49 contra R$ 4,65. Não existe tamanho em que a folha A3 ganhe.

O m² ainda tem mais opção de mídia: BOPP Transparente Brilho e Metalizada só existem nessa
modalidade. Na folha A3 é só Adesivo Brilho.

> Único cenário a verificar: se a M2 cobrar um **mínimo de m²** por pedido, um pedido muito
> pequeno pode acabar saindo mais caro no m². Confirmar.

#### Custo por etiqueta

O custo unitário depende do aproveitamento. O script calcula os dois caminhos no padrão de
montagem da skill `faca-de-corte-m2` (margem de 7 mm, 5 mm entre peças, testando os dois
sentidos da folha):

```bash
python3 fornecedores/consulta.py --categoria rotulo --material BOPP --rotulo 5x5 --qtd 1000
```

Para um rótulo de 5 × 5 cm em BOPP: 35 cabem por folha A3, a R$ 0,1329 cada — contra
R$ 0,1182 pedindo por m². **Cotar por m².**

A tabela pronta de 3 × 3 a 7 × 7, redondo e quadrado, está em
[`rotulos_aproveitamento.md`](rotulos_aproveitamento.md).

> **Cuidado com o termo "M2":** aqui ele é a revenda **M2 Flex**. O **SOS M2** da Olimac é
> um tamanho de saco (16,5 × 32,5 × 25,5 cm). São coisas diferentes.

## Equivalência de tamanhos entre os dois fornecedores de embalagem

Só existe **um par diretamente comparável**: o GG.

| Volume | Embaré | Olimac |
|---|---|---|
| 18,8 L | GG — 31x32x19 | |
| 18,2 L | | SOS GG — 30x32x19 |
| 16,0 L | G2 — 28x38x15 | |
| 13,7 L | | SOS M2 — 16,5x32,5x25,5 |
| 10,5 L | G1 — 22x34x14 | |
| 8,4 L | M — 22x32x12 | |
| 5,2 L | P — 18x24x12 | |

O SOS M2 da Olimac não tem equivalente na Embaré, e a diferença não é só de volume: é um saco
**estreito e fundo** (16,5 cm de largura por 25,5 cm de fundo), formato de delivery/garrafa.
Os da Embaré são largos e rasos. Não dá para substituir um pelo outro sem testar o produto que vai dentro.

## Pendências

1. **Preço da versão sacola (com alça) na Embaré** — é o que compara com o SOS GG da Olimac.
2. **Preço do tamanho P na Embaré.**
3. **Impressão na Embaré** — o preço de tabela inclui? Quantas cores? Qual o custo adicional?
4. **Gramatura do papel da Embaré** — a Olimac usa Kraft 110g e Offset 150g. Sem esse dado
   não dá para comparar resistência.
5. **Impostos na Embaré** — com ou sem? Na Olimac está embutido no preço unitário.
6. **CNPJ e endereço da Embaré** — a empresa não aparece em buscadores; contato só por
   WhatsApp e Instagram. Pedir dados cadastrais e nota fiscal antes de fechar volume alto.
7. **Faixas sobrepostas na Embaré** — "500/1000" e "1.000/10.000" se encontram em 1.000;
   confirmar em qual faixa cai um pedido de exatamente 1.000 ou 10.000 unidades.
8. **Linha "G1 5000/1000"** — registrada como 500/1.000 por coerência com os outros tamanhos. Confirmar.
9. **Frete e prazo de produção** — não informados por nenhum dos dois.
10. **Mínimo de m² por pedido na M2** — se existir, é o único caso em que a folha A3 poderia
    compensar.
11. **Confirmar os preços da M2 na tabela oficial** — os valores vieram do ambiente de homologação.
12. **Imposto na M2** — os preços de revenda são com ou sem?
13. **Laminação por folha A3** — o valor de R$ 0,50 é cálculo a partir do preço por m².
    Confirmar no carrinho.
14. **Etiqueta de papel para delivery** — o Couchê Brilho serve? Confirmar se rasga como
    a aplicação de delivery exige, ou se existe outra opção na M2.

## Observações contratuais (Olimac)

- Quantidade entregue pode oscilar ±10% — o custo real varia na mesma proporção.
- Tonalidade das cores pode oscilar ±10%.
- Validade da proposta: 7 dias a partir de 18/11/2026 (vence em 25/11/2026).
- Aprovação para entrega em dezembro: até 24/11/2026. Depois disso entra na grade de janeiro.
- Prazo de entrega e condição de pagamento: a combinar.

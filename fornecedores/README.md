# Base de fornecedores — embalagens, etiquetas e afins

Base de consulta para cotações de embalagens (sacos, sacolas), etiquetas e materiais
relacionados. Atualizada manualmente conforme chegam novas propostas.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `fornecedores.csv` | Cadastro dos fornecedores: CNPJ, contato, endereço, categorias atendidas |
| `precos_embalagens.csv` | Preços de sacos e sacolas, por produto e faixa de quantidade |
| `precos_etiquetas.csv` | Preços de etiquetas e rótulos — mesmo esquema de colunas (ainda vazio) |
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
- **preco_unit_brl** — preço por unidade em reais
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

### F003 — M2 Flex (etiquetas e rótulos)

Base de revenda. **Fornecedor padrão para etiquetas.** A tabela de preços ainda não foi
carregada — `precos_etiquetas.csv` está só com o cabeçalho.

**Regra padrão:** etiqueta = **rótulo de BOPP com impressão digital**, pela base de revenda da M2.
Exceção única: **delivery**, quando especificado — aí é **etiqueta de papel**, porque precisa rasgar.

O padrão de faca de corte da M2 Flex está na skill `faca-de-corte-m2`.

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
10. **Tabela de rótulos da M2 Flex** — carregar em `precos_etiquetas.csv`: material
    (BOPP branco, transparente, metalizado), medidas, faixas de quantidade, acabamento
    (verniz, laminação), tipo de corte e preço por unidade ou por metro de rolo.
11. **Etiqueta de papel para delivery** — levantar a opção na M2 para quando o pedido pedir.

## Observações contratuais (Olimac)

- Quantidade entregue pode oscilar ±10% — o custo real varia na mesma proporção.
- Tonalidade das cores pode oscilar ±10%.
- Validade da proposta: 7 dias a partir de 18/11/2026 (vence em 25/11/2026).
- Aprovação para entrega em dezembro: até 24/11/2026. Depois disso entra na grade de janeiro.
- Prazo de entrega e condição de pagamento: a combinar.

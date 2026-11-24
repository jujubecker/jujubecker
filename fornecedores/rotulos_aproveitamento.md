# Rótulos M2 — aproveitamento e custo por etiqueta

Quantos rótulos cabem por m² e quanto custa cada um, de 3×3 a 7×7 cm.
Base: BOPP, impressão digital 4/0, meio corte + depilado.

## Regras confirmadas com a Juliana

- **A faca é montada por nós** — a montagem é livre, desde que respeite o espaçamento.
- **Espaçamento de 5 mm entre peças, sempre.** Não é folga arbitrária: cada peça sangra
  2 mm, duas peças encostando dão 2 + 2 = 4 mm, mais 1 mm de distância = 5 mm.
- **Imposto já incluso** nos preços de revenda.
- **Sem taxa de arte, faca ou setup** — nada a diluir no preço.
- **Mínimo de 1 m²** na modalidade por m². Abaixo disso, pedir por folha A3.
- **O sistema calcula o m²** a partir do tamanho da peça e da quantidade informados.

---

## Quantos cabem

Célula ocupada por etiqueta = (lado + 0,5 cm)². Vale igual para redondo e quadrado
em arranjo de grade: a faca trabalha dentro do quadrado que envolve o círculo.

| Tamanho | Célula | Por m² (grade) | Por folha A3 | Por m² (hexagonal, só redondo) |
|---|---|---|---|---|
| 3 × 3 | 12,25 cm² | 816 | 88 | 942 |
| 4 × 4 | 20,25 cm² | 494 | 54 | 570 |
| 5 × 5 | 30,25 cm² | 331 | 35 | 382 |
| 6 × 6 | 42,25 cm² | 237 | 24 | 273 |
| 7 × 7 | 56,25 cm² | 178 | 15 | 205 |

Folha A3 calculada com margem de 7 mm na borda (limite de impressão da folha) e os
mesmos 5 mm entre peças.

---

## Onde vira de folha para m²

Com mínimo de 1 m², a modalidade m² começa cobrando R$ 39,06 mesmo para uma etiqueta —
o equivalente a 8,4 folhas A3. Abaixo da virada, a folha é sempre mais barata.

| Tamanho | **Vira em** | Na virada: A3 | Na virada: m² |
|---|---|---|---|
| 3 × 3 | 705 un | R$ 41,85 | R$ 39,06 |
| 4 × 4 | 433 un | R$ 41,85 | R$ 39,06 |
| 5 × 5 | 281 un | R$ 41,85 | R$ 39,06 |
| 6 × 6 | 193 un | R$ 41,85 | R$ 39,06 |
| 7 × 7 | 121 un | R$ 41,85 | R$ 39,06 |

Quanto maior a etiqueta, mais cedo o m² passa a compensar — porque cabem menos por folha.

### Custo por etiqueta nas duas modalidades

| | 3 × 3 | 4 × 4 | 5 × 5 | 6 × 6 | 7 × 7 |
|---|---|---|---|---|---|
| **100 un** | A3 R$ 0,0930 | A3 R$ 0,0930 | A3 R$ 0,1395 | A3 R$ 0,2325 | A3 R$ 0,3255 |
| **250 un** | A3 R$ 0,0558 | A3 R$ 0,0930 | A3 R$ 0,1488 | m² R$ 0,1650 | m² R$ 0,2197 |
| **500 un** | A3 R$ 0,0558 | m² R$ 0,0791 | m² R$ 0,1182 | m² R$ 0,1650 | m² R$ 0,2197 |
| **1.000 un** | m² R$ 0,0478 | m² R$ 0,0791 | m² R$ 0,1182 | m² R$ 0,1650 | m² R$ 0,2197 |
| **5.000 un** | m² R$ 0,0478 | m² R$ 0,0791 | m² R$ 0,1182 | m² R$ 0,1650 | m² R$ 0,2197 |

A modalidade indicada é a mais barata em cada caso. Preços da promoção, válidos até 30/11.

**Piso de custo por etiqueta** (m², acima da virada, promoção):
3 × 3 → R$ 0,0478 · 4 × 4 → R$ 0,0791 · 5 × 5 → R$ 0,1182 · 6 × 6 → R$ 0,1650 · 7 × 7 → R$ 0,2197

A partir de 01/12, com o preço cheio de R$ 42,00/m², some 7,5% a todos eles.

---

## A questão em aberto: o encaixe hexagonal chega até o preço?

Como a faca é nossa, um rótulo **redondo** pode ser montado em fileiras alternadas, deslocadas
em meio passo. Isso rende **15,5% a mais** por m²:

| Tamanho | Grade | Hexagonal | Custo/etiq. em grade | Custo/etiq. em hexagonal |
|---|---|---|---|---|
| 3 × 3 | 816/m² | 942/m² | R$ 0,0478 | R$ 0,0414 |
| 4 × 4 | 494/m² | 570/m² | R$ 0,0791 | R$ 0,0685 |
| 5 × 5 | 331/m² | 382/m² | R$ 0,1182 | R$ 0,1023 |
| 6 × 6 | 237/m² | 273/m² | R$ 0,1650 | R$ 0,1429 |
| 7 × 7 | 178/m² | 205/m² | R$ 0,2197 | R$ 0,1903 |

**Mas o ganho só é real se o sistema cobrar pela montagem, e não pela fórmula dele.**
Se o sistema calcula o m² a partir do tamanho da peça e da quantidade, ele provavelmente
aplica uma área fixa por etiqueta — e nesse caso a montagem mais apertada economiza material
da M2, não o nosso custo.

Como descobrir: ver que m² o sistema devolve para entradas conhecidas (seção seguinte).

---

## Teste para mapear a fórmula do sistema

O sistema pede tamanho da peça e quantidade, e devolve o m². Rodando estas entradas e
anotando o m² de cada uma, dá para saber exatamente como ele calcula — e aí a base passa a
prever o custo sem precisar consultar.

| # | Peça | Quantidade | m² que o sistema devolve |
|---|---|---|---|
| 1 | 5 × 5 | 1 | |
| 2 | 5 × 5 | 100 | |
| 3 | 5 × 5 | 331 | |
| 4 | 5 × 5 | 1.000 | |
| 5 | 3 × 3 | 1.000 | |
| 6 | 7 × 7 | 1.000 | |
| 7 | 5 × 5 redondo | 1.000 | |

O que cada linha revela:

- **1 e 2** — se devolve menos de 1 m², existe mínimo na cobrança ou só no pedido.
- **2, 3 e 4** — se o m² cresce proporcional à quantidade, a fórmula é área fixa por etiqueta.
  Se cresce em degraus, ele monta em folhas.
- **4 contra 5 e 6** — qual espaçamento ele assume. Se 5 × 5 com 1.000 der 3,025 m²,
  ele usa os mesmos 5 mm. Se der 2,5 m², não considera espaçamento nenhum.
- **7 contra 4** — se o resultado for menor para o redondo, o sistema reconhece encaixe
  hexagonal e os 15,5% são nossos. Se for igual, redondo e quadrado custam o mesmo e não
  adianta apertar a montagem.

---

## Pendência restante

Os preços foram levantados no **ambiente de homologação** da M2 Store, conforme o próprio
documento de origem registra. Conferir com a tabela oficial; se baterem, remover a ressalva
das oito linhas de `precos_etiquetas.csv`.

## Alerta de prazo

Promoção **Black Friday GR 26 até 30/11/2026, 23:59**. Fechamento em dezembro usa o preço
cheio: BOPP passa de R$ 39,06 para R$ 42,00 o m², e de R$ 4,65 para R$ 5,00 a folha A3.

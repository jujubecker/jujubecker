# Contexto do repositório

## Embalagens e etiquetas (`fornecedores/`)

Base de fornecedores e preços usada para cotar embalagens, etiquetas e materiais
relacionados. Ver [`fornecedores/README.md`](fornecedores/README.md) para a estrutura.

### Regra padrão para etiquetas

Quando o assunto for **etiqueta**, assumir sempre:

> **Rótulo de BOPP, impressão digital, pela base de revenda da M2 (M2 Flex).**

Exceção única: **delivery**, e só quando a Juliana especificar. Nesse caso a etiqueta é
de **papel**, porque precisa rasgar. Sem essa especificação explícita, vale o BOPP.

Não perguntar qual material a cada pedido — partir do BOPP e seguir. Se o pedido for de
delivery mas ela não disser o material, aí sim vale uma pergunta curta.

### Atenção a "M2" — o termo tem dois significados

- **M2 Flex** — a revenda, fornecedor de rótulos e base padrão para etiquetas.
- **SOS M2** — um tamanho de saco da Gráfica Olimac (16,5 × 32,5 × 25,5 cm).

Nunca confundir os dois ao ler ou escrever na base de preços.

### Faca de corte

Para facas de corte existe a skill `faca-de-corte-m2`, no padrão de produção da M2 Flex.
Usar essa skill, e não improvisar, quando o pedido envolver faca.

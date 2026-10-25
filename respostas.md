# Respostas da Atividade: Rastreador de Causalidade

## 1. Qual posição do vetor pertence ao Processo A, B e C?

- Posição 0: Processo A.
- Posição 1: Processo B.
- Posição 2: Processo C.

Cada posição representa a quantidade de eventos conhecidos de cada processo. Por exemplo, o vetor `[2, 3, 0]` indica que são conhecidos dois eventos de A, três de B e nenhum de C.

## 2. O que aconteceu com o vetor de B quando ele recebeu uma mensagem de A?

Antes de receber a mensagem, B possuía o vetor `[0, 1, 0]`. A enviou o vetor `[2, 0, 0]`.

B comparou cada posição dos dois vetores e manteve o maior valor, obtendo `[2, 1, 0]`. Em seguida, incrementou sua própria posição devido ao evento de recebimento.

O vetor final de B passou a ser `[2, 2, 0]`.

## 3. Por que C passa a conhecer eventos de A mesmo sem receber uma mensagem diretamente de A?

Isso acontece porque B recebeu uma mensagem de A e incorporou as informações do vetor de A ao seu próprio relógio. Quando B enviou uma mensagem a C, transmitiu também esse conhecimento causal.

Assim, C passou a conhecer indiretamente os eventos de A.

## 4. Que informação foi propagada por B?

B propagou o conhecimento acumulado dos eventos de A e dos próprios eventos de B registrados até o momento do envio. O vetor acompanha a mensagem para transmitir essas informações causais.

## 5. O vetor representa horário real? Explique.

Não. O relógio vetorial não representa horas, minutos ou segundos. Ele representa a ordem lógica dos eventos e permite identificar relações de causalidade entre processos distribuídos, sem exigir sincronização dos relógios físicos.

## 6. Desafio: eventos concorrentes

Considere os vetores:

- D1 = `[2, 0, 0]`
- D2 = `[0, 2, 0]`

D1 não aconteceu antes de D2, pois sua primeira posição é maior que a primeira posição de D2.

D2 também não aconteceu antes de D1, pois sua segunda posição é maior que a segunda posição de D1.

Portanto, os eventos são concorrentes, pois não existe uma relação causal estabelecida entre eles pelos vetores.

## 7. Desafio extra: função de comparação

A função `aconteceu_antes(v1, v2)` retorna verdadeiro quando todas as posições de `v1` são menores ou iguais às posições correspondentes de `v2`, e pelo menos uma posição é estritamente menor.

Resultados:

- `[1, 0, 0]` aconteceu antes de `[2, 1, 0]`: **True**.
- `[2, 1, 0]` aconteceu antes de `[0, 2, 0]`: **False**.

O segundo resultado é falso porque a primeira posição do primeiro vetor é maior que a do segundo vetor.

## Conclusão

Os relógios vetoriais permitem acompanhar a causalidade entre eventos em sistemas distribuídos. Eles ajudam a identificar quando um evento aconteceu antes de outro e quando os eventos são concorrentes.

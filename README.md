# Rastreador de Causalidade

## Atividade prática de Sistemas Distribuídos

### Objetivo
Desenvolver um programa em Python que simula três processos (A, B e C) usando relógios vetoriais para acompanhar eventos e identificar relações de causalidade.

### Tecnologias utilizadas
- Python 3
- Relógios vetoriais
- Sistemas distribuídos

### Funcionalidades
- Criação de três processos.
- Registro de eventos locais.
- Envio e recebimento de mensagens.
- Atualização dos relógios vetoriais.
- Propagação de informações causais.
- Comparação de vetores.
- Identificação de eventos concorrentes.

### Como executar
Com o Python 3 instalado, execute no terminal:

```bash
python vetor.py
```

No Windows, também é possível usar:

```bash
py vetor.py
```

### Arquivos do projeto
- `vetor.py`: código-fonte do programa.
- `README.md`: documentação do projeto.
- `respostas.md`: respostas às perguntas da atividade.

### Conceito principal
Os relógios vetoriais permitem determinar se existe uma relação causal entre eventos em processos distribuídos. Eles não representam o horário real, mas registram o conhecimento lógico de cada processo.

### Conclusão
A atividade demonstra como informações sobre eventos são propagadas entre processos e como os vetores permitem distinguir eventos causalmente relacionados de eventos concorrentes.


class Processo:
    def __init__(self, nome, indice, total):
        self.nome = nome
        self.indice = indice
        self.vetor = [0] * total

    def mostrar(self, evento):
        print(self.nome, evento, "->", self.vetor)

    def evento_local(self, descricao):
        self.vetor[self.indice] += 1
        self.mostrar(descricao)

    def enviar(self, mensagem):
        self.vetor[self.indice] += 1
        self.mostrar("ENVIA: " + mensagem)
        return self.vetor.copy()

    def receber(self, mensagem, vetor_recebido):
        for i in range(len(self.vetor)):
            self.vetor[i] = max(
                self.vetor[i], vetor_recebido[i]
            )

        self.vetor[self.indice] += 1
        self.mostrar("RECEBE: " + mensagem)


def aconteceu_antes(v1, v2):
    menor_ou_igual = all(
        a <= b for a, b in zip(v1, v2)
    )

    estritamente_menor = any(
        a < b for a, b in zip(v1, v2)
    )

    return menor_ou_igual and estritamente_menor


if __name__ == "__main__":
    # Passo 4: criar os tres processos
    A = Processo("A", 0, 3)
    B = Processo("B", 1, 3)
    C = Processo("C", 2, 3)

    # Eventos locais
    A.evento_local("criou pedido")
    B.evento_local("consultou estoque")
    C.evento_local("iniciou faturamento")

    # Passo 5: enviar mensagem de A para B
    vetor_A = A.enviar("pedido criado")
    B.receber("pedido criado", vetor_A)

    # Passo 6: B processa e envia para C
    B.evento_local("reservou estoque")

    vetor_B = B.enviar("estoque reservado")
    C.receber("estoque reservado", vetor_B)

    # Desafio: eventos concorrentes
    print("\n--- Desafio: eventos concorrentes ---")

    D1 = [2, 0, 0]
    D2 = [0, 2, 0]

    print("Evento 1:", D1)
    print("Evento 2:", D2)
    print("D1 aconteceu antes de D2?",
          aconteceu_antes(D1, D2))
    print("D2 aconteceu antes de D1?",
          aconteceu_antes(D2, D1))

    concorrentes = (
        not aconteceu_antes(D1, D2)
        and not aconteceu_antes(D2, D1)
    )

    print("Eventos concorrentes?", concorrentes)

    # Testes da funcao de comparacao
    print("\n--- Testes da funcao de comparacao ---")

    v1 = [1, 0, 0]
    v2 = [2, 1, 0]
    v3 = [0, 2, 0]

    print("v1 antes de v2?",
          aconteceu_antes(v1, v2))
    print("v2 antes de v3?",
          aconteceu_antes(v2, v3))

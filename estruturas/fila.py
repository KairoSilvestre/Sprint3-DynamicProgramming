class Fila:
    def __init__(self):
        # Inicializa a fila como uma lista vazia
        self.itens = []

    def enfileirar(self, item):
        # Adiciona um item ao final da fila
        self.itens.append(item)
        # O primeiro a entrar, vai ser o último a sair

    def desenfileirar(self):
        # Remove e retorna o primeiro elemento da fila (posição 0)
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None
        # Caso a fila esteja vazia, retorna None

    def esta_vazia(self):
        # Retorna True se a fila estiver sem elementos, False caso contrário
        return len(self.itens) == 0

    def listar(self):
        # Retorna todos os elementos da fila na ordem em que foram inseridos
        return self.itens
        # Essa ordem é cronológica (FIFO)

class Pilha:
    def __init__(self):
        # Inicializa a pilha como uma lista vazia
        self.itens = []

    def empilhar(self, item):
        # Adiciona um item ao topo da pilha
        # o último elemento inserido será o primeiro a ser removido
        self.itens.append(item)

    def desempilhar(self):
        # Remove e retorna o último item da pilha (topo)
        if not self.esta_vazia():
            return self.itens.pop()
        return None
        # Caso a pilha esteja vazia, retorna None

    def esta_vazia(self):
        # Retorna True se a pilha não tiver elementos, False caso contrário
        return len(self.itens) == 0

    def listar(self):
        # Retorna todos os elementos da pilha na ordem em que estão armazenados
        return self.itens

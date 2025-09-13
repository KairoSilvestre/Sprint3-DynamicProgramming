def busca_sequencial(lista, chave, valor):
    for item in lista:
        if item[chave] == valor:
            return item
    return None

def busca_binaria(lista, valor, chave):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio][chave] == valor:
            return lista[meio]
        elif lista[meio][chave] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None

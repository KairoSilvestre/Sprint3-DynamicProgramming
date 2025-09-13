def merge_sort(lista, chave):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)

    return juntar(esquerda, direita, chave)

def juntar(esq, dir, chave):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i][chave] <= dir[j][chave]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

def quick_sort(lista, chave):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista)//2]
    menores = [x for x in lista if x[chave] < pivo[chave]]
    iguais = [x for x in lista if x[chave] == pivo[chave]]
    maiores = [x for x in lista if x[chave] > pivo[chave]]

    return quick_sort(menores, chave) + iguais + quick_sort(maiores, chave)

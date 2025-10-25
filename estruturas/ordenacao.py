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

def merge_sort_recursivo(lista, chave):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort_recursivo(lista[:meio], chave)
    direita = merge_sort_recursivo(lista[meio:], chave)
    return juntar(esquerda, direita, chave)

def merge_sort_memo(lista, chave, memo=None):
    if memo is None:
        memo = {}
    chave_cache = tuple(id(x) for x in lista)
    if chave_cache in memo:
        return memo[chave_cache]
    if len(lista) <= 1:
        memo[chave_cache] = lista
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort_memo(lista[:meio], chave, memo)
    direita = merge_sort_memo(lista[meio:], chave, memo)
    resultado = juntar(esquerda, direita, chave)
    memo[chave_cache] = resultado
    return resultado

def merge_sort_iterativo(lista, chave):
    n = len(lista)
    largura = 1
    while largura < n:
        for i in range(0, n, 2 * largura):
            meio = min(i + largura, n)
            fim = min(i + 2 * largura, n)
            esquerda = lista[i:meio]
            direita = lista[meio:fim]
            lista[i:fim] = juntar(esquerda, direita, chave)
        largura *= 2
    return lista

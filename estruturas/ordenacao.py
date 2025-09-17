def merge_sort(lista, chave):
    if len(lista) <= 1:
        return lista

    # Divide a lista em duas metades
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)  
    direita = merge_sort(lista[meio:], chave)  

    # Junta as duas metades já ordenadas
    return juntar(esquerda, direita, chave)

def juntar(esq, dir, chave):
    resultado = []
    i = j = 0

    # Percorre as duas listas comparando os elementos
    while i < len(esq) and j < len(dir):
        if esq[i][chave] <= dir[j][chave]:
            resultado.append(esq[i])  
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    # Adiciona os elementos restantes (se houver)
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

def quick_sort(lista, chave):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista)//2]

    # Cria três listas: menores, iguais e maiores em relação ao pivô
    menores = [x for x in lista if x[chave] < pivo[chave]]
    iguais = [x for x in lista if x[chave] == pivo[chave]]
    maiores = [x for x in lista if x[chave] > pivo[chave]]

    # Ordena recursivamente menores e maiores, e junta o resultado
    return quick_sort(menores, chave) + iguais + quick_sort(maiores, chave)

from dados import gerar_dados
from estruturas.pilha import Pilha
from estruturas.fila import Fila
from estruturas.ordenacao import merge_sort, quick_sort, merge_sort_recursivo, merge_sort_memo, merge_sort_iterativo

def imprimir_dados(titulo, lista):
    print("\n" + "="*50)
    print(f"{titulo}")
    print("="*50)
    for d in lista:
        validade = d["validade"].strftime("%d/%m/%Y") if hasattr(d["validade"], "strftime") else d["validade"]
        print(f"Insumo: {d['insumo']:<12} | Quantidade: {d['quantidade']:<3} | Validade: {validade}")

dados = gerar_dados(10)
imprimir_dados("Dados Simulados", dados)

fila = Fila()
pilha = Pilha()

for d in dados:
    fila.enfileirar(d)
    pilha.empilhar(d)

imprimir_dados("Fila (ordem de consumo)", fila.listar())
imprimir_dados("Pilha (últimos consumos primeiro)", pilha.listar())

def busca_sequencial(lista, chave, valor):
    for item in lista:
        if item[chave] == valor:
            return item
    return None

def busca_binaria(lista, chave, valor):
    lista_ordenada = quick_sort(lista, chave)
    esquerda = 0
    direita = len(lista_ordenada) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista_ordenada[meio][chave] == valor:
            return lista_ordenada[meio]
        elif lista_ordenada[meio][chave] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None

print("\n" + "="*50)
print("Busca sequencial por 'Reagente A':")
print(busca_sequencial(dados, "insumo", "Reagente A"))

print("\nBusca binária por 'Reagente A':")
print(busca_binaria(dados, "insumo", "Reagente A"))

dados_ordenados_quantidade = quick_sort(dados, "quantidade")
imprimir_dados("Ordenação por quantidade (QuickSort)", dados_ordenados_quantidade)

dados_ordenados_validade = merge_sort(dados, "validade")
imprimir_dados("Ordenação por validade (MergeSort)", dados_ordenados_validade)

dados_merge_rec = merge_sort_recursivo(dados, "quantidade")
dados_merge_memo = merge_sort_memo(dados, "quantidade")
dados_merge_iter = merge_sort_iterativo(dados.copy(), "quantidade")

print("\nVerificando se todas as versões produzem o mesmo resultado:")
print("Recursiva == Memoização:", dados_merge_rec == dados_merge_memo)
print("Recursiva == Iterativa:", dados_merge_rec == dados_merge_iter)

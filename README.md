# Integrantes
* [Kaique Zaffarani](https://github.com/Z4ffarani) | 556677

* [Guilerme Santos Nunes](https://github.com/sannunez) | 558989

* [Kairo da Silva Silvestre de Carvalho](https://github.com/Pedro-Josue) | 558288

* [Pedro Josué Pereira Almeida]() | 554913

# Dynamic Programming 
Esse projeto foi desenvolvido como parte da Sprint 3 da faculdade, com o objetivo de praticar conceitos de estruturas de dados e algoritmos de ordenação/busca em Python. 

O sistema simula o gerenciamento de insumos de laboratório, permitindo: 

* Gerar dados aleatórios (insumos, quantidade, validade)
* Armazenar dados em Fila e Pilha
* Ordenar por quantidade (QuickSort) e por validade (MergeSort)
* Pesquisar itens por Busca Sequencial e Busca Binária
## Como rodar o projeto
1. Clonar o repositório:
```bash
    git clone https://github.com/KairoSilvestre/Sprint3-DynamicProgramming.git
```
2. Navegar para a pasta do projeto: 
```bash
    cd Sprint3-DynamicProgramming
```
3. Executar projeto 
    py main.py 

## Funcionalidades 

### Geração de dados 

Arquivo: dados.py 
* Gera insumos aleatórios com nome, quantidade e validade. 
* Exemplo de saída:

```bash
{'insumo': 'Reagente B', 'quantidade': 15, 'validade': '2026-03-15'}
```

## 1. Fila (FIFO)
* A fila segue a regra FIFO, então o primeiro elemento que entrar, será o primeiro a sair. 
* Isso é importante para simular consumo em ordem cronológica, como insumos ou tarefas processadas em sequência.

### Exemplo: 

```
fila = Fila()

# Aqui, o elemento é inserido na fila
fila.enfileirar("Reagente A")
fila.enfileirar("Reagente B")
fila.enfileirar("Descartável X")

print("Fila atual:", fila.listar())

# Ele então é retirado o primeiro elemento da fila.
primeiro = fila.desenfileirar()
print("Item removido:", primeiro)
print("Fila após remoção:", fila.listar())
```

## 2. Pilha 

* A pilha segue a regra LIFO, ou seja, o último elemento que entrar, será o primeiro a sair. 

### Exemplo: 

```
pilha = Pilha()

# Inserindo elementos na pilha
pilha.empilhar("Reagente A")
pilha.empilhar("Reagente B")
pilha.empilhar("Descartável X")

print("Pilha atual:", pilha.listar())

# Retirando o último elemento
ultimo = pilha.desempilhar()
print("Item removido:", ultimo)
print("Pilha após remoção:", pilha.listar())
```

## 3. Merge Sort 
* É um algoritmo de oridenação eficiente baseado em divisão e conquista.
* Ele divide a lista em metades menores, ordena cada metade recursiva e depois junta os resultados.
* Muito usado quando precisamos de estabilidade (elementos iguais mantêm sua ordem original)

### Exemplo prático: 

Ordenar insumos pela validade (datas mais próximas na frente)

## 4. Quick Sort

* Também é baseado em divisão e conquista, mas escolhe um pivô e organiza os elementos em três grupos (Menores, iguais e maiores).
* Depois aplica recursivamente a ordenação nos grupos menores e maiores. 
* É geralmente mais rápido que Merge Sort em listas grandes por causa do baixo uso de memória.

## Exemplo prático:

* Ordenar insumos pela quantidade consumida.

## Dados (Simulação)

Os dados são gerados aleatóriamente para simular como funcionaria o sistema. 

### Funcionalidades: 
* Cria uma lista de insumos aleatórios com:
    * Nome(insumos)
    * Quantidade(quantidade)
    * Data de validade(validade)
Esses dados são usados para testar as estruturas (Fila, Pilha) e algoritmos (Busca, Ordenação).

### Atualizações da SPRINT 4 - Dynamic Programming

Durante a última etapa do projeto, foram realizadas atualizações específicas para atender aos novos requisitos relacionados à programação dinâmica e à validação de algoritmos.

### Arquivos Atualizados

## 1. estruturas/ordenacao.py

O que foi feito:
Foram adicionadas três novas implementações do algoritmo Merge Sort:
```
 1. merge_sort_recursivo: versão recursiva (top-down).

 2. merge_sort_memo: versão com memoização, utilizando cache para armazenar subsoluções.

 3. merge_sort_iterativo: versão iterativa (bottom-up), eliminando o uso de recursão.
```

Essas versões foram criadas para cumprir os requisitos de desenvolvimento de soluções recursiva, com memorização e iterativa, demonstrando o uso dos princípios da programação dinâmica — definição de estados, decisões, função de transição e função objetivo.

## 2. main.py

O arquivo principal foi atualizado para:
```
1. Importar as novas funções do módulo ordenacao.

2. Executar as três versões do Merge Sort.

3. Comparar os resultados entre as versões para garantir que todas retornam o mesmo resultado.
```
Essa atualização valida experimentalmente o requisito 3 do professor, garantindo que as diferentes abordagens do algoritmo produzem resultados idênticos e funcionam de forma consistente dentro do sistema de gestão de almoxarifado.

### Resultado das Alterações
O projeto agora contempla os três paradigmas da programação dinâmica (recursivo, memoizado e iterativo).

O código foi mantido modular e coeso, sem comprometer as funcionalidades anteriores.

Todos os requisitos exigidos foram atendidos de forma clara, comprovável e integrada ao contexto do problema.

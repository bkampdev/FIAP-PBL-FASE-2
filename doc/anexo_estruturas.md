
# Anexo — Estruturas de Dados e Algoritmos

## 1. Objetivo

Este documento apresenta as estruturas de dados e os algoritmos
utilizados no sistema de gerenciamento de pouso de módulos espaciais.

O objetivo é demonstrar como listas, filas, pilhas, buscas lineares
e ordenação Bubble Sort contribuem para o processamento e a
organização das informações durante a simulação.

## 2. Listas

As listas são estruturas que armazenam múltiplos elementos em uma
sequência e permitem acessar, adicionar e percorrer esses elementos.

No arquivo `main.py`, são utilizadas listas para armazenar os
módulos conforme sua situação:

```python
modulos_pousados = []
modulos_em_espera = []
modulos_em_alerta = []
modulos_definidos = []
condicoes_externas_ambiente = []
```

Cada lista possui uma finalidade específica:

- `modulos_pousados`: módulos autorizados a pousar.
- `modulos_em_espera`: módulos cujo pouso foi adiado.
- `modulos_em_alerta`: módulos bloqueados por falha total dos sensores.
- `modulos_definidos`: módulos gerados para a simulação.
- `condicoes_externas_ambiente`: condições ambientais geradas durante o processamento.

O método `append()` é utilizado para inserir novos elementos nas listas.

Exemplo:

```python
modulos_pousados.append(modulo_atual)
```

## 3. Fila FIFO

FIFO significa *First In, First Out*, ou seja, o primeiro elemento
a entrar é o primeiro a sair.

No sistema, a fila de pouso utiliza a estrutura `deque`, importada
da biblioteca `collections`.

```python
from collections import deque

modulos_fila_de_pouso = deque()
```

Os módulos são inseridos na fila com `append()`:

```python
modulos_fila_de_pouso.append(modulo)
```

Durante o processamento, o próximo módulo é retirado com `popleft()`:

```python
modulo_atual = modulos_fila_de_pouso.popleft()
```

### Exemplo

Considere a seguinte ordem de entrada:

1. Módulo A
2. Módulo B
3. Módulo C

A ordem de retirada será:

1. Módulo A
2. Módulo B
3. Módulo C

Essa estrutura permite processar os módulos na ordem em que foram
adicionados à fila.

## 4. Pilha LIFO

LIFO significa *Last In, First Out*, ou seja, o último elemento
a entrar é o primeiro a sair.

No sistema, o histórico de decisões é armazenado em uma lista:

```python
historico_de_decisoes = []
```

As decisões são adicionadas com `append()`:

```python
historico_de_decisoes.append(
    f"{modulo_atual.nome_modulo}: Autorizado"
)
```

Na exibição dos resultados, o método `pop()` remove o último
registro inserido:

```python
print(" -", historico_de_decisoes.pop())
```

### Exemplo

Considere as decisões registradas nesta ordem:

1. Módulo A: Autorizado
2. Módulo B: Adiado
3. Módulo C: Bloqueado

A ordem de exibição será:

1. Módulo C: Bloqueado
2. Módulo B: Adiado
3. Módulo A: Autorizado

Dessa forma, o histórico é apresentado da decisão mais recente
para a mais antiga.

Observação: como o método `pop()` remove os elementos, o histórico
fica vazio após sua exibição completa.

## 5. Busca Linear

A busca linear percorre os elementos de uma coleção, comparando
cada elemento com uma condição definida.

No arquivo `Consultas.py`, existem três funções que utilizam
esse princípio.

### 5.1. Módulo com menor combustível

A função `modulo_menor_combustivel()` percorre a lista e retorna
o módulo com o menor nível de combustível.

```python
if lista_de_modulos[i].nivel_combustivel < menor.nivel_combustivel:
    menor = lista_de_modulos[i]
```

### 5.2. Módulo com maior prioridade

A função `modulo_maior_prioridade()` identifica o módulo de maior
urgência.

No sistema, o número 1 representa uma prioridade maior do que
os números 2 ou 3.

```python
if lista_de_modulos[i].prioridade_pouso < maior.prioridade_pouso:
    maior = lista_de_modulos[i]
```

### 5.3. Busca por criticidade

A função `modulos_por_criticidade()` retorna todos os módulos
cuja criticidade de carga corresponde ao valor informado.

```python
if lista_de_modulos[i].criticidade_carga == criticidade:
    encontrados.append(lista_de_modulos[i])
```

As três buscas possuem complexidade de tempo O(n), pois podem
precisar percorrer todos os módulos da lista.

As funções de menor combustível e maior prioridade pressupõem
que a lista recebida não esteja vazia.

## 6. Ordenação Bubble Sort

O algoritmo Bubble Sort organiza os elementos por meio de
comparações entre posições vizinhas.

No arquivo `Consultas.py`, a função `ordena_fila()` utiliza esse
algoritmo para reorganizar os módulos conforme um critério.

O trecho responsável pelas trocas é:

```python
if valor_do_criterio(lista[j], criterio) > valor_do_criterio(lista[j + 1], criterio):
    lista[j], lista[j + 1] = lista[j + 1], lista[j]
```

Os critérios disponíveis são:

| Código | Critério |
|---|---|
| 1 | Prioridade de pouso |
| 2 | Nível de combustível |
| 3 | Massa |
| 4 | Horário estimado de chegada |

A função `valor_do_criterio()` utiliza `match/case` para selecionar
o atributo correspondente.

A ordenação é crescente, ou seja, os menores valores aparecem
primeiro.

### Exemplo de ordenação por prioridade

Antes da ordenação:

- Módulo A: prioridade 3
- Módulo B: prioridade 1
- Módulo C: prioridade 2

Depois da ordenação:

- Módulo B: prioridade 1
- Módulo C: prioridade 2
- Módulo A: prioridade 3

A função retorna uma nova estrutura `deque` com os módulos ordenados.

A implementação possui complexidade de tempo O(n²), devido aos
dois laços de repetição aninhados.

## 7. Validação Automatizada

Foram desenvolvidos testes automatizados com a biblioteca
`unittest` para verificar o funcionamento das estruturas
e dos algoritmos.

Os testes contemplam:

- Ordem de processamento da fila FIFO.
- Ordem de exibição do histórico LIFO.
- Busca do módulo com menor combustível.
- Busca do módulo com maior prioridade.
- Busca de módulos por criticidade.
- Ordenação por prioridade.
- Ordenação por combustível.
- Ordenação por massa.
- Ordenação por horário de chegada.
- Tratamento de critério de ordenação inválido.

Também foram realizados testes das decisões de pouso considerando
falhas nos sensores, limites de combustível e condições ambientais.

Na execução conjunta, os 15 testes automatizados passaram.

## 8. Observações sobre a integração

As funções de busca e ordenação estão implementadas no arquivo
`Consultas.py` e foram validadas individualmente.

Entretanto, na versão analisada do `main.py`, essas funções ainda
não são chamadas durante a execução principal da simulação.

Assim, os testes comprovam seu funcionamento isolado, mas não
demonstram sua integração ao fluxo principal.

## 9. Conclusão

O projeto utiliza estruturas de dados adequadas para organizar
os módulos e registrar as decisões da simulação.

As listas classificam os módulos conforme seus resultados,
a fila FIFO organiza a sequência de processamento e a pilha
LIFO permite exibir as decisões mais recentes primeiro.

As buscas lineares permitem localizar módulos por atributos
específicos, enquanto o Bubble Sort oferece diferentes
critérios de ordenação.

Os testes automatizados confirmaram o funcionamento dos
comportamentos avaliados, preservando a implementação
original do projeto.

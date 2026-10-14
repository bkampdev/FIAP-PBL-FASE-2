
# Relatório de Validação — Issue #2

## 1. Objetivo

Este relatório documenta a validação das estruturas de dados,
dos algoritmos de consulta e das regras de decisão utilizadas
no sistema de gerenciamento de pousos de módulos espaciais.

A validação foi realizada por meio de testes automatizados
em Python, utilizando a biblioteca unittest.

O trabalho teve como objetivo verificar o comportamento da
implementação existente, preservando o código desenvolvido
originalmente pela equipe.

## 2. Arquivos analisados

- main.py — processamento da fila e decisões de pouso.
- Modulos.py — definição das estruturas de dados.
- Dados.py — geração dos dados da simulação.
- Consultas.py — buscas lineares e ordenação Bubble Sort.

## 3. Arquivos de testes

Os testes automatizados estão organizados em:

- tests/test_decisoes.py
- tests/test_estruturas.py
- tests/test_consultas.py

## 4. Cenários validados

### 4.1. Regras de decisão

| Cenário | Resultado esperado | Status |
|---|---|---|
| Falha total dos sensores | Bloqueio do pouso | Aprovado |
| Combustível abaixo de 10 | Pouso de emergência | Aprovado |
| Combustível igual a 10 ou 11 | Sem emergência por combustível | Aprovado |
| Atmosfera instável | Pouso adiado | Aprovado |
| Área ocupada | Pouso adiado | Aprovado |

Os testes utilizaram dados controlados para evitar que
a geração aleatória interferisse nos resultados.

### 4.2. Estruturas de dados

| Estrutura | Comportamento validado | Status |
|---|---|---|
| Fila FIFO | Primeiro módulo inserido é processado primeiro | Aprovado |
| Pilha LIFO | Última decisão registrada é exibida primeiro | Aprovado |

### 4.3. Buscas e ordenação

| Cenário | Resultado esperado | Status |
|---|---|---|
| Menor combustível | Retornar o módulo com menor nível | Aprovado |
| Maior prioridade | Retornar o módulo com menor número de prioridade | Aprovado |
| Busca por criticidade | Retornar os módulos correspondentes | Aprovado |
| Ordenação por prioridade | Ordem crescente de prioridade | Aprovado |
| Ordenação por combustível | Ordem crescente de combustível | Aprovado |
| Ordenação por massa | Ordem crescente de massa | Aprovado |
| Ordenação por chegada | Ordem cronológica crescente | Aprovado |
| Critério inválido | Lançar ValueError | Aprovado |

## 5. Execução dos testes

Os testes foram executados no terminal, a partir
da pasta principal do projeto, utilizando:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

Resultado registrado:

```text
Ran 15 tests

OK
```

Total de testes executados: 15.

Total de testes aprovados: 15.

Falhas identificadas nessa execução: 0.

## 6. Pontos de atenção

### 6.1. Integração das consultas

As funções de busca e ordenação presentes no arquivo
Consultas.py foram testadas isoladamente.

Na versão analisada, o arquivo main.py importa o módulo
Consultas, mas não executa suas funções durante a simulação.

Portanto, a integração dessas funcionalidades ao fluxo
principal ainda não foi demonstrada.

### 6.2. Listas vazias

As funções modulo_menor_combustivel() e
modulo_maior_prioridade() acessam o primeiro elemento
da lista recebida.

Caso recebam uma lista vazia, ocorre IndexError.

Essa condição não foi tratada na implementação analisada.

### 6.3. Histórico de decisões

A função exibe_resultado() utiliza pop() para apresentar
as decisões da mais recente para a mais antiga.

Como pop() remove os elementos da lista, o histórico
fica vazio após a exibição.

Esse comportamento foi observado na análise do código.

### 6.4. Cobertura dos testes

Os testes verificam os cenários descritos neste relatório,
mas não representam cobertura integral de todas as
combinações possíveis de entradas.

O resultado OK indica que os cenários testados passaram,
não que o programa esteja livre de qualquer defeito.

## 7. Conclusão

A execução dos 15 testes automatizados apresentou
resultado satisfatório, sem falhas nos cenários avaliados.

Foram validadas as regras de decisão de pouso, o
comportamento FIFO e LIFO, as buscas lineares e os
quatro critérios de ordenação Bubble Sort.

Os pontos de atenção identificados foram documentados
para conhecimento da equipe, sem alterar a lógica
original do sistema.

A documentação das estruturas e dos algoritmos está
disponível no arquivo doc/anexo_estruturas.md.

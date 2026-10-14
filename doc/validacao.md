
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

Na versão original analisada, main.py não executa as funções de
Consultas.py durante a simulação.

Portanto, a integração dessas funcionalidades ao fluxo
principal ainda não foi demonstrada.

### 6.2. Listas vazias

As funções modulo_menor_combustivel() e
modulo_maior_prioridade() acessam o primeiro elemento
da lista recebida.

Caso recebam uma lista vazia, ocorre IndexError.

Essa condição não foi tratada na implementação analisada.

Na integração da issue #5, ambas passaram a retornar `None` para entrada vazia.

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

## 8. Validação adicional da integração - issue #5

Autoria dos testes e do relatório original: Davi Coninck Cassaro, PR #8.
A integração acrescentou as verificações abaixo. O registro do executor e
dos comandos está no checklist de entrega.

- `main.py`: execução protegida por `if __name__ == "__main__"`; inicialização
  reutilizável e entrada opcional de ambientes fixos. As regras de decisão são preservadas.
- `Consultas.py`: buscas vazias retornam `None`; critério inválido é rejeitado
  mesmo quando não há pares para comparar.
- `exemplos/exemplo_deterministico.py`: buscas, quatro ordenações, fila por
  prioridade, decisões e consumo LIFO do histórico, todos com os mesmos registros.
- `tests/test_integracao.py`: seis testes adicionais, incluindo 135 combinações
  para equivalência com o diagrama, empate estável e entrada vazia.

Comandos executados em 13/10/2026, Python 3.14.7:

```sh
python3 -m unittest discover -s tests -v
python3 -m exemplos.exemplo_deterministico
python3 main.py
```

Resultado: 21 testes aprovados, zero falhas; exemplo com três pousados, dois
adiados e um bloqueado. Energia é autorizada por emergência mesmo com tempestade
e área ocupada; Saúde é bloqueada por falha total mesmo com combustível baixo.
Essa precedência é uma limitação didática, não uma garantia de segurança física.

Os 15 cenários de teste de Davi foram preservados; as massas fixas foram alinhadas para 10/15/20 toneladas, sem alterar a ordem esperada ou os critérios testados. Foram reproduzidos antes da correção
o `IndexError` nas buscas vazias e a aceitação indevida do critério 99 em filas
com zero ou um elemento; os testes adicionais falharam antes e passaram depois.
A simulação aleatória continua usando a faixa 0–100% de combustível.

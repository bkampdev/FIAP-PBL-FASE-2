# MGPEB - Missão Aurora Siger

Trabalho da Atividade Integradora da Fase 2 da FIAP, desenvolvido pelo Grupo 2.
O programa organiza os módulos que aguardam pouso, consulta seus atributos e
avalia cada tentativa conforme combustível, sensores, atmosfera e área disponível.
O relatório apresenta as regras, o modelo de consumo de combustível, as escolhas
de programação e a discussão sobre ESG e governança da base.

## Entrega

- [Relatório técnico em PDF, com anexo integrado](doc/relatorio_mgpeb.pdf)
- [Versão textual editável](doc/pdf.md)
- [Anexo completo de estruturas de Davi](doc/anexo_estruturas.md)
- [Validação original e complemento de integração](doc/validacao.md)
- [Checklist, matriz de requisitos e instruções do portal](doc/checklist_entrega.md)
- [Gerador do PDF e das figuras](scripts/gerar_pdf.py)

Repositório: [bkampdev/FIAP-PBL-FASE-2](https://github.com/bkampdev/FIAP-PBL-FASE-2).
A atividade está no **Grupo 2**, com os cinco participantes confirmados no FIAP ON
em 13/10/2026. PDF e arquivos no GitHub não significam envio ao portal.

## Execução

Requer **Python 3.10 ou superior** por causa de `match/case`. Não é necessário
instalar dependências para executar a simulação, o exemplo ou os testes.
Na raiz do repositório:

```sh
python3 main.py
python3 -m exemplos.exemplo_deterministico
python3 -m unittest discover -s tests -v
```

No Windows, use `python` no lugar de `python3` se esse for o comando disponível.
`main.py` gera seis módulos aleatórios; tipos podem se repetir. O exemplo fixo
cadastra um registro de cada tipo, chama as três buscas e as quatro ordenações,
aplica a fila por prioridade e executa o mesmo processamento de pouso.

Resultado fixo esperado:

| Evidência | Resultado |
|---|---|
| Menor combustível e maior prioridade | Saúde |
| Criticidade Alta | Saúde, Energia, Segurança |
| Fila aplicada por prioridade | Saúde, Energia, Comunicação, Suprimentos, Transporte, Segurança |
| Pousados | Energia (emergência), Comunicação, Suprimentos |
| Em espera | Transporte, Segurança |
| Em alerta | Saúde |
| Pilha exibida com pop | Segurança, Transporte, Suprimentos, Comunicação, Energia, Saúde |
| Fila e pilha ao final | Vazias |

A suíte contém os 15 testes de Davi e seis de integração: **21 testes**.
Um dos testes compara as regras do programa com o circuito em 135 combinações.

## Regras e limites didáticos

- Combustível gerado: 0–100%; emergência estritamente abaixo de 10%.
- Falha total dos sensores bloqueia antes de avaliar emergência.
- Emergência autoriza sem conferir atmosfera/área; é uma limitação do modelo.
- Sem emergência, atmosfera diferente de Estável ou área diferente de Livre adia.
- Falha parcial não é bloqueio automático; não comprova segurança de uma nave real.
- Prioridade vai de 1 a 5; menor número é mais urgente. A fila continua FIFO
  depois de uma ordenação explícita. Emergência não muda a ordem da fila.
- Massa: 10–20 toneladas. Data fixa: 12/10/2026, chegadas de 06:00 a 17:59.
- O modelo `C(t)=C0-k*t`, com `k=5` pontos percentuais/hora e reserva de 10%,
  está no relatório; o código não calcula tempo limite nem atualiza combustível.
- Buscas vazias retornam `None`/`[]`; empates na ordenação mantêm a ordem de entrada.
- O histórico em memória tem nome e decisão; a exibição consome a pilha.
  Não há banco de auditoria, desvio para área alternativa, reentrada automática,
  medição de hardware nem tolerância à radiação implementada.

## Regenerar o relatório

As dependências abaixo são usadas apenas nos artefatos de documentação:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
python scripts/gerar_pdf.py
python scripts/verificar_pdf.py
```

No Windows, ative com `.venv\Scripts\activate`.
O gerador lê `doc/pdf.md`, cria duas figuras em PNG/SVG e o PDF com oito páginas.
O verificador renderiza todas as páginas para inspeção; uma análise automática
não substitui a conferência visual.

## Equipe - Grupo 2

| Integrante | RM | GitHub | Contribuição |
|---|---|---|---|
| Lorenzo Mendes Rocha | RM575361 | @Rocha0306 | Base e etapas 1–4, PR #1 |
| Davi Coninck Cassaro | RM572772 | @daviconinck | Testes, validação e anexo, PR #8 |
| Eduardo Backes Klauck | RM575889 | @BackesEdu | Evolução computacional, PR #6 |
| Gabriel Gonzales | RM574746 | @ItsTheContext | ESG e governança, PR #7 |
| Guilherme Cardoso Bremenkamp | RM574229 | @bkampdev | Integração, correções, exemplo fixo e pacote |

Nomes e RMs recuperados do [README do PBL 1](https://github.com/bkampdev/FIAP-PBL-FASE-1/blob/main/README.md).
Os cinco nomes foram conferidos na atividade atual; o Grupo 16 do PBL 1 não foi
reutilizado como identificação do PBL 2. As contribuições e a conferência da integração estão registradas no checklist.

## Requisitos atuais do FIAP ON

Conferidos diretamente na [atividade MGPEB](https://on.fiap.com.br/mod/assign/view.php?id=616789)
em 13/10/2026: PDF de 5–10 páginas, código `.py` organizado/comentado/executável
com exemplos simples e anexo concreto de listas/filas/pilhas, que pode integrar
o relatório. Prazo: **14/10/2026 às 23h59**, horário de São Paulo. Avaliação: 15 pontos.

O formulário é de **envio de arquivos**, até 20 anexos, limite informado de
256 MB por arquivo; não apresentou campo para link ou texto. É necessário
anexar os entregáveis, salvar e conferir o estado posterior. O link público no
PDF ajuda a rastreabilidade, mas não substitui o envio do código pedido.
Em 13/10/2026, a atividade ainda estava com **Entrega pendente**. A conferência
do formulário foi feita sem enviar arquivos.

Para a entrega, anexar o PDF e os arquivos `main.py`, `Dados.py`, `Modulos.py`,
`Consultas.py` e `exemplos/exemplo_deterministico.py`. O anexo de estruturas
já está incluído no relatório. O README também pode acompanhar os arquivos.
Se os cinco arquivos Python forem baixados para uma mesma pasta, o exemplo
pode ser executado com `python3 exemplo_deterministico.py`. No repositório,
a execução segue o comando com `-m` indicado acima.

## Arquivos

`main.py`, `Dados.py`, `Modulos.py` e `Consultas.py` preservam o núcleo de Lorenzo.
`exemplos/` contém a demonstração fixa; `tests/`, os testes.
`doc/etapa_5_computacao.md` e `doc/etapa_6_esg_governanca.md` preservam as seções
de Eduardo e Gabriel com correções identificadas. `doc/pdf.md` é o texto consolidado.

Licença: [MIT](LICENSE).

# Checklist de integração e entrega - issue #5

Conferência em 13/10/2026, horário de São Paulo. Este arquivo comprova a
preparação técnica descrita; **não comprova envio ao FIAP ON**.

## Origem e versão

- Base: `main`, commit `dff41369ca8a907f3d904680da8f5cd0d15f1a1f`.
- Lorenzo: PR #1, base das etapas 1–4, commit `8d440757`.
- Eduardo: PR #6; Gabriel: PR #7; Davi: PR #8, todos integrados à base.
- Branch: `feat/issue-5-integracao-entrega`.
- A versão final validada e seu SHA completo são registrados na descrição do
  PR da issue #5; `git rev-parse HEAD` identifica a versão local após o commit.
- Nomes/RMs conferidos no README público do PBL 1 e nomes confirmados no Grupo 2.

## Matriz requisito → evidência

| Requisito (Capítulo 1, pp. 14–17; portal atual) | Arquivo/evidência |
|---|---|
| Etapa 1: tipos, atributos, fila e listas auxiliares | `Modulos.py`, `Dados.py`, `main.py`; relatório p. 2 |
| Etapa 2: AND/OR/NOT e decisões | `doc/image.png`, `doc/image.svg`; relatório p. 3; teste com 135 combinações |
| Etapa 3: Python simples, busca e ordenação executadas | `Consultas.py`, `main.py`, `exemplos/exemplo_deterministico.py`; relatório p. 4 |
| Etapa 4: função, parâmetros/unidades, gráfico e decisão | `doc/image-1.png`, `doc/image-1.svg`; relatório p. 5; 2/8/16 h |
| Etapa 5: computação e restrições embarcadas | `doc/etapa_5_computacao.md`; relatório p. 6 |
| Etapa 6: ESG, governança, riscos e transparência | `doc/etapa_6_esg_governanca.md`, `doc/matriz_riscos_governanca.md`; relatório p. 7 |
| PDF de 5–10 páginas | `doc/relatorio_mgpeb.pdf`: 8 páginas; todas renderizadas e abertas |
| Código .py organizado/comentado/executável | Quatro módulos do núcleo e exemplo fixo; execução com Python 3.14.7 |
| Anexo concreto de lista/fila/pilha | Relatório p. 8; `doc/anexo_estruturas.md`, mesmos registros do exemplo |
| Reprodução e equipe com RM | `README.md` e capa do relatório |
| Fontes dos artefatos | `scripts/gerar_pdf.py`, `requirements-docs.txt` |

## Conferência técnica

- [x] Conteúdo útil e autoria das etapas 1–4 preservados; contribuições separadas identificadas.
- [x] Correções feitas localmente com autorização, sem cobrar alterações dos autores.
- [x] Python básico; biblioteca padrão no núcleo, exemplo e testes.
- [x] Buscas e quatro ordenações efetivamente chamadas no exemplo fixo.
- [x] Faixa 0–100%; emergência <10%; falha total precede emergência.
- [x] Falha parcial, ambientes adversos, fronteiras, FIFO, LIFO, vazios e empates conferidos.
- [x] Diagrama AND/OR/NOT corresponde às expressões e ao código.
- [x] Modelo linear preservado; consumo em pontos percentuais/hora; 2/8/16 h conferidos.
- [x] Propostas de prioridade pelo tempo limite, auditoria e governança identificadas como propostas.
- [x] PDF com 8 páginas; imagens, tabelas, fórmulas, margens e links conferidos visualmente.
- [x] README, capa e dados da equipe alinhados com o PBL 1 e Grupo 2 atual.
- [x] Validação técnica da integração registrada com executor e comandos.
- [ ] Aceite/merge do PR: etapa posterior à abertura do PR solicitado.

Comandos:

```sh
python3 -m unittest discover -s tests -v
python3 -m exemplos.exemplo_deterministico
python3 main.py
.venv/bin/python scripts/gerar_pdf.py
.venv/bin/python scripts/verificar_pdf.py
```

Resultado: 21 testes aprovados; exemplo com 3 pousados, 2 adiados e 1 bloqueado;
histórico desempilhado em LIFO e consumido. As 135 combinações são subcasos de
um dos 21 testes. PDF com 8 páginas, quatro links de referência e link do
repositório na capa. A revisão desta integração foi executada por Guilherme com apoio do Codex.
Não foi registrada nova aprovação dos demais integrantes.

## Requisitos verificados no FIAP ON

Página: https://on.fiap.com.br/mod/assign/view.php?id=616789

- [x] Enunciado atual conferido; mesmas seis etapas do capítulo.
- [x] Entregáveis: PDF de 5–10 páginas, código `.py` e anexo, integrado ou separado.
- [x] Prazo oficial: quarta-feira, **14/10/2026 às 23h59**, America/Sao_Paulo.
- [x] Avaliação exibida: 15 pontos; grupo com mínimo 1 e máximo 5 participantes.
- [x] Grupo atual: **Grupo 2**; Eduardo Backes Klauck, Guilherme Cardoso Bremenkamp,
  Davi Coninck Cassaro, Gabriel Gonzales e Lorenzo Mendes Rocha presentes.
- [x] Formulário aberto para leitura: somente arquivos, até 20 anexos e 256 MB
  por arquivo. Nenhum campo de link/texto foi apresentado.
- [x] Conferência encerrada por Cancelar, sem anexar ou salvar arquivos.
- [ ] Anexar e confirmar a entrega acadêmica.
- [ ] Reabrir o portal, confirmar estado de envio e data/hora.
- [ ] Guardar eventual comprovante de forma privada.

**Estado observado: Entrega pendente; Avaliação pendente; Última modificação: "-".**
A issue #5 permanece referenciada, sem fechamento automático por este PR,
pois inclui submissão e confirmação acadêmica que ainda não ocorreram.

## Organização para a submissão

O PBL 1 reuniu PDF, código/notebook, README, fontes dos artefatos e checklist.
Sua página no portal foi reaberta nesta conferência e mostrou envio para
avaliação, avaliação concluída e `relatorio-pre-decolagem.pdf` anexado.
Essa organização foi reaproveitada, com os requisitos atuais da Fase 2:
o portal agora pede `.py` e não exige notebook `.ipynb`.

Anexar o PDF e os cinco arquivos Python: `main.py`, `Dados.py`, `Modulos.py`,
`Consultas.py` e `exemplos/exemplo_deterministico.py`. O anexo de estruturas
já faz parte do PDF e permanece disponível em Markdown no repositório.
O README pode acompanhar os anexos com as instruções de execução.

Se os cinco arquivos Python forem baixados para uma mesma pasta, executar
`python3 main.py` e `python3 exemplo_deterministico.py`. Na organização do
repositório, o exemplo é executado com `python3 -m exemplos.exemplo_deterministico`.

Após anexar os arquivos corretos, usar o fluxo exibido pelo portal e conferir
o estado posterior. Não presumir confirmação definitiva apenas pelo botão
Salvar mudanças ou por um upload iniciado. Não publicar capturas de login,
comprovantes privados, e-mails dos participantes ou o material didático exclusivo.

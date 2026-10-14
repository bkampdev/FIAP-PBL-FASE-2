Texto elaborado por Gabriel Gonzales. Contribuição registrada no PR #7 e revisada na integração do relatório.

# Relatório Técnico: Dimensões Operacionais, Governança, Riscos e Transparência
**Projeto:** Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB) — Missão Aurora Siger

---

## 1. Dimensão Ambiental no Cenário da Missão
* **Critérios para área de pouso:** *(Hipótese)* A seleção das zonas de pouso prioriza superfícies com estabilidade geotécnica comprovada e distantes de feições geomorfológicas sensíveis ou de alto valor científico. *(Recomendação)* Estabelecer zonas de exclusão (*buffer zones*) ao redor de depósitos de gelo subterrâneo e formações minerais virgens para mitigar a compactação excessiva do solo e a contaminação por poeira gerada pelos retrofoguetes.
* **Uso de combustível e energia:** *(Recomendação)* O planejamento das manobras em órbita deve otimizar o tempo de espera para evitar o esgotamento prematuro das reservas técnicas, priorizando perfis balísticos eficientes e o alinhamento com a matriz energética da base.
* **Gestão de resíduos:** *(Recomendação)* Garantir a contenção rigorosa de descartes operacionais e materiais de consumo (como embalagens de carga e detritos metálicos), evitando o espalhamento de resíduos no ambiente marciano.
* **Uso responsável de recursos locais:** *(Hipótese)* Eventuais utilizações de recursos *in-situ* (como regolito ou gelo) devem ser estritamente monitoradas para preservar regiões de interesse científico e limitar alterações ambientais e garantir a sustentabilidade a longo prazo da colônia.

---

## 2. Dimensão Social
* **Segurança e proteção:** *[Diretriz proposta]* Priorizar a integridade física de operadores, equipes de solo e futuras comunidades humanas. A regra didática de emergência ainda ignora atmosfera e área; portanto, não implementa essa garantia.
* **Necessidades fundamentais da base:** Assegurar o suprimento contínuo de suporte vital, energia e infraestrutura essencial antes de autorizar o processamento de cargas secundárias.
* **Hierarquia de cargas essenciais:** *[Proposta]* Definição de critérios de prioridade onde módulos críticos — como o **Módulo de Saúde** e o **Módulo de Energia** — poderiam receber prioridade elevada na fila de processamento e pouso em relação a cargas de menor urgência.
* **Participação social:** Incorporação de instâncias consultivas e canais de feedback para que os colonos e operadores afetados pelas regras de tráfego espacial possam opinar sobre limites operacionais e janelas de pouso.

---

## 3. Estrutura de Governança
* **Proposição e revisão de critérios:** *[Proposta]* Um comitê técnico-operacional multidisciplinar seria responsável por propor, auditar e atualizar as regras lógicas e os limiares de segurança do MGPEB.
* **Decisão de exceções:** Definição clara de responsabilidades para a decisão de exceções por um operador para situações imprevistas que fujam do escopo nominal das regras lógicas.
* **Documentação de justificativas e alterações:** *[Proposta]* Registro persistente das decisões tomadas pelo sistema, armazenando o estado dos módulos, carimbos de tempo (*timestamp*) e as condições ambientais vigentes no momento da tentativa de pouso.
* **Supervisão humana (Human-in-the-loop):** *[Proposta]* O sistema deveria operar sob supervisão, com confirmação humana para casos de exceção, falhas críticas de sensores ou ativações de protocolos de emergência.

---

## 4. Análise de Casos Concretos do Protótipo
* **Emergência por combustível:** 
  * *Risco:* Esgotamento do propulsor abaixo da reserva mínima de segurança durante o tempo de espera em órbita.
  * *Limite da simulação:* O modelo adota uma taxa de consumo linear simplificada ($k = 5$ pontos percentuais por hora), sem simular variações térmicas complexas, perturbações atmosféricas dinâmicas ou manobras multi-eixo avançadas.
* **Área de pouso indisponível:** 
  * *Risco:* Impossibilidade de pouso na coordenada primária devido a obstruções físicas ou ocupação simultânea da pista.
  * *Limite da simulação:* A simulação atual trata a disponibilidade da área por três categorias estáticas (Livre, Ocupada, Obstruída), sem modelar dinâmicas complexas de redirecionamento simultâneo para múltiplas pistas alternativas.
* **Falha parcial ou total de sensores:** 
  * *Risco:* Tomada de decisão automatizada baseada em telemetria corrompida ou perda total da percepção de altitude e velocidade.
  * *Limite da simulação:* As falhas de sensores são representadas de forma categórica (*Operacional*, *Falha parcial*, *Falha total*), desconsiderando ruídos estocásticos de leitura e degradação gradual por radiação.
* **Desempilhamento do histórico:** 
  * *Risco:* Perda dos registros após a exibição, pois pop() consome a pilha.
  * *Limite da simulação:* O uso de uma pilha (*stack*) em Python processa os dados de forma sequencial controlada, sem concorrer com fluxos de rede distribuídos reais.

---

## 5. Matriz de Riscos Operacionais

| Risco | Consequência | Mitigação Proposta (ou Implementada) | Responsável | Evidência Verificável | Limitação Restante |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Esgotamento de Energia / Combustível** | Perda de margem de combustível para manobras ou descida | *[Implementado]* Autorização de emergência se combustível <10% e sem falha total dos sensores | Sistema Automático / Operador de Voo | Logs de execução da fila e histórico de decisões | Consumo é análise matemática separada; código usa combustível estático e ignora ambiente na emergência |
| **Indisponibilidade da Área de Pouso** | Risco de colisão ou atraso prolongado em órbita | *[Implementado]* Adiamento sem emergência; *[Proposta]* avaliação de área alternativa | Equipe de Navegação Orbital | Parâmetros de disponibilidade da área nos registros | Falta de roteamento dinâmico complexo no código atual |
| **Falha Total de Sensores** | Descida às cegas sem referência de altitude | *[Implementado]* Bloqueio automático de pouso baseado na porta lógica de integridade | Sistema de Controle de Voo | Registro de módulos mantidos em estado de alerta | Ausência de simulação de redundância física de hardware |

---

## 6. Transparência e Rastreabilidade
* **Modelo de Transparência:** *[Proposta]* A auditoria poderia registrar quatro informações. O histórico atual só guarda nome e decisão:
  1. `[Entradas (Inputs)]`: Estado bruto do módulo e condições ambientais coletadas no momento da tentativa.
  2. `[Regra Aplicada]`: Expressão booleana ou condicional correspondente (ex: verificação de falha de sensores ou nível de combustível).
  3. `[Decisão Tomada]`: O veredito computacional gerado (*Autorizado*, *Adiado*, *Bloqueado* ou *Autorizado por emergência*).
  4. `[Motivo / Justificativa]`: O parâmetro crítico que motivou a bifurcação no fluxo lógico.
* **Alinhamento com o Código Final:** *Atenção ao escopo:* O protótipo desenvolvido utiliza estruturas lineares em memória (como listas, filas `deque` e pilhas para o histórico). Portanto, **não se deve afirmar** que o sistema possui auditoria persistente em banco de dados externo, desvio automatizado avançado para área alternativa em tempo real ou filas de emergência distribuídas, visto que esses recursos extrapolam o código final implementado nesta fase.

---

## 7. Revisão Independente e Coerência do Projeto
* **Revisão do Anexo:** Proposta de validação cruzada da consistência entre a modelagem matemática do consumo de combustível ($C(t) = C_0 - 5t$), os limiares de tempo limite ($t_{limite}$) e os dados tabulados, assegurando ausência de contradições técnicas.
* **Compilação e Coerência do Documento (Guilherme):** Conferência final da formatação, padronização visual dos diagramas lógicos e gráficos, clareza da nomenclatura dos módulos e coesão global do texto antes da entrega unificada da equipe.

## 8. Conferência da integração

A conferência da integração comparou o texto com o exemplo fixo e os testes. O exemplo fixo mostra Energia (9%, falha parcial, tempestade e área ocupada) autorizada por emergência, Saúde (5%, falha total) bloqueada, Comunicação (10%, falha parcial) autorizada, Transporte adiado por ventos e Segurança adiada por área ocupada. Esses casos estão em tests/test_integracao.py. Nenhuma emergência fura a fila nem desvia para área alternativa.

Transparência por entradas, regra, decisão e motivo é proposta de auditoria. O histórico implementado contém apenas nome e decisão e é apagado da pilha pela exibição; a cópia do exemplo é transitória.

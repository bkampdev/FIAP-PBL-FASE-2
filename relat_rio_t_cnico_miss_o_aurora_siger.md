# Relatório Técnico: Dimensões Operacionais, Governança, Riscos e Transparência
**Projeto:** Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB) — Missão Aurora Siger

---

## 1. Dimensão Ambiental no Cenário da Missão
* **Critérios para área de pouso:** *(Hipótese)* A seleção das zonas de pouso prioriza superfícies com estabilidade geotécnica comprovada e distantes de feições geomorfológicas sensíveis ou de alto valor científico. *(Recomendação)* Estabelecer zonas de exclusão (*buffer zones*) ao redor de depósitos de gelo subterrâneo e formações minerais virgens para mitigar a compactação excessiva do solo e a contaminação por poeira gerada pelos retrofoguetes.
* **Uso de combustível e energia:** *(Recomendação)* O planejamento das manobras em órbita deve otimizar o tempo de espera para evitar o esgotamento prematuro das reservas técnicas, priorizando perfis balísticos eficientes e o alinhamento com a matriz energética da base.
* **Gestão de resíduos:** *(Recomendação)* Garantir a contenção rigorosa de descartes operacionais e materiais de consumo (como embalagens de carga e detritos metálicos), evitando o espalhamento de resíduos no ambiente marciano.
* **Uso responsável de recursos locais:** *(Hipótese)* Eventuais utilizações de recursos *in-situ* (como regolito ou gelo) devem ser estritamente monitoradas para evitar desequilíbrios locais no ecossistema e garantir a sustentabilidade a longo prazo da colônia.

---

## 2. Dimensão Social
* **Segurança e proteção:** A integridade física de operadores, equipes de solo e futuras comunidades humanas constitui o limite inegociável e a prioridade máxima em todas as tomadas de decisão autônomas do MGPEB.
* **Necessidades fundamentais da base:** Assegurar o suprimento contínuo de suporte vital, energia e infraestrutura essencial antes de autorizar o processamento de cargas secundárias.
* **Hierarquia de cargas essenciais:** Implementação de uma taxonomia estrita onde módulos críticos — como o **Módulo de Saúde** e o **Módulo de Energia** — ocupam prioridade máxima na fila de processamento e pouso em relação a cargas de menor urgência.
* **Participação social:** Incorporação de instâncias consultivas e canais de feedback para que os colonos e operadores afetados pelas regras de tráfego espacial possam opinar sobre limites operacionais e janelas de pouso.

---

## 3. Estrutura de Governança
* **Proposição e revisão de critérios:** Um comitê técnico-operacional multidisciplinar é responsável por propor, auditar e atualizar as regras lógicas e os limiares de segurança do MGPEB.
* **Decisão de exceções:** Definição clara de alçadas de comando (como o *override* manual por um operador sênior) para situações imprevistas que fujam do escopo nominal das regras lógicas.
* **Documentação de justificativas e alterações:** Registro imutável de todas as decisões tomadas pelo sistema, armazenando o estado dos módulos, carimbos de tempo (*timestamp*) e as condições ambientais vigentes no momento da tentativa de pouso.
* **Supervisão humana (Human-in-the-loop):** O sistema opera sob vigilância contínua, exigindo confirmação humana mandatória para casos de exceção, falhas críticas de sensores ou ativações de protocolos de emergência.

---

## 4. Análise de Casos Concretos do Protótipo
* **Emergência por combustível:** 
  * *Risco:* Esgotamento do propulsor abaixo da reserva mínima de segurança durante o tempo de espera em órbita.
  * *Limite da simulação:* O modelo adota uma taxa de consumo linear simplificada ($k = 5 \%/h$), sem simular variações térmicas complexas, perturbações atmosféricas dinâmicas ou manobras multi-eixo avançadas.
* **Área de pouso indisponível:** 
  * *Risco:* Impossibilidade de pouso na coordenada primária devido a obstruções físicas ou ocupação simultânea da pista.
  * *Limite da simulação:* A simulação atual trata a disponibilidade da área de forma binária ou estática, sem modelar dinâmicas complexas de redirecionamento simultâneo para múltiplas pistas alternativas.
* **Falha parcial ou total de sensores:** 
  * *Risco:* Tomada de decisão automatizada baseada em telemetria corrompida ou perda total da percepção de altitude e velocidade.
  * *Limite da simulação:* As falhas de sensores são representadas de forma categórica (*Operacional*, *Falha parcial*, *Falha total*), desconsiderando ruídos estocásticos de leitura e degradação gradual por radiação.
* **Desempilhamento do histórico:** 
  * *Risco:* Conflito na ordem de recuperação dos registros de eventos passados durante auditorias de estado.
  * *Limite da simulação:* O uso de uma pilha (*stack*) em Python processa os dados de forma sequencial controlada, sem concorrer com fluxos de rede distribuídos reais.

---

## 5. Matriz de Riscos Operacionais

| Risco | Consequência | Mitigação Proposta (ou Implementada) | Responsável | Evidência Verificável | Limitação Restante |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Esgotamento de Energia / Combustível** | Abortagem forçada / Queda livre do módulo | *[Implementado]* Gatilho de emergência para módulos com combustível abaixo do limiar crítico (ex: $< 10\%$) | Sistema Automático / Operador de Voo | Logs de execução da fila e histórico de decisões | Taxa de consumo linear modelada sem ruídos térmicos |
| **Indisponibilidade da Área de Pouso** | Risco de colisão ou atraso prolongado em órbita | *[Proposta]* Protocolo de adiamento e redirecionamento para zonas secundárias | Equipe de Navegação Orbital | Parâmetros de disponibilidade da área nos registros | Falta de roteamento dinâmico complexo no código atual |
| **Falha Total de Sensores** | Descida às cegas sem referência de altitude | *[Implementado]* Bloqueio automático de pouso baseado na porta lógica de integridade | Sistema de Controle de Voo | Registro de módulos mantidos em estado de alerta | Ausência de simulação de redundância física de hardware |

---

## 6. Transparência e Rastreabilidade
* **Modelo de Transparência:** A rastreabilidade das decisões do MGPEB é sustentada estruturalmente por quatro eixos lógicos extraídos da execução:
  1. `[Entradas (Inputs)]`: Estado bruto do módulo e condições ambientais coletadas no momento da tentativa.
  2. `[Regra Aplicada]`: Expressão booleana ou condicional correspondente (ex: verificação de falha de sensores ou nível de combustível).
  3. `[Decisão Tomada]`: O veredito computacional gerado (*Autorizado*, *Adiado*, *Bloqueado* ou *Autorizado por emergência*).
  4. `[Motivo / Justificativa]`: O parâmetro crítico que motivou a bifurcação no fluxo lógico.
* **Alinhamento com o Código Final:** *Atenção ao escopo:* O protótipo desenvolvido utiliza estruturas lineares em memória (como listas, filas `deque` e pilhas para o histórico). Portanto, **não se deve afirmar** que o sistema possui auditoria persistente em banco de dados externo, desvio automatizado avançado para área alternativa em tempo real ou filas de emergência distribuídas, visto que esses recursos extrapolam o código final implementado nesta fase.

---

## 7. Revisão Independente e Coerência do Projeto
* **Revisão do Anexo (Davi):** Validação cruzada da consistência entre a modelagem matemática do consumo de combustível ($C(t) = C_0 - 5t$), os limiares de tempo limite ($t_{limite}$) e os dados tabulados, assegurando ausência de contradições técnicas.
* **Compilação e Coerência do Documento (Guilherme):** Conferência final da formatação, padronização visual dos diagramas lógicos e gráficos, clareza da nomenclatura dos módulos e coesão global do texto antes da entrega unificada da equipe.
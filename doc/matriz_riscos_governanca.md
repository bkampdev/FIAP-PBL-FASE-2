# Matriz de riscos e governança - MGPEB

Quadro elaborado a partir da contribuição de Gabriel (PR #7) e conferido
com os registros do exemplo determinístico durante a integração.

| Risco | Consequência potencial | Controle implementado / proposta | Responsável proposto | Evidência | Limitação |
|---|---|---|---|---|---|
| Emergência e área ocupada | Colisão ou pouso inviável | Implementado: autorização <10% sem falha total. Proposta: revisão da regra antes de uso real | Comitê técnico e operador | Energia: 9%, Tempestade/Ocupada, autorizada | Emergência ignora ambiente; não há desvio |
| Área ocupada sem emergência | Atraso e perda de reserva em espera real | Implementado: adiamento. Proposta: operador reavalia janela | Operador | Segurança: 90%, Estável/Ocupada, adiada | Não há passagem de tempo nem reentrada |
| Falha total dos sensores | Descida sem instrumentação | Implementado: bloqueio anterior à emergência. Proposta: avaliar redundância | Responsável técnico | Saúde: 5%, Falha total, bloqueada | Sem redundância física |
| Falha parcial dos sensores | Decisão com instrumentação degradada | Implementado: não bloqueia automaticamente. Proposta: revisão de critérios para falhas parciais | Responsável técnico e operador | Comunicação: 10%, Falha parcial, autorizada | Categorias não medem qualidade real |
| pop consome o histórico | Perda de rastreabilidade após exibição | Implementado: LIFO destrutivo; exemplo copia a pilha. Proposta: retenção persistente | Responsável pela auditoria | Pilha antes/depois no exemplo | Cópia é transitória; sem banco de dados |

Riscos são interpretações do grupo; não há consequências físicas simuladas,
medição de risco ou eficácia de mitigação comprovada. A auditoria proposta deve
guardar entradas, regra, decisão, motivo e versão. O histórico atual contém
apenas nome e decisão. A participação social e a alçada de exceções são propostas
de governança detalhadas em `etapa_6_esg_governanca.md`.

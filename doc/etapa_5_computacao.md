# Evolução da Computação Conectada às Limitações do Hardware Embarcado e Escolhas do MGPEB

A evolução histórica da computação — da transição dos computadores de grande porte baseados em válvulas e transistores para os modernos microcontroladores e sistemas embarcados de baixo consumo — foi guiada pela necessidade implacável de otimização de recursos. No contexto de missões espaciais (como o módulo de pouso da Aurora Siger), a computação não atua apenas como ferramenta de processamento de dados, mas como um elemento crítico de operação e sobrevivência, onde restrições físicas severas moldam diretamente as decisões de arquitetura de software, estruturas de dados e algoritmos.

---

## 1. Marcos da Evolução Computacional Aplicados a Sistemas Embarcados

Para compreender o software do MGPEB, destacam-se marcos evolutivos cruciais:
* **Circuitos Integrados e Microcontroladores:** Permitiram a descentralização do poder de processamento, viabilizando o uso de unidades de processamento dedicadas a bordo de módulos espaciais autônomos, minimizando a dependência de ciclos contínuos de telemetria com a base terrestre.
* **Evolução das Memórias de Estado Sólido:** A transição de sistemas eletromecânicos e magnéticos para memórias semicondutoras de baixo consumo reduziu drasticamente o espaço físico e a dissipação térmica, embora traga o desafio inerente da volatilidade e da suscetibilidade a falhas por radiação ionizante.

---

## 2. Restrições Físicas do Ambiente Espacial

Em operações embarcadas em ambientes extraterrestres (como Marte), o projeto de software lida com quatro limitantes críticos:

* **Memória:** Sistemas embarcados dispõem de capacidade restrita de RAM e armazenamento não volátil. Cada estrutura de dados alocada em tempo de execução compete por recursos escassos com o sistema operacional de bordo.
* **Processamento:** A frequência de clock e o paralelismo são limitados para evitar o aquecimento excessivo e o alto consumo de corrente em ambientes onde a dissipação de calor por convecção de ar é inexistente (vácuo).
* **Consumo de Energia:** A fonte primária de energia (geralmente painéis solares e baterias) é finita. Processamentos excessivos drenam a carga e comprometem o suporte operacional e a telemetria.
* **Confiabilidade e Radiação:** Partículas energéticas de alta radiação no espaço podem causar *Single Event Upsets* (SEUs), alterando o estado lógico de bits na memória física e gerando falhas operacionais.

---

## 3. Relação com os Algoritmos e Estruturas do Projeto

O código implementado para o MGPEB utiliza estruturas lineares e algoritmos fundamentais:
* **Buscas Lineares e Ordenação em `Consultas.py`:** Utiliza busca linear para localizar registros específicos e o algoritmo **Bubble Sort** para a ordenação dos módulos com base em critérios operacionais.
* **Gerenciamento de Fluxo em `main.py`:** Emprega filas estruturadas com `deque` para gerenciar a ordem de pouso, listas para controle de estados e pilhas para o rastreamento do histórico de operações.

---

## 4. Análise de Custos e Vantagens das Escolhas Algorítmicas

* **Custo de Busca e Ordenação:** A busca linear possui complexidade $O(N)$, crescendo proporcionalmente ao número de registros. O Bubble Sort apresenta complexidade quadrática $O(N^2)$, tornando-se custoso computacionalmente para grandes massas de dados.
* **Justificativa da Simplicidade:** Para a pequena amostra de dados manipulada no escopo do protótipo, a simplicidade de implementação, a legibilidade e a facilidade de auditoria do código justificam a escolha de algoritmos elementares.
* **Limite da Justificativa:** Caso a volumetria de dados telemetricos da missão aumente exponencialmente, o custo computacional do Bubble Sort e da busca linear tornará o sistema ineficiente, exigindo a adoção futura de estruturas indexadas ou algoritmos de complexidade logarítmica ($O(N \log N)$).

---

## 5. Gerenciamento de Memória e Preservação de Evidências

O uso de filas baseadas em `deque` e estruturas de pilha no `main.py` otimiza a inserção e remoção rápida de elementos nas extremidades, garantindo baixo consumo de ciclos de CPU. Contudo:
* O armazenamento contínuo de históricos exige controle para evitar o esgotamento do espaço heap disponível.
* A preservação de evidências de telemetria prioriza representações lineares simples para garantir previsibilidade e determinismo no comportamento do sistema.

---

## 6. Quadro Compacto de Relações

| Limitação Física | Decisão / Algoritmo no Projeto | Benefício Prático | Limitação Restante |
| :--- | :--- | :--- | :--- |
| **Processamento** | Uso de Bubble Sort e buscas lineares em `Consultas.py` | Código simples, direto e de fácil auditoria | Custo quadrático/linear para grandes massas de dados ($O(N^2)$ e $O(N)$) |
| **Memória** | Emprego de coleções nativas e filas com `deque` no `main.py` | Baixo *overhead* e alta eficiência em operações de inserção/remoção | Risco de estouro de pilha/heap caso o histórico cresça indefinidamente |
| **Energia / Hardware** | Processamento lógico enxuto sem dependências externas pesadas | Execução leve adequada a hardwares de baixo consumo | Inexistência de telemetria dinâmica de consumo energético no software |
| **Confiabilidade** | Estruturas de dados lineares e previsíveis | Redução de pontos de falha imprevistos e facilidade de depuração | Ausência de mecanismos redundantes de correção de erros de memória (ECC) |

---

## 7. Referências

1. TANENBAUM, Andrew S.; WOODHULL, Albert S. *Sistemas Operacionais: Projeto e Implementação*. 3. ed. Porto Alegre: Bookman, 2006.
2. PATTERSON, David A.; HENNESSY, John L. *Organização e Projeto de Computadores: A Hardware/Software Interface*. 4. ed. Rio de Janeiro: Elsevier, 2014.
3. Documentação Interna e Repositório do Projeto MGPEB (Branch `main`, commit `8d4407574fbb2501e8152b4b982855ae2cb27b2e`).
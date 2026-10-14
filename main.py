from collections import deque
import Dados

# ---------- Constantes ----------
COMBUSTIVEL_MINIMO = 10
QUANTIDADE_MODULOS = 6

# ---------- Estruturas de dados ----------
modulos_fila_de_pouso = deque()   # fila: aguardando autorização
modulos_pousados = []             # lista: autorizados
modulos_em_espera = []            # lista: adiados
modulos_em_alerta = []            # lista: bloqueados
historico_de_decisoes = []        # pilha: registro das decisões
modulos_definidos = []            # lista: todos os módulos gerados
condicoes_externas_ambiente = []  # lista: ambiente sorteado em cada tentativa


# ---------- Geração dos módulos ----------
def inicializar_simulacao(modulos=None):
    """Reinicia as coleções; aceita dados fixos para exemplos e testes."""
    for estrutura in (modulos_fila_de_pouso, modulos_pousados,
                      modulos_em_espera, modulos_em_alerta,
                      historico_de_decisoes, modulos_definidos,
                      condicoes_externas_ambiente):
        estrutura.clear()
    if modulos is None:
        modulos = [Dados.gerar_modulo() for _ in range(QUANTIDADE_MODULOS)]
    for modulo in modulos:
        modulos_definidos.append(modulo)
        modulos_fila_de_pouso.append(modulo)  # todos começam na fila


# ---------- Decisão de pouso ----------
def decide_pouso(ambientes=None):
    """Atende a fila em FIFO; ambientes fixos seguem a mesma ordem da fila."""
    quantidade_na_fila = len(modulos_fila_de_pouso)
    if ambientes is not None and len(ambientes) != quantidade_na_fila:
        raise ValueError("Informe um ambiente por módulo da fila.")

    for i in range(0, quantidade_na_fila):
        modulo_atual = modulos_fila_de_pouso.popleft()   # sai o primeiro da fila

        ambiente = (Dados.gerar_condicoes_ambiente() if ambientes is None
                    else ambientes[i])  # condições no momento da tentativa
        condicoes_externas_ambiente.append(ambiente)

        # 1. Falha total dos sensores -> Bloqueado
        if modulo_atual.integridade_sensores == "Falha total":
            modulos_em_alerta.append(modulo_atual)
            historico_de_decisoes.append(f"{modulo_atual.nome_modulo}: Bloqueado")

        # 2. Combustível baixo -> Autorizado (emergência)
        elif modulo_atual.nivel_combustivel < COMBUSTIVEL_MINIMO:
            modulos_pousados.append(modulo_atual)
            historico_de_decisoes.append(f"{modulo_atual.nome_modulo}: Autorizado (emergência)")

        # 3. Atmosfera instável ou área indisponível -> Adiado
        elif (ambiente.condicoes_atmosfericas != "Estável"
              or ambiente.disponibilidade_area != "Livre"):
            modulos_em_espera.append(modulo_atual)
            historico_de_decisoes.append(f"{modulo_atual.nome_modulo}: Adiado")

        # 4. Demais casos -> Autorizado
        else:
            modulos_pousados.append(modulo_atual)
            historico_de_decisoes.append(f"{modulo_atual.nome_modulo}: Autorizado")
            
            
def exibe_resultado():
    print("Pousados:")
    for i in range(0, len(modulos_pousados)):
        print(" -", modulos_pousados[i].nome_modulo)

    print("Em espera:")
    for i in range(0, len(modulos_em_espera)):
        print(" -", modulos_em_espera[i].nome_modulo)

    print("Em alerta:")
    for i in range(0, len(modulos_em_alerta)):
        print(" -", modulos_em_alerta[i].nome_modulo)

    print("\nHistórico de decisões (mais recente primeiro):")
    for i in range(0, len(historico_de_decisoes)):
        print(" -", historico_de_decisoes.pop())   # desempilha do topo


# ---------- Execução ----------
if __name__ == "__main__":
    inicializar_simulacao()
    decide_pouso()
    exibe_resultado()

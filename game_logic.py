# game_logic.py
import random

ABERTURAS = [1, 2, 3, 4, 5, 6]

BARRA_INICIAL = {
    1: 3,
    2: 4,
    3: 2,
    4: 5,
    5: 3,
    6: 6
}

def sortear_abertura():
    return random.choice(ABERTURAS)

def get_barra_inicial(abertura):
    return BARRA_INICIAL.get(abertura, 3)

def processar_escolha(abertura, cena, opcao, barra_atual):
    # A definir — lógica completa das escolhas por abertura
    return barra_atual

def molly_age_sozinha(abertura, cena, barra):
    # Retorna True se a Molly deve agir sozinha nessa cena
    gatilhos = {
        1: {4: 4, 7: 10},
        2: {3: 4, 7: 10},
        3: {3: 3, 7: 10},
        4: {3: 5, 5: 4},
        5: {3: 4, 7: 10},
        6: {2: 6, 5: 5},
    }
    cenas_abertura = gatilhos.get(abertura, {})
    nivel = cenas_abertura.get(cena)
    if nivel and barra >= nivel:
        return True
    return False

def get_final(abertura, barra):
    if barra <= 4:
        tipo = "bom"
    else:
        tipo = "ruim"
    return {"abertura": abertura, "tipo": tipo}
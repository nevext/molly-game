# game_logic.py

# ─────────────────────────────────────────────
# ESTRUTURA DO JOGO
# Ato 1:
#   Cap_1 (dia)   — cinemático, sem escolhas
#   Cap_2 (noite) — com escolhas, barra de ansiedade
# ─────────────────────────────────────────────

CAPITULOS = {
    "ato1_cap1_dia": {
        "tipo": "dia",
        "trilha": "journey/ato_1/Cap_1(dia)/Music/Molly_Original_Soundtrack(Day).mp3",
        "frames": [
            "journey/ato_1/Cap_1(dia)/Molly_1.png",
            "journey/ato_1/Cap_1(dia)/Molly_2.png",
            "journey/ato_1/Cap_1(dia)/Molly_3.png",
            "journey/ato_1/Cap_1(dia)/Molly_4.png",
            "journey/ato_1/Cap_1(dia)/Molly_5.png",
            "journey/ato_1/Cap_1(dia)/Molly_6.png",
        ],
        "proximo": "ato1_cap2_noite",
        "tem_escolhas": False,
    },
    "ato1_cap2_noite": {
        "tipo": "noite",
        "trilha": "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3",
        "frames": [
            "journey/ato_1/Cap_2(noite)/Molly_1.png",
            "journey/ato_1/Cap_2(noite)/Molly_2.png",
            "journey/ato_1/Cap_2(noite)/Molly_3.png",
            "journey/ato_1/Cap_2(noite)/Molly_4.png",
            "journey/ato_1/Cap_2(noite)/Molly_5.png",
            "journey/ato_1/Cap_2(noite)/Molly_6.png",
        ],
        "proximo": None,
        "tem_escolhas": True,
        "barra_inicial": 3,
        "cenas": {
            1: {
                "titulo": "A mensagem",
                "texto": "Você está deitada. O celular ilumina na mesa — uma mensagem da sua amiga. Vi que você apagou a foto. Está bem?",
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": [
                    {"texto": "Responder que está bem. É mentira mas é mais fácil.", "delta": 1},
                    {"texto": "Não responder. Fechar o celular.", "delta": 2},
                ]
            },
            2: {
                "titulo": "O feed",
                "texto": "Antes de dormir você abre o feed sem querer. A mesma garota. Mais 400 curtidas desde hoje de manhã.",
                "molly_age_nivel": 5,
                "texto_automatico": "Molly ficou olhando o perfil dela por quarenta minutos sem perceber.",
                "easter_egg": None,
                "opcoes": [
                    {"texto": "Fechar o aplicativo. Já chega.", "delta": -1},
                    {"texto": "Continuar olhando.", "delta": 2},
                ]
            },
        }
    },
}

BARRA_FINAL_BOM = 4


def get_capitulo(cap_id):
    return CAPITULOS.get(cap_id)


def get_proximo_capitulo(cap_id):
    cap = CAPITULOS.get(cap_id)
    if cap:
        return cap.get("proximo")
    return None


def processar_escolha(cap_id, cena_num, opcao_index, barra_atual):
    cap = CAPITULOS.get(cap_id)
    if not cap or not cap.get("tem_escolhas"):
        return barra_atual
    cenas = cap.get("cenas", {})
    cena = cenas.get(cena_num)
    if not cena:
        return barra_atual
    opcoes = cena.get("opcoes", [])
    if opcao_index < len(opcoes):
        delta = opcoes[opcao_index]["delta"]
        nova = barra_atual + delta
        return max(0, min(10, nova))
    return barra_atual


def molly_age_sozinha(cap_id, cena_num, barra):
    cap = CAPITULOS.get(cap_id)
    if not cap:
        return False
    cena = cap.get("cenas", {}).get(cena_num)
    if not cena:
        return False
    nivel = cena.get("molly_age_nivel")
    if nivel and barra >= nivel:
        return True
    return False


def get_final(barra):
    tipo = "bom" if barra <= BARRA_FINAL_BOM else "ruim"
    finais = {
        "bom": {
            "tipo": "bom",
            "texto": "São 23h. O celular está na mão. Você olha para ele por um segundo e coloca na gaveta. Não checou as curtidas uma última vez. Não abriu o feed. Só fechou a gaveta. A tela apaga. O quarto fica escuro. Pela primeira vez em semanas, você dorme antes da meia noite.",
            "mensagem": "Desconectar não é fraqueza. É escolha. E escolhas pequenas mudam padrões grandes.",
            "frame": "journey/ato_1/Cap_2(noite)/Molly_1.png",
        },
        "ruim": {
            "tipo": "ruim",
            "texto": "São 2h da manhã. Você ainda está checando. A foto tem 89 curtidas agora. Parece pouco. Parece sempre pouco. Você dorme às 3h. No dia seguinte acorda cansada. No outro também.",
            "mensagem": "Ansiedade digital não some sozinha. Se isso parece familiar, você não está sozinha. CVV: 188.",
            "frame": "journey/ato_1/Cap_2(noite)/Molly_6.png",
        }
    }
    return finais[tipo]
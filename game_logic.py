# game_logic.py

CAPITULOS = {
    "ato1_cap1_dia": {
        "tipo": "dia",
        "trilha": "journey/ato_1/Cap_1(dia)/Music/Molly_Original_Soundtrack(Day).mp3",
        "proximo": "ato1_cap2_noite",
        "tem_escolhas": False,
        "frames": [
            {"imagem": None, "tipo_texto": "narrador", "texto": "Era uma terça-feira comum. Molly acabou de chegar da escola."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_1.png", "tipo_texto": "narrador", "texto": "Ela ainda estava de mochila. O celular já estava na mão antes mesmo de sentar."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_1.png", "tipo_texto": "narrador", "texto": "Tinha tirado a foto no intervalo. Ajustou o filtro por quinze minutos antes de postar."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_1.png", "tipo_texto": "molly",    "texto": "Ficou boa. Ficou, né?"},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_2.png", "tipo_texto": "narrador", "texto": "Ela abriu o aplicativo. 32 curtidas. 10 minutos. O número ficou parado na cabeça dela."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_2.png", "tipo_texto": "narrador", "texto": "Parecia pouco. Ou era bom pra 10 minutos? Ela não sabia mais."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_2.png", "tipo_texto": "molly",    "texto": "As pessoas que importam nem curtiram ainda."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_3.png", "tipo_texto": "narrador", "texto": "Ela foi olhar a foto de novo. O ângulo. O filtro. Algo estava errado."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_3.png", "tipo_texto": "molly",    "texto": "Os olhos. São sempre os olhos."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_4.png", "tipo_texto": "narrador", "texto": "Ela desviou o olhar. Não era pra tela — era pra lugar nenhum."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_4.png", "tipo_texto": "molly",    "texto": "Queria que eu fosse assim. Do jeito que o filtro faz."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_5.png", "tipo_texto": "narrador", "texto": "Ela trocou o filtro. Melhorou. Pelo menos era o que ela achava."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_5.png", "tipo_texto": "molly",    "texto": "Assim está melhor. Assim parece mais... eu."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_6.png", "tipo_texto": "narrador", "texto": "Ela postou. O coração acelerou um pouco quando apertou o botão."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_6.png", "tipo_texto": "narrador", "texto": "Mas ela apertou."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_6.png", "tipo_texto": "molly",    "texto": "Agora é só esperar."},
        ]
    },

    "ato1_cap2_noite": {
        "tipo": "noite",
        "trilha": "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3",
        "proximo": "ato1_cap3_dia",
        "tem_escolhas": True,
        "barra_inicial": 3,
        "frames": [
            "journey/ato_1/Cap_2(noite)/Molly_1.png",
            "journey/ato_1/Cap_2(noite)/Molly_2.png",
            "journey/ato_1/Cap_2(noite)/Molly_3.png",
            "journey/ato_1/Cap_2(noite)/Molly_4.png",
            "journey/ato_1/Cap_2(noite)/Molly_5.png",
            "journey/ato_1/Cap_2(noite)/Molly_6.png",
        ],
        "cenas": {
            1: {
                "titulo": "A mensagem",
                "tipo_texto": "narrador",
                "texto": "Você está deitada. O celular ilumina na mesa — uma mensagem da sua amiga. Vi que você apagou a foto. Está bem?",
                "frame_idx": 0,
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
                "tipo_texto": "narrador",
                "texto": "Antes de dormir você abre o feed sem querer. A mesma garota. Mais 400 curtidas desde hoje de manhã.",
                "frame_idx": 3,
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

    "ato1_cap3_dia": {
        "tipo": "dia",
        "trilha": "journey/ato_1/Cap_1(dia)/Music/Molly_Original_Soundtrack(Day).mp3",
        "proximo": "ato2_cap4_noite",
        "tem_escolhas": False,
        "frames": [
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_1.png", "tipo_texto": "narrador", "texto": "Na manhã seguinte. O mesmo quarto. A mesma luz entrando pela janela."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_2.png", "tipo_texto": "narrador", "texto": "Ela pegou o celular antes de se levantar. 89 curtidas."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_3.png", "tipo_texto": "molly",    "texto": "89. Devia ser mais."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_4.png", "tipo_texto": "narrador", "texto": "Ela ficou olhando pro teto por um tempo."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_5.png", "tipo_texto": "narrador", "texto": "Depois levantou. Teve que levantar."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_6.png", "tipo_texto": "molly",    "texto": "Tudo bem. Hoje vai ser diferente."},
        ]
    },

    "ato2_cap4_noite": {
        "tipo": "noite",
        "trilha": "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3",
        "proximo": "fim_demo",
        "tem_escolhas": True,
        "barra_inicial": None,
        "frames": [
            "journey/ato_2/Cap_4(noite)/Molly_1.png",
            "journey/ato_2/Cap_4(noite)/Molly_2.png",
            "journey/ato_2/Cap_4(noite)/Molly_3.png",
            "journey/ato_2/Cap_4(noite)/Molly_4.png",
        ],
        "cenas": {
            1: {
                "titulo": "A comparação",
                "tipo_texto": "narrador",
                "texto": "De noite ela abriu o perfil da garota de novo. Não conseguiu não abrir.",
                "frame_idx": 0,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": [
                    {"texto": "Fechar e tentar dormir.", "delta": -1},
                    {"texto": "Continuar comparando.", "delta": 2},
                ]
            },
            2: {
                "titulo": "O espelho",
                "tipo_texto": "narrador",
                "texto": "Ela foi até o espelho. Olhou pra si mesma por um tempo longo demais.",
                "frame_idx": 2,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": [
                    {"texto": "Voltar pra cama.", "delta": -1},
                    {"texto": "Abrir o aplicativo de novo.", "delta": 2},
                ]
            },
        }
    },

    "fim_demo": {
        "tipo": "demo",
        "trilha": "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3",
        "proximo": None,
        "tem_escolhas": False,
        "frames": []
    },
}

BARRA_FINAL_BOM = 4


def get_capitulo(cap_id):
    return CAPITULOS.get(cap_id)


def get_proximo_capitulo(cap_id):
    cap = CAPITULOS.get(cap_id)
    return cap.get("proximo") if cap else None


def processar_escolha(cap_id, cena_num, opcao_index, barra_atual):
    cap = CAPITULOS.get(cap_id)
    if not cap or not cap.get("tem_escolhas"):
        return barra_atual
    cena = cap.get("cenas", {}).get(cena_num)
    if not cena:
        return barra_atual
    opcoes = cena.get("opcoes", [])
    if opcao_index < len(opcoes):
        return max(0, min(10, barra_atual + opcoes[opcao_index]["delta"]))
    return barra_atual


def molly_age_sozinha(cap_id, cena_num, barra):
    cap = CAPITULOS.get(cap_id)
    if not cap:
        return False
    cena = cap.get("cenas", {}).get(cena_num)
    if not cena:
        return False
    nivel = cena.get("molly_age_nivel")
    return bool(nivel and barra >= nivel)


def get_final(barra):
    tipo = "bom" if barra <= BARRA_FINAL_BOM else "ruim"
    finais = {
        "bom": {
            "tipo": "bom",
            "texto": "São 23h. O celular está na mão. Você olha para ele por um segundo e coloca na gaveta. Não checou as curtidas uma última vez. Não abriu o feed. Só fechou a gaveta. A tela apaga. Pela primeira vez em semanas, você dorme antes da meia noite.",
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
# game_logic.py

SFX_BASE = "journey/ato_1/Cap_2(noite)/Sound/"

CAPITULOS = {
    "ato1_cap1_dia": {
        "tipo": "dia",
        "trilha": "journey/ato_1/Cap_1(dia)/Music/Molly_Original_Soundtrack(Day).mp3",
        "proximo": "ato1_cap2_noite",
        "tem_escolhas": False,
        "frames": [
            {"imagem": None,                                        "tipo_texto": "narrador", "texto": "Era uma terça-feira comum. Molly acabou de chegar da escola."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_1.png",     "tipo_texto": "narrador", "texto": "Ela ainda estava de mochila. O celular já estava na mão antes mesmo de sentar."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_1.png",     "tipo_texto": "narrador", "texto": "Tinha tirado a foto no intervalo. Ajustou o filtro por quinze minutos antes de postar."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_1.png",     "tipo_texto": "molly",    "texto": "Ficou boa. Ficou, né?"},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_2.png",     "tipo_texto": "narrador", "texto": "Ela abriu o aplicativo. 8 curtidas. O número ficou parado na cabeça dela."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_2.png",     "tipo_texto": "narrador", "texto": "Parecia pouco. Ou era bom pra 10 minutos? Ela não sabia mais."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_2.png",     "tipo_texto": "molly",    "texto": "As pessoas que importam nem curtiram ainda."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_3.png",     "tipo_texto": "narrador", "texto": "Ela foi olhar a foto de novo. O ângulo. O filtro. Algo estava errado."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_3.png",     "tipo_texto": "molly",    "texto": "Os olhos. São sempre os olhos."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_4.png",     "tipo_texto": "narrador", "texto": "Ela desviou o olhar. Não era pra tela era pra lugar nenhum."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_4.png",     "tipo_texto": "molly",    "texto": "Queria que eu fosse assim. Do jeito que o filtro faz."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_5.png",     "tipo_texto": "narrador", "texto": "Ela trocou o filtro. Melhorou. Pelo menos era o que ela achava."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_5.png",     "tipo_texto": "molly",    "texto": "Assim está melhor. Assim parece mais... eu."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_6.png",     "tipo_texto": "narrador", "texto": "Ela postou. O coração acelerou um pouco quando apertou o botão."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_6.png",     "tipo_texto": "narrador", "texto": "Mas ela apertou mesmo assim."},
            {"imagem": "journey/ato_1/Cap_1(dia)/Molly_6.png",     "tipo_texto": "molly",    "texto": "Agora é só esperar."},
        ]
    },

    "ato1_cap2_noite": {
        "tipo": "noite",
        "trilha": "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3",
        "proximo": "ato1_cap3_dia",
        "tem_escolhas": True,
        "barra_inicial": None,
        "frames": [
            "journey/ato_1/Cap_2(noite)/Molly_1.png",
            "journey/ato_1/Cap_2(noite)/Molly_2.png",
            "journey/ato_1/Cap_2(noite)/Molly_3.png",
            "journey/ato_1/Cap_2(noite)/Molly_4.png",
            "journey/ato_1/Cap_2(noite)/Molly_5.png",
            "journey/ato_1/Cap_2(noite)/Molly_6.png",
        ],
        "cenas": {
            # Cena 1: narrador introduz, sem escolhas ainda
            1: {
                "titulo": "A mensagem",
                "tipo_texto": "narrador",
                "texto": "Você está deitada. O celular ilumina na mesa.",
                "frame_idx": 0,
                "sfx": None,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": []
            },
            # Cena 2: mesmo frame, notificação toca
            2: {
                "titulo": "A mensagem",
                "tipo_texto": "narrador",
                "texto": "Uma notificação. Alguém mandou mensagem.",
                "frame_idx": 0,
                "sfx": "Notification(Molly).mp3",
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": []
            },
            # Cena 3: Molly_2, olhando pro celular
            3: {
                "titulo": "A mensagem",
                "tipo_texto": "narrador",
                "texto": "Ela olhou para o celular. Não conseguiu não olhar.",
                "frame_idx": 1,
                "sfx": None,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": []
            },
            # Cena 4: Molly_3, pegando o celular
            4: {
                "titulo": "A mensagem",
                "tipo_texto": "narrador",
                "texto": "Ela pegou o celular. Só pra ver quem era.",
                "frame_idx": 2,
                "sfx": None,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": []
            },
            # Cena 5: Molly_4, vendo a mensagem — balão de SMS da Kelly
            5: {
                "titulo": "A mensagem",
                "tipo_texto": "sms",
                "texto": "Nada a ver oq ele disse sobre sua foto Molly, liga não viu",
                "remetente": "Kelly",
                "frame_idx": 3,
                "sfx": None,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": []
            },
            # Cena 6: Molly_4 repetido — com 3 opções
            6: {
                "titulo": "A mensagem",
                "tipo_texto": "narrador",
                "texto": "O que você faz?",
                "frame_idx": 3,
                "sfx": None,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": [
                    {"texto": "Responder \"Não ligo pra essas coisas\"",  "delta": -1, "acao": "conversa_kelly",   "posicao": "esquerda"},
                    {"texto": "Não responder e ir dormir",                "delta": 0,  "acao": "dormir",          "posicao": "direita"},
                    {"texto": "Examinar que comentário é esse",           "delta": 2,  "acao": "examinar",        "posicao": "baixo",  "sfx": "sfx_bad_ending(Molly).mp3"},
                ]
            },
        }
    },

    # Rota: Examinar o comentário
    "ato1_cap2_examinar": {
        "tipo": "noite",
        "trilha": "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3",
        "proximo": "ato1_cap3_dia",
        "tem_escolhas": True,
        "barra_inicial": None,
        "frames": [
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_1.png",
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_2.png",
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_3.png",
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_4.png",
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_5.png",
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_6.png",
            None,  # placeholder Molly_7
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_8.png",
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_9.png",
        ],
        "cenas": {
            # Molly_1 embaçado — ansiedade
            1: {
                "titulo": "O post",
                "tipo_texto": "narrador",
                "texto": "A tela estava embaçada. Ou eram os olhos dela.",
                "frame_idx": 0, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            2: {
                "titulo": "O post",
                "tipo_texto": "narrador",
                "texto": "O coração acelerou. Ela não conseguia focar. Que comentário era esse?",
                "frame_idx": 0, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            3: {
                "titulo": "O post",
                "tipo_texto": "molly",
                "texto": "Respira. Só precisa respirar.",
                "frame_idx": 0, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            # Molly_2 — vendo sem embaçado
            4: {
                "titulo": "O post",
                "tipo_texto": "narrador",
                "texto": "A imagem foi clareando. A foto. Os filtros. As curtidas.",
                "frame_idx": 1, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            5: {
                "titulo": "O post",
                "tipo_texto": "narrador",
                "texto": "8 curtidas. Mas tinha um comentário. Um comentário que ela não tinha visto antes.",
                "frame_idx": 1, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            5: {
                "titulo": "O post",
                "tipo_texto": "molly",
                "texto": "Quem comentou?",
                "frame_idx": 1, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            # Molly_3 — vê o comentário com clareza, 3 opções
            6: {
                "titulo": "O comentário",
                "tipo_texto": "narrador",
                "texto": "Ela conseguiu ver. Tinha um comentário ali.",
                "frame_idx": 2, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None,
                "opcoes": [
                    {"texto": "Deixar pra lá e ir dormir",  "delta": -1, "acao": "dormir_olho",   "posicao": "esquerda"},
                    {"texto": "Ver as curtidas",            "delta": 1,  "acao": "ver_curtidas",  "posicao": "direita"},
                    {"texto": "Ver o comentário",           "delta": 2,  "acao": "ver_comentario","posicao": "baixo"},
                ]
            },
        }
    },

    # Sub-rota: ver curtidas
    "ato1_cap2_curtidas": {
        "tipo": "noite",
        "trilha": "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3",
        "proximo": "ato1_cap2_examinar",
        "tem_escolhas": True,
        "barra_inicial": None,
        "frames": [
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_4.png",
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_5.png",
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_6.png",
        ],
        "cenas": {
            1: {
                "titulo": "As curtidas",
                "tipo_texto": "narrador",
                "texto": "Embaçado de novo. A ansiedade voltou antes dela ver o número.",
                "frame_idx": 0, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            2: {
                "titulo": "As curtidas",
                "tipo_texto": "narrador",
                "texto": "Ela foi focando. Devagar. Os nomes foram aparecendo.",
                "frame_idx": 1, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            3: {
                "titulo": "As curtidas",
                "tipo_texto": "narrador",
                "texto": "Molly H. Quem é essa Molly? Não conheço. E esse Frances? Estranho.",
                "frame_idx": 2, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": {
                    "texto": "Frances Haugen. Ela sabia sobre os filtros. Ela falou.",
                    "url": "https://www.bbc.com/portuguese/articles/c3g1q1y1y1y1"
                }, "opcoes": []
            },
            4: {
                "titulo": "As curtidas",
                "tipo_texto": "molly",
                "texto": "Espera... 32 curtidas? Não eram 8 ou 9? Devo estar com sono.",
                "frame_idx": 2, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
        }
    },

    # Sub-rota: ver comentário
    "ato1_cap2_comentario": {
        "tipo": "noite",
        "trilha": "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3",
        "proximo": "ato1_cap3_dia",
        "tem_escolhas": True,
        "barra_inicial": None,
        "frames": [
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_8.png",
            "journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_9.png",
        ],
        "cenas": {
            1: {
                "titulo": "O comentário",
                "tipo_texto": "narrador",
                "texto": "\"menor da zl\".",
                "frame_idx": 0, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            2: {
                "titulo": "O comentário",
                "tipo_texto": "molly",
                "texto": "Como assim eu não sou assim.",
                "frame_idx": 0, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            3: {
                "titulo": "O comentário",
                "tipo_texto": "narrador",
                "texto": "Talvez não tivesse falado por mal. Mas certas palavras machucam mesmo brincando.",
                "frame_idx": 0, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None, "opcoes": []
            },
            4: {
                "titulo": "O comentário",
                "tipo_texto": "narrador",
                "texto": "O que ela faz com isso agora?",
                "frame_idx": 0, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None,
                "opcoes": [
                    {"texto": "Ignorar e ir dormir",  "delta": -1, "acao": "dormir_olho",  "posicao": "esquerda"},
                    {"texto": "Apagar o post",        "delta": 3,  "acao": "apagar_post",  "posicao": "direita", "sfx": "sfx_bad_ending(Molly).mp3", "borboleta": True},
                ]
            },
            # Cena de apagar o post
            5: {
                "titulo": "Apagou",
                "tipo_texto": "molly",
                "texto": "Estou com sono.",
                "frame_idx": 1, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None,
                "opcoes": [],
                "cortar_musica": True,
                "ir_dormir": True,
            },
        }
    },

    # Rota: conversa com Kelly
    "ato1_cap2_kelly": {
        "tipo": "noite",
        "trilha": "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3",
        "proximo": "ato1_cap3_dia",
        "tem_escolhas": True,
        "barra_inicial": None,
        "frames": [
            "journey/ato_1/Cap_2(noite)/Molly_5.png",
        ],
        "cenas": {
            1: {
                "titulo": "Kelly",
                "tipo_texto": "conversa",
                "frame_idx": 0, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None,
                "opcoes": [],
                "mensagens": [
                    {"lado": "deles", "nome": "Kelly", "texto": "Nada a ver oq ele disse sobre sua foto Molly 🙄"},
                    {"lado": "eu",                     "texto": "Não ligo pra essas coisas"},
                    {"lado": "deles", "nome": "Kelly", "texto": "ainda bem!! vc é linda do jeito q é"},
                    {"lado": "deles", "nome": "Kelly", "texto": "ai soube das noticias?"},
                    {"lado": "eu",                     "texto": "q noticias"},
                    {"lado": "deles", "nome": "Kelly", "texto": "tao procurando uma Reporter por ai"},
                    {"lado": "deles", "nome": "Kelly", "texto": "parece q ela é perigosa"},
                    {"lado": "deles", "nome": "Kelly", "texto": "a tv disse q se ver ela tem q chamar as autoridades"},
                    {"lado": "eu",                     "texto": "sério?? q assustador"},
                    {"lado": "deles", "nome": "Kelly", "texto": "pois é... fica ligada tá"},
                    {"lado": "deles", "nome": "Kelly", "texto": "vai dormir tá tarde demais"},
                    {"lado": "eu",                     "texto": "tá bom. boa noite kel 🦋"},
                    {"lado": "deles", "nome": "Kelly", "texto": "boa noite molly 🦋"},
                ],
                "ir_dormir": True,
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
                "frame_idx": 0, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None,
                "opcoes": [
                    {"texto": "Fechar e tentar dormir.", "delta": -1, "acao": "dormir", "posicao": "esquerda"},
                    {"texto": "Continuar comparando.",  "delta": 2,  "acao": "proximo", "posicao": "direita"},
                ]
            },
            2: {
                "titulo": "O espelho",
                "tipo_texto": "narrador",
                "texto": "Ela foi até o espelho. Olhou pra si mesma por um tempo longo demais.",
                "frame_idx": 2, "sfx": None, "molly_age_nivel": None,
                "texto_automatico": None, "easter_egg": None,
                "opcoes": [
                    {"texto": "Voltar pra cama.",         "delta": -1, "acao": "dormir", "posicao": "esquerda"},
                    {"texto": "Abrir o aplicativo de novo.", "delta": 2, "acao": "proximo", "posicao": "direita"},
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
        return barra_atual, None
    cena = cap.get("cenas", {}).get(cena_num)
    if not cena:
        return barra_atual, None
    opcoes = cena.get("opcoes", [])
    if opcao_index < len(opcoes):
        op = opcoes[opcao_index]
        nova = max(0, min(10, barra_atual + op.get("delta", 0)))
        return nova, op.get("acao", "proximo")
    return barra_atual, None


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
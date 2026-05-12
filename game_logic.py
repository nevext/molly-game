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
                    {"texto": "Deixar pra lá e ir dormir",  "delta": -1, "acao": "dormir_olho",   "posicao": "esquerda", "sumir_apos": True},
                    {"texto": "Ver as curtidas",            "delta": 1,  "acao": "ver_curtidas",  "posicao": "direita",  "sumir_apos": True},
                    {"texto": "Ver o comentário",           "delta": 2,  "acao": "ver_comentario","posicao": "baixo"},
                ],
                "volta_aqui": True,
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
                "tipo_texto": "molly",
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
                "texto_automatico": None, "easter_egg": None, "opcoes": [],
                "fim_curtidas": True,
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
                "tipo_texto": "molly",
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
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_1.png", "tipo_texto": "narrador", "texto": "Ela acabou de chegar da escola. O celular estava ali, esperando. Os amigos dela nem tocaram no assunto do post, a não ser a Kelly. Será que era pra tanto?"},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_1.png", "tipo_texto": "molly", "texto": "Será que exagerei? Ou foi só um dia ruim?"},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_2.png", "tipo_texto": "narrador", "texto": "Ela pegou o celular. Uma notificação chegou. Era Kelly."},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_2.png", "tipo_texto": "sms", "texto": "Ei Molly, posta mais fotos hoje! Você é bonita demais, vai arrasar!"},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_2.png", "tipo_texto": "narrador", "texto": "Ela hesitou, mas Kelly insistiu. 'Você merece mostrar o quão incrível é'. Molly se convenceu."},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_3.png", "tipo_texto": "molly", "texto": "Ela tem razão... talvez eu deva tentar de novo. Vou fazer direito dessa vez."},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_4.png", "tipo_texto": "narrador", "texto": "Ela ajustou o ângulo, o filtro. Tudo tinha que ser perfeito."},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_4.png", "tipo_texto": "molly", "texto": "Assim... não, espera. Melhor assim."},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_5.png", "tipo_texto": "narrador", "texto": "A tela mostrou a imagem. Não era o que ela esperava. Os olhos, o sorriso... algo errado."},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_5.png", "tipo_texto": "molly", "texto": "Não ficou boa. De novo não. Por que eu não consigo?"},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_6.png", "tipo_texto": "narrador", "texto": "Ela baixou o celular. O cansaço venceu. Talvez amanhã."},
            {"imagem": "journey/ato_1/Cap_3(dia)/Molly_6.png", "tipo_texto": "molly", "texto": "Estou cansada disso. Tudo bem, deixa pra lá."},
        ]
    },

    "ato2_cap4_noite": {
        "tipo": "noite",
        "trilha": "journey/ato_2/Cap_4(noite)/Music/Molly_Original_Soundtrack(Night).mp3",
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
                "titulo": "A noite",
                "tipo_texto": "narrador",
                "texto": "Você está deitada. O celular ilumina na mesa.",
                "frame_idx": 0,
                "sfx": None,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": []
            },
            2: {
                "titulo": "A noite",
                "tipo_texto": "narrador",
                "texto": "Uma notificação. Alguém mandou mensagem.",
                "frame_idx": 0,
                "sfx": "Notification(Molly).mp3",
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": []
            },
            3: {
                "titulo": "A noite",
                "tipo_texto": "narrador",
                "texto": "Ela virou para olhar. O coração acelerou um pouco.",
                "frame_idx": 1,
                "sfx": None,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": [
                    {"texto": "Ver a mensagem", "delta": 0, "acao": "ver_kelly", "posicao": "direita"},
                    {"texto": "Ir dormir", "delta": 0, "acao": "dormir", "posicao": "esquerda"},
                    {"texto": "Ficar olhando para o teto", "delta": 0, "acao": "olhar_teto", "posicao": "baixo"},
                ]
            },
        }
    },

    "ato2_cap4_kelly": {
        "tipo": "noite",
        "trilha": "journey/ato_2/Cap_4(noite)/Music/Molly_Original_Soundtrack(Night).mp3",
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
                "titulo": "Pegando o celular",
                "tipo_texto": "narrador",
                "texto": "Ela pegou o celular. Era Kelly.",
                "frame_idx": 2,
                "sfx": None,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": []
            },
            2: {
                "titulo": "Mensagens de Kelly",
                "tipo_texto": "conversa",
                "frame_idx": 3,
                "sfx": None,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": [
                    {"texto": "Responder para Kelly", "delta": 0, "acao": "responder", "posicao": "direita"},
                    {"texto": "Deixar para depois", "delta": 0, "acao": "deixar_pra_la", "posicao": "esquerda"},
                ],
                "mensagens": [
                    {"lado": "deles", "nome": "Kelly", "texto": "Oi molly, mandei mensagem na janta, respondeu?"},
                    {"lado": "deles", "nome": "Kelly", "texto": "Vc tá bem?"},
                    {"lado": "deles", "nome": "Kelly", "texto": "Não tá respondendo no grupo tbm..."},
                    {"lado": "deles", "nome": "Kelly", "texto": "Tô preocupada, fale comigo"},
                ]
            },
            3: {
                "titulo": "Conversando com Kelly",
                "tipo_texto": "conversa",
                "frame_idx": 3,
                "sfx": None,
                "molly_age_nivel": None,
                "texto_automatico": None,
                "easter_egg": None,
                "opcoes": [],
                "mensagens_barra_alta": [
                    {"lado": "eu", "texto": "Oi Kel, tava só ocupada mesmo"},
                    {"lado": "deles", "nome": "Kelly", "texto": "Ocupada com quê? Você tava dormindo?"},
                    {"lado": "eu", "texto": "É... tipo... estudos e tal"},
                    {"lado": "deles", "nome": "Kelly", "texto": "Molly... você tá bem mesmo?"},
                    {"lado": "eu", "texto": "Sim, tô sim. Tá tudo bem mesmo"},
                    {"lado": "deles", "nome": "Kelly", "texto": "Tá... mas você sabe que pode contar comigo né"},
                    {"lado": "eu", "texto": "Eu sei. Obrigada Kel"},
                ],
                "mensagens_barra_baixa": [
                    {"lado": "eu", "texto": "Oi Kel, tava dormindo"},
                    {"lado": "deles", "nome": "Kelly", "texto": "Você não dorme tão cedo assim, fala a verdade"},
                    {"lado": "eu", "texto": "Tá... não tava dormindo"},
                    {"lado": "eu", "texto": "Só tô cansada sabe"},
                    {"lado": "deles", "nome": "Kelly", "texto": "Do quê? Aconteceu algo?"},
                    {"lado": "eu", "texto": "Não... é só... tudo"},
                    {"lado": "deles", "nome": "Kelly", "texto": "Você quer conversar? Sobre a foto de ontem?"},
                    {"lado": "eu", "texto": "Não sei... acho q sim"},
                    {"lado": "deles", "nome": "Kelly", "texto": "Vc é linda mesmo Molly, acredita em mim?"},
                    {"lado": "deles", "nome": "Kelly", "texto": "Não precisa de filtro pra ninguém gostar de você"},
                    {"lado": "eu", "texto": "Obrigada Kel... 🦋"},
                ],
                "ir_dormir": True,
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
# app.py
import os
from flask import Flask, render_template, session, redirect, url_for, jsonify
from game_logic import get_capitulo, get_proximo_capitulo, processar_escolha, molly_age_sozinha, get_final, get_flag_escolha

TRILHAS_NOITE = [
    "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night).mp3",
    "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3",
    "journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_3).mp3",
]

TRILHA_NOMES = {
    "Molly_Original_Soundtrack(Day).mp3":    "Molly OST — Dia",
    "Molly_Original_Soundtrack(Night).mp3":  "Molly OST — Noite",
    "Molly_Original_Soundtrack(Night_2).mp3":"Molly OST — Noite 2",
    "Molly_Original_Soundtrack(Night_3).mp3":"Molly OST — Noite 3",
    "Cannibal_remix_nightmare.mp3":          "Cannibal (Remix)",
    "Color_Your_Night_Remix(Molly).mp3":     "Color Your Night",
    "Four_Seasons.mp3":                      "Four Seasons",
    "Hey_Kids.mp3":                          "Hey Kids",
    "Its_Going_Down_Now _Remix(Molly).mp3":  "It's Going Down Now",
    "Last_Surprise_Remix(Molly).mp3":        "Last Surprise",
    "Mr_Magic_Remix(Molly).mp3":             "Mr. Magic",
    "Refrao_O_Sol.mp3":                      "Refrão — O Sol",
}

HUD_MAP = {
    "ato1_cap1_dia":       ("Ato 1", "Capítulo 1"),
    "ato1_cap2_noite":     ("Ato 1", "Capítulo 2"),
    "ato1_cap2_examinar":  ("Ato 1", "Capítulo 2"),
    "ato1_cap2_curtidas":  ("Ato 1", "Capítulo 2"),
    "ato1_cap2_comentario":("Ato 1", "Capítulo 2"),
    "ato1_cap2_kelly":     ("Ato 1", "Capítulo 2"),
    "ato1_cap3_dia":       ("Ato 1", "Capítulo 3"),
    "ato2_cap4_noite":     ("Ato 2", "Capítulo 4"),
    "ato2_cap4_kelly":     ("Ato 2", "Capítulo 4"),
    "ato1_cap5_dia":       ("Ato 2", "Capítulo 5"),
    "ato2_cap6_noite":     ("Ato 2", "Capítulo 6"),
    "ato3_cap5_dia":       ("Ato 3", "Capítulo 7"),
    "ato3_cap6_noite":     ("Ato 3", "Capítulo 8"),
    "ato3_cap7_dia":       ("Ato 3", "Capítulo 9"),
    "ato3_cap8_dia":       ("Ato 3", "Capítulo 10"),
    "ato3_cap9_noite":     ("Ato 3", "Capítulo 11"),
}

def get_trilha_noite():
    idx = session.get("noite_count", 0) % len(TRILHAS_NOITE)
    return TRILHAS_NOITE[idx]

def incrementar_noite():
    session["noite_count"] = session.get("noite_count", 0) + 1

def trilha_nome(trilha_path):
    filename = os.path.basename(trilha_path)
    return TRILHA_NOMES.get(filename, filename.replace(".mp3", "").replace("_", " "))

def hud_info(cap_id):
    return HUD_MAP.get(cap_id, ("", ""))

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "molly2026")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/jogar")
def jogar():
    session.clear()
    session["cap"] = "ato1_cap1_dia"
    session["frame"] = 0
    session["barra"] = 3
    session["cena"] = 1
    session["noite_count"] = 0
    session["contador_kelly"] = 0
    return redirect(url_for("cena"))


@app.route("/cena")
def cena():
    cap_id  = session.get("cap", "ato1_cap1_dia")
    frame_idx = session.get("frame", 0)
    barra   = session.get("barra", 3)
    cena_num = session.get("cena", 1)

    cap = get_capitulo(cap_id)
    if not cap:
        return redirect(url_for("index"))

    # Trilha rotativa para noite
    if cap.get("tipo") == "noite":
        trilha = get_trilha_noite()
    else:
        trilha = cap.get("trilha", "")

    if cap.get("tipo") == "demo":
        return render_template("fimdemo.html")

    hud = hud_info(cap_id)
    tnome = trilha_nome(trilha)

    # DIA
    if not cap.get("tem_escolhas"):
        frames = cap.get("frames", [])
        total  = len(frames)
        if frame_idx >= total:
            proximo = get_proximo_capitulo(cap_id)
            if proximo:
                session["cap"] = proximo
                session["frame"] = 0
                session["cena"] = 1
                cap_prox = get_capitulo(proximo)
                if not cap_prox or cap_prox.get("tipo") == "demo":
                    return redirect(url_for("cena"))
                tipo = cap_prox.get("tipo", "noite")
                return redirect(url_for("transicao", tipo=tipo))
            return redirect(url_for("final"))

        frame_atual = frames[frame_idx]
        frame_ant   = frames[frame_idx - 1] if frame_idx > 0 else None
        imagem_mudou = frame_ant is None or frame_ant.get("imagem") != frame_atual.get("imagem")

        return render_template("cena.html",
            cap_id=cap_id, tipo="dia", trilha=trilha,
            frame=frame_atual, frame_idx=frame_idx,
            total_frames=total, imagem_mudou=imagem_mudou,
            tem_escolhas=False, dados=None,
            molly_age=False, barra=barra, cena_num=cena_num,
            hud_ato=hud[0], hud_cap=hud[1], trilha_nome=tnome)

    # NOITE
    frames_noite = cap.get("frames", [])
    cenas = cap.get("cenas", {})
    dados_cena = cenas.get(cena_num)

    if not dados_cena:
        return redirect(url_for("final"))

    frame_idx_cena = dados_cena.get("frame_idx", 0)
    frame_atual = frames_noite[frame_idx_cena] if frame_idx_cena < len(frames_noite) else None
    age = molly_age_sozinha(cap_id, cena_num, barra)

    # Detectar se voltou de curtidas
    session_volta = session.pop("volta_curtidas", False)

    # Resolver mensagens para render server-side
    dados_cena = dict(dados_cena)
    if not dados_cena.get("mensagens"):
        contador_kelly = session.get("contador_kelly", 0)
        if contador_kelly >= 2 and dados_cena.get("mensagens_contador_kelly"):
            dados_cena["mensagens"] = dados_cena["mensagens_contador_kelly"]
        elif dados_cena.get("mensagens_barra_alta") or dados_cena.get("mensagens_barra_baixa"):
            if barra > 5:
                dados_cena["mensagens"] = dados_cena.get("mensagens_barra_alta", [])
            else:
                dados_cena["mensagens"] = dados_cena.get("mensagens_barra_baixa", [])
        else:
            humor = session.get("humor_kelly", "animada")
            if humor == "insegura":
                dados_cena["mensagens"] = dados_cena.get("mensagens_humor_insegura", [])
            else:
                dados_cena["mensagens"] = dados_cena.get("mensagens_humor_animada", [])

    return render_template("cena.html",
        cap_id=cap_id, tipo="noite", trilha=trilha,
        frame=frame_atual, frame_idx=frame_idx,
        total_frames=len(cenas), imagem_mudou=True,
        tem_escolhas=True, dados=dados_cena,
        molly_age=age, barra=barra, cena_num=cena_num,
        session_volta=session_volta,
        sfx_base="/static/journey/ato_1/Cap_2(noite)/Sound/",
        hud_ato=hud[0], hud_cap=hud[1], trilha_nome=tnome)


@app.route("/avancar_frame")
def avancar_frame():
    cap_id = session.get("cap", "ato1_cap1_dia")
    frame_idx = session.get("frame", 0)
    cap = get_capitulo(cap_id)
    if not cap:
        return redirect(url_for("index"))

    total = len(cap.get("frames", []))
    proximo = frame_idx + 1

    if proximo >= total:
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
            cap_prox = get_capitulo(proximo_cap)
            if not cap_prox or cap_prox.get("tipo") == "demo":
                return redirect(url_for("cena"))
            tipo = cap_prox.get("tipo", "noite")
            return redirect(url_for("transicao", tipo=tipo))
        return redirect(url_for("final"))

    session["frame"] = proximo
    return redirect(url_for("cena"))


@app.route("/frame_data")
def frame_data():
    from flask import jsonify
    cap_id = session.get("cap", "ato1_cap1_dia")
    frame_idx = session.get("frame", 0)
    cap = get_capitulo(cap_id)

    if not cap or cap.get("tem_escolhas"):
        return jsonify({"fim": True, "redirect": "/final"})

    frames = cap.get("frames", [])
    total  = len(frames)
    proximo = frame_idx + 1
    session["frame"] = proximo

    if proximo >= total:
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
            cap_prox = get_capitulo(proximo_cap)
            if not cap_prox or cap_prox.get("tipo") == "demo":
                return jsonify({"fim": True, "redirect": "/cena"})
            tipo = cap_prox.get("tipo", "noite")
            return jsonify({"fim": True, "redirect": f"/transicao/{tipo}"})
        return jsonify({"fim": True, "redirect": "/final"})

    frame_ant   = frames[frame_idx]
    frame_atual = frames[proximo]
    imagem_mudou = frame_ant.get("imagem") != frame_atual.get("imagem")

    return jsonify({
        "fim": False,
        "imagem": frame_atual.get("imagem"),
        "tipo_texto": frame_atual.get("tipo_texto"),
        "texto": frame_atual.get("texto"),
        "imagem_mudou": imagem_mudou,
    })


@app.route("/transicao/<tipo>")
def transicao(tipo):
    return render_template("transicao.html", tipo=tipo)


@app.route("/transicao_pesadelo")
def transicao_pesadelo():
    return render_template("transicao_pesadelo.html")


@app.route("/transicao_sonho_bom")
def transicao_sonho_bom():
    return render_template("transicao_sonho_bom.html")


@app.route("/iniciar_cap")
def iniciar_cap():
    cap_id = session.get("cap", "")
    cap = get_capitulo(cap_id)
    if cap and cap.get("tipo") == "noite":
        incrementar_noite()
    return redirect(url_for("cena"))


@app.route("/escolha/<int:opcao>")
def escolha(opcao):
    cap_id   = session.get("cap")
    cena_num = session.get("cena", 1)
    barra    = session.get("barra", 3)

    nova_barra, acao = processar_escolha(cap_id, cena_num, opcao, barra)
    session["barra"] = nova_barra

    # delta_extra por contador_kelly >= 2 (ato2_cap4_kelly cena 3)
    _cap_def = get_capitulo(cap_id)
    if _cap_def:
        _cena_def = _cap_def.get("cenas", {}).get(cena_num, {})
        _delta_extra = _cena_def.get("delta_extra_contador", 0)
        if _delta_extra and session.get("contador_kelly", 0) >= 2:
            nova_barra = max(0, min(10, nova_barra + _delta_extra))
            session["barra"] = nova_barra

    # Ações especiais
    if acao == "dormir" or acao == "dormir_olho":
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
        return redirect(url_for("transicao", tipo="dia"))

    if acao == "examinar":
        session["cap"] = "ato1_cap2_examinar"
        session["frame"] = 0
        session["cena"] = 1
        return redirect(url_for("cena"))

    if acao == "conversa_kelly":
        flag = get_flag_escolha(cap_id, cena_num, opcao)
        if "humor" in flag:
            session["humor_kelly"] = flag["humor"]
        session["contador_kelly"] = session.get("contador_kelly", 0) + 1
        session["cap"] = "ato1_cap2_kelly"
        session["frame"] = 0
        session["cena"] = 1
        return redirect(url_for("cena"))

    if acao == "ver_curtidas":
        session["cap"] = "ato1_cap2_curtidas"
        session["frame"] = 0
        session["cena"] = 1
        return redirect(url_for("cena"))

    if acao == "ver_comentario":
        session["cap"] = "ato1_cap2_comentario"
        session["frame"] = 0
        session["cena"] = 1
        return redirect(url_for("cena"))

    if acao == "apagar_post":
        # Avança para cena 5 do comentario (apagou)
        session["cena"] = 5
        return redirect(url_for("cena"))

    if acao == "ver_kelly":
        _cap_vk = get_capitulo(cap_id)
        if _cap_vk:
            _op_vk = _cap_vk.get("cenas", {}).get(cena_num, {}).get("opcoes", [])
            if opcao < len(_op_vk) and _op_vk[opcao].get("contador_kelly"):
                session["contador_kelly"] = session.get("contador_kelly", 0) + _op_vk[opcao]["contador_kelly"]
        session["cap"] = "ato2_cap4_kelly"
        session["frame"] = 0
        session["cena"] = 1
        return redirect(url_for("cena"))

    if acao == "olhar_teto":
        session["cena"] = 4
        return redirect(url_for("cena"))

    if acao == "dormir_cap4":
        session["cena"] = 7
        return redirect(url_for("cena"))

    if acao == "responder":
        session["cena"] = 3
        return redirect(url_for("cena"))

    if acao == "deixar_pra_la":
        return redirect(url_for("final"))

    # Ação padrão: próxima cena
    cap = get_capitulo(cap_id)
    cenas = cap.get("cenas", {}) if cap else {}
    proxima = cena_num + 1

    if proxima not in cenas:
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
            cap_prox = get_capitulo(proximo_cap)
            if not cap_prox or cap_prox.get("tipo") == "demo":
                return redirect(url_for("cena"))
            return redirect(url_for("transicao", tipo=cap_prox.get("tipo", "noite")))
        return redirect(url_for("final"))

    session["cena"] = proxima
    return redirect(url_for("cena"))


@app.route("/avancar")
def avancar():
    cap_id   = session.get("cap")
    cena_num = session.get("cena", 1)
    cap = get_capitulo(cap_id)
    cenas = cap.get("cenas", {}) if cap else {}

    dados_cena = cenas.get(cena_num, {})

    # Fim das curtidas: volta para examinar cena 6 (3 opções com fade)
    if dados_cena.get("fim_curtidas"):
        session["cap"] = "ato1_cap2_examinar"
        session["cena"] = 6
        session["frame"] = 0
        session["volta_curtidas"] = True
        return redirect(url_for("cena"))

    # Ir dormir: transição para dia
    if dados_cena.get("ir_dormir"):
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
        return redirect(url_for("transicao", tipo="dia"))

    proxima = cena_num + 1
    if proxima not in cenas:
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
            cap_prox = get_capitulo(proximo_cap)
            if not cap_prox or cap_prox.get("tipo") == "demo":
                return redirect(url_for("cena"))
            return redirect(url_for("transicao", tipo=cap_prox.get("tipo", "noite")))
        return redirect(url_for("final"))

    session["cena"] = proxima
    return redirect(url_for("cena"))


def build_cena_json(cap_id, cena_num, barra):
    cap = get_capitulo(cap_id)
    if not cap:
        return {"fim": True, "redirect": "/"}
    frames_noite = cap.get("frames", [])
    cenas = cap.get("cenas", {})
    dados_cena = cenas.get(cena_num)
    if not dados_cena:
        return {"fim": True, "redirect": "/final"}
    frame_idx_cena = dados_cena.get("frame_idx", 0)
    frame_atual = frames_noite[frame_idx_cena] if frame_idx_cena < len(frames_noite) else None
    age = molly_age_sozinha(cap_id, cena_num, barra)
    
    # Escolher mensagens baseado na barra (se existirem variações)
    mensagens = dados_cena.get("mensagens", [])
    if not mensagens:
        contador_kelly = session.get("contador_kelly", 0)
        if contador_kelly >= 2 and dados_cena.get("mensagens_contador_kelly"):
            mensagens = dados_cena.get("mensagens_contador_kelly", [])
        elif barra > 5:
            mensagens = dados_cena.get("mensagens_barra_alta", [])
        else:
            mensagens = dados_cena.get("mensagens_barra_baixa", [])
    # Roteamento por humor (ato1_cap2_kelly)
    if not mensagens:
        humor = session.get("humor_kelly", "animada")
        if humor == "insegura":
            mensagens = dados_cena.get("mensagens_humor_insegura", [])
        else:
            mensagens = dados_cena.get("mensagens_humor_animada", [])
    
    return {
        "fim": False,
        "frame": frame_atual,
        "tipo_texto": dados_cena.get("tipo_texto"),
        "texto": dados_cena.get("texto", ""),
        "titulo": dados_cena.get("titulo", ""),
        "remetente": dados_cena.get("remetente", ""),
        "mensagens": mensagens,
        "sfx": dados_cena.get("sfx"),
        "sfx_base": "/static/journey/ato_1/Cap_2(noite)/Sound/",
        "opcoes": dados_cena.get("opcoes", []),
        "easter_egg": dados_cena.get("easter_egg"),
        "molly_age": age,
        "barra": barra,
        "volta_aqui": dados_cena.get("volta_aqui", False),
        "session_volta": False,
        "ir_dormir": dados_cena.get("ir_dormir", False),
        "fim_curtidas": dados_cena.get("fim_curtidas", False),
        "cortar_musica": dados_cena.get("cortar_musica", False),
    }


@app.route("/avancar_data")
def avancar_data():
    cap_id   = session.get("cap")
    cena_num = session.get("cena", 1)
    barra    = session.get("barra", 3)
    cap = get_capitulo(cap_id)
    cenas = cap.get("cenas", {}) if cap else {}
    dados_cena = cenas.get(cena_num, {})

    if dados_cena.get("fim_curtidas"):
        session["cap"] = "ato1_cap2_examinar"
        session["cena"] = 6
        session["frame"] = 0
        result = build_cena_json("ato1_cap2_examinar", 6, barra)
        result["session_volta"] = True
        return jsonify(result)

    if dados_cena.get("vai_dormir"):
        # Determinar tipo de transição baseado na barra: 0-1=sonho, 2-8=linear, 9-10=pesadelo
        if barra >= 9:
            session["transicao_tipo"] = "pesadelo"
            return jsonify({"fim": True, "redirect": "/transicao_pesadelo"})
        elif barra <= 1:
            session["transicao_tipo"] = "sonho_bom"
            return jsonify({"fim": True, "redirect": "/transicao_sonho_bom"})
        else:
            prox_dormir = cap.get("proximo_dormir") if cap else None
            session["cap"] = prox_dormir or "ato1_cap5_dia"
            session["frame"] = 0
            session["cena"] = 1
            return jsonify({"fim": True, "redirect": "/transicao/dia"})

    if dados_cena.get("ir_dormir"):
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
        return jsonify({"fim": True, "redirect": "/transicao/dia"})

    proxima = cena_num + 1
    if proxima not in cenas:
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
            cap_prox = get_capitulo(proximo_cap)
            if not cap_prox or cap_prox.get("tipo") == "demo":
                return jsonify({"fim": True, "redirect": "/cena"})
            return jsonify({"fim": True, "redirect": f"/transicao/{cap_prox.get('tipo', 'noite')}"})
        return jsonify({"fim": True, "redirect": "/final"})

    session["cena"] = proxima
    return jsonify(build_cena_json(cap_id, proxima, barra))


@app.route("/escolha_data/<int:opcao>")
def escolha_data(opcao):
    cap_id   = session.get("cap")
    cena_num = session.get("cena", 1)
    barra    = session.get("barra", 3)

    nova_barra, acao = processar_escolha(cap_id, cena_num, opcao, barra)
    session["barra"] = nova_barra

    # delta_extra por contador_kelly >= 2 (ato2_cap4_kelly cena 3)
    _cap_def2 = get_capitulo(cap_id)
    if _cap_def2:
        _cena_def2 = _cap_def2.get("cenas", {}).get(cena_num, {})
        _delta_extra2 = _cena_def2.get("delta_extra_contador", 0)
        if _delta_extra2 and session.get("contador_kelly", 0) >= 2:
            nova_barra = max(0, min(10, nova_barra + _delta_extra2))
            session["barra"] = nova_barra

    if acao in ("dormir", "dormir_olho"):
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
        return jsonify({"fim": True, "redirect": "/transicao/dia", "dormir": True})

    if acao == "examinar":
        session["cap"] = "ato1_cap2_examinar"
        session["frame"] = 0
        session["cena"] = 1
        return jsonify(build_cena_json("ato1_cap2_examinar", 1, nova_barra))

    if acao == "conversa_kelly":
        flag = get_flag_escolha(cap_id, cena_num, opcao)
        if "humor" in flag:
            session["humor_kelly"] = flag["humor"]
        session["contador_kelly"] = session.get("contador_kelly", 0) + 1
        session["cap"] = "ato1_cap2_kelly"
        session["frame"] = 0
        session["cena"] = 1
        return jsonify(build_cena_json("ato1_cap2_kelly", 1, nova_barra))

    if acao == "ver_curtidas":
        session["cap"] = "ato1_cap2_curtidas"
        session["frame"] = 0
        session["cena"] = 1
        return jsonify(build_cena_json("ato1_cap2_curtidas", 1, nova_barra))

    if acao == "ver_comentario":
        session["cap"] = "ato1_cap2_comentario"
        session["frame"] = 0
        session["cena"] = 1
        return jsonify(build_cena_json("ato1_cap2_comentario", 1, nova_barra))

    if acao == "apagar_post":
        session["cena"] = 5
        return jsonify(build_cena_json(cap_id, 5, nova_barra))

    if acao == "ver_kelly":
        _cap_vk2 = get_capitulo(cap_id)
        if _cap_vk2:
            _op_vk2 = _cap_vk2.get("cenas", {}).get(cena_num, {}).get("opcoes", [])
            if opcao < len(_op_vk2) and _op_vk2[opcao].get("contador_kelly"):
                session["contador_kelly"] = session.get("contador_kelly", 0) + _op_vk2[opcao]["contador_kelly"]
        session["cap"] = "ato2_cap4_kelly"
        session["frame"] = 0
        session["cena"] = 1
        return jsonify(build_cena_json("ato2_cap4_kelly", 1, nova_barra))

    if acao == "olhar_teto":
        session["cena"] = 4
        return jsonify(build_cena_json(cap_id, 4, nova_barra))

    if acao == "dormir_cap4":
        session["cena"] = 7
        return jsonify(build_cena_json(cap_id, 7, nova_barra))

    if acao == "responder":
        session["cena"] = 3
        return jsonify(build_cena_json(cap_id, 3, nova_barra))

    if acao == "deixar_pra_la":
        return jsonify({"fim": True, "redirect": "/final"})

    if acao == "final_aceitar":
        session["tipo_final"] = "aceitar"
        return jsonify({"fim": True, "redirect": "/final"})

    if acao == "final_lutar":
        session["tipo_final"] = "lutar"
        return jsonify({"fim": True, "redirect": "/final"})

    cap = get_capitulo(cap_id)
    cenas = cap.get("cenas", {}) if cap else {}
    proxima = cena_num + 1
    if proxima not in cenas:
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
            cap_prox = get_capitulo(proximo_cap)
            if not cap_prox or cap_prox.get("tipo") == "demo":
                return jsonify({"fim": True, "redirect": "/cena"})
            return jsonify({"fim": True, "redirect": f"/transicao/{cap_prox.get('tipo', 'noite')}"})
        return jsonify({"fim": True, "redirect": "/final"})

    session["cena"] = proxima
    return jsonify(build_cena_json(cap_id, proxima, nova_barra))


@app.route("/final")
def final():
    barra = session.get("barra", 3)
    tipo_final = session.get("tipo_final", None)
    dados = get_final(barra, tipo_forcado=tipo_final)
    return render_template("final.html", dados=dados)


@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect(url_for("index"))


@app.route("/test_transitions")
def test_transitions():
    """Página de teste para transições"""
    return render_template("test_transitions.html")


@app.route("/set_barra/<int:valor>")
def set_barra(valor):
    """Define a barra para testes - apenas em debug"""
    if app.debug:
        session["barra"] = max(0, min(10, valor))
        return jsonify({"barra": session.get("barra"), "status": "ok"})
    return jsonify({"status": "erro", "msg": "Apenas em modo debug"})


@app.route("/force_sleep")
def force_sleep():
    """Força a cena de dormir para testes rápidos"""
    if app.debug:
        session["cap"] = "ato2_cap4_kelly"
        session["cena"] = 7  # Última cena antes de dormir
        session["frame"] = 0
        return redirect(url_for("cena"))
    return jsonify({"status": "erro"})


if __name__ == "__main__":
    app.run(debug=True)
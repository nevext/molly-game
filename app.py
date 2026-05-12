# app.py
from flask import Flask, render_template, session, redirect, url_for, jsonify
from game_logic import get_capitulo, get_proximo_capitulo, processar_escolha, molly_age_sozinha, get_final

app = Flask(__name__)
app.secret_key = "molly2026"


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

    trilha = cap.get("trilha", "")

    if cap.get("tipo") == "demo":
        return render_template("fim_demo.html")

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
            molly_age=False, barra=barra, cena_num=cena_num)

    # NOITE
    frames_noite = cap.get("frames", [])
    cenas = cap.get("cenas", {})
    dados_cena = cenas.get(cena_num)

    if not dados_cena:
        return redirect(url_for("final"))

    frame_idx_cena = dados_cena.get("frame_idx", 0)
    frame_atual = frames_noite[frame_idx_cena] if frame_idx_cena < len(frames_noite) else None
    age = molly_age_sozinha(cap_id, cena_num, barra)

    return render_template("cena.html",
        cap_id=cap_id, tipo="noite", trilha=trilha,
        frame=frame_atual, frame_idx=frame_idx,
        total_frames=len(cenas), imagem_mudou=True,
        tem_escolhas=True, dados=dados_cena,
        molly_age=age, barra=barra, cena_num=cena_num,
        sfx_base="/static/journey/ato_1/Cap_2(noite)/Sound/")


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


@app.route("/iniciar_cap")
def iniciar_cap():
    return redirect(url_for("cena"))


@app.route("/escolha/<int:opcao>")
def escolha(opcao):
    cap_id   = session.get("cap")
    cena_num = session.get("cena", 1)
    barra    = session.get("barra", 3)

    nova_barra, acao = processar_escolha(cap_id, cena_num, opcao, barra)
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


@app.route("/final")
def final():
    barra = session.get("barra", 3)
    dados = get_final(barra)
    return render_template("final.html", dados=dados)


@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
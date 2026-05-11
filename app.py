# app.py
from flask import Flask, render_template, session, redirect, url_for, jsonify
from game_logic import (
    get_capitulo, get_proximo_capitulo,
    processar_escolha, molly_age_sozinha, get_final
)

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
    cap_id = session.get("cap", "ato1_cap1_dia")
    frame_idx = session.get("frame", 0)
    barra = session.get("barra", 3)
    cena_num = session.get("cena", 1)

    cap = get_capitulo(cap_id)
    if not cap:
        return redirect(url_for("index"))

    frames = cap.get("frames", [])
    total_frames = len(frames)

    # Frame atual
    frame_atual = frames[frame_idx] if frame_idx < total_frames else None

    # Capítulo de dia — só passa frames, sem escolhas
    if not cap.get("tem_escolhas"):
        return render_template(
            "cena.html",
            cap_id=cap_id,
            tipo=cap.get("tipo"),
            trilha=cap.get("trilha"),
            frame=frame_atual,
            frame_idx=frame_idx,
            total_frames=total_frames,
            tem_escolhas=False,
            dados=None,
            molly_age=False,
            barra=barra,
            cena_num=cena_num,
        )

    # Capítulo de noite — tem escolhas
    cenas = cap.get("cenas", {})
    dados_cena = cenas.get(cena_num)

    if not dados_cena:
        return redirect(url_for("final"))

    age = molly_age_sozinha(cap_id, cena_num, barra)

    return render_template(
        "cena.html",
        cap_id=cap_id,
        tipo=cap.get("tipo"),
        trilha=cap.get("trilha"),
        frame=frame_atual,
        frame_idx=frame_idx,
        total_frames=total_frames,
        tem_escolhas=True,
        dados=dados_cena,
        molly_age=age,
        barra=barra,
        cena_num=cena_num,
    )


@app.route("/avancar_frame")
def avancar_frame():
    """Avança frame no capítulo de dia."""
    cap_id = session.get("cap", "ato1_cap1_dia")
    frame_idx = session.get("frame", 0)
    cap = get_capitulo(cap_id)

    if not cap:
        return redirect(url_for("index"))

    total = len(cap.get("frames", []))
    proximo_frame = frame_idx + 1

    if proximo_frame >= total:
        # Acabou o capítulo — vai para transição
        proximo_cap = get_proximo_capitulo(cap_id)
        if proximo_cap:
            session["cap"] = proximo_cap
            session["frame"] = 0
            session["cena"] = 1
            cap_proximo = get_capitulo(proximo_cap)
            tipo_proximo = cap_proximo.get("tipo") if cap_proximo else "noite"
            return redirect(url_for("transicao", tipo=tipo_proximo))
        else:
            return redirect(url_for("final"))
    else:
        session["frame"] = proximo_frame
        return redirect(url_for("cena"))


@app.route("/transicao/<tipo>")
def transicao(tipo):
    """Tela de transição DIA/NOITE."""
    return render_template("transicao.html", tipo=tipo)


@app.route("/iniciar_cap")
def iniciar_cap():
    """Inicia o capítulo após a transição."""
    return redirect(url_for("cena"))


@app.route("/escolha/<int:opcao>")
def escolha(opcao):
    cap_id = session.get("cap")
    cena_num = session.get("cena", 1)
    barra = session.get("barra", 3)

    nova_barra = processar_escolha(cap_id, cena_num, opcao, barra)
    session["barra"] = nova_barra

    cap = get_capitulo(cap_id)
    cenas = cap.get("cenas", {}) if cap else {}
    proxima = cena_num + 1

    if proxima not in cenas:
        return redirect(url_for("final"))

    session["cena"] = proxima
    return redirect(url_for("cena"))


@app.route("/avancar")
def avancar():
    """Molly agiu sozinha — avança sem escolha."""
    cap_id = session.get("cap")
    cena_num = session.get("cena", 1)
    cap = get_capitulo(cap_id)
    cenas = cap.get("cenas", {}) if cap else {}
    proxima = cena_num + 1

    if proxima not in cenas:
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
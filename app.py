# app.py
from flask import Flask, render_template, session, redirect
from game_logic import sortear_abertura, get_barra_inicial

app = Flask(__name__)
app.secret_key = "molly2026"

@app.route("/")
def index():
    vezes = session.get("vezes_zerado", 0)
    return render_template("index.html", vezes=vezes)

@app.route("/jogar")
def jogar():
    abertura = sortear_abertura()
    session["abertura"] = abertura
    session["cena"] = 1
    session["barra"] = get_barra_inicial(abertura)
    return redirect("/cena")

@app.route("/cena")
def cena():
    return render_template("cena.html")

@app.route("/escolha/<int:opcao>")
def escolha(opcao):
    return redirect("/cena")

@app.route("/final")
def final():
    return render_template("final.html")

@app.route("/reiniciar")
def reiniciar():
    vezes = session.get("vezes_zerado", 0)
    session.clear()
    session["vezes_zerado"] = vezes + 1
    return redirect("/")

@app.route("/sobre")
def sobre():
    return render_template("index.html")

@app.route("/creditos")
def creditos():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask

app_web = Flask(__name__)

@app_web.route("/")
def inicio():
    return "Página Inicial"

@app_web.route("/ola")
def raiz():
    return "Olá, turma!!!"

if __name__ == "__main__":
    app_web.run(host="127.0.0.1", port=5000, debug=True)
    # app_web.run(debug=True)
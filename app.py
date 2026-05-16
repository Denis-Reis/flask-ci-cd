from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "Minha Aplicação Flask")
    return f"<h1>{app_name}! And Hello CI/CD</h1>"

@app.route("/saudacao")
def saudacao():
    return "Olá, Deninho!"

if __name__ == "__main__":
    app.run(host="0.0.0", port=5000)
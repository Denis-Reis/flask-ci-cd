import pytest, sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

def test_home_route():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert "Minha Aplicação Flask! And Hello CI/CD" in response.text

def test_404_route():

    tester = app.test_client()
    response = tester.get("/rota-inexistente")
    assert response.status_code == 404

def test_env_variable(monkeypatch):
    monkeypatch.setenv("APP_NAME", "Teste Flask")
    tester = app.test_client()
    response = tester.get("/")
    assert "Teste Flask" in response.text

def test_saudacao_route():
    tester = app.test_client()
    response = tester.get("/saudacao")
    assert response.status_code == 200
    assert "Olá, Deninho!" in response.text




# Flask CI/CD App 🚀

Este é um projeto de exemplo utilizando **Flask** com integração contínua (CI) e entrega contínua (CD) configurados via **GitHub Actions**.

## 📂 Estrutura do projeto
- `app.py` → aplicação Flask principal
- `tests/` → testes automatizados com Pytest
- `requirements.txt` → dependências do projeto
- `.github/workflows/ci-cd.yml` → pipeline CI/CD

## ⚙️ Funcionalidades
- Servidor web simples em Flask
- Testes automatizados com Pytest
- Linting com Flake8 (PEP8)
- Pipeline CI/CD no GitHub Actions
- Build de imagem Docker

## 🚀 Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd SEU_REPOSITORIO

2. Crie e ative um ambiente virtual

    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

3. Instale as dependências

    pip install -r requirements.txt

4. Rode a aplicação

    python app.py

    - Acesse em: http://localhost:5000 

🧪 Rodando os testes

pytest


🐳 Docker
Para criar a imagem Docker (quando tiver Docker instalado):
docker build -t flask-app .
docker run -d -p 5000:5000 flask-app


🔄 CI/CD Pipeline

O pipeline roda automaticamente em cada push na branch main:

- ✅ Instala dependências
- ✅ Checa estilo com Flake8
- ✅ Executa testes com Pytest
- ✅ Faz build da imagem Docker

Status do pipeline
https://github.com/SEU_USUARIO/SEU_REPOSITORIO/actions/workflows/ci-cd.yml/badge.svg

📌 Conclusão

Este projeto demonstra como integrar Flask + Pytest + Flake8 + Docker em um pipeline CI/CD com GitHub Actions.

Ele serve como base para projetos maiores e pode ser facilmente estendido para deploy em serviços como Heroku, AWS, Azure ou Docker Hub.




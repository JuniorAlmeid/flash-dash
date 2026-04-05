# ⚡📊 Flash-Dash

O **Flash-Dash** é um projeto universitário focado na democratização do Business Intelligence (BI). O sistema automatiza processos de dados para oferecer dashboards ágeis e de baixo custo, ideal para **Pequenas e Médias Empresas (PMEs)** e **Analistas de Dados**.

---

## 🛠️ Stack Tecnológica

* **Front-End:** [Flutter](https://flutter.dev/) (UI/UX Responsivo)
* **Back-End:** [Python](https://www.python.org/) com [FastAPI](https://fastapi.tiangolo.com/) (Motor de BI)
* **Banco de Dados:** [Supabase](https://supabase.com/) (Backend-as-a-Service)

---

## 📂 Estrutura do Repositório (Monorepo)

* `core/backend`: Motor de processamento em Python e API REST.
* `core/frontend`: Interface mobile/web em Flutter.
* `docs/`: Requisitos, cronogramas e documentação acadêmica.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.12+
* Flutter SDK
* Git

### 🐍 Configurando o Back-End (Motor de BI)
1. Acesse a pasta: `cd backend`
2. Crie o ambiente virtual: `python -m venv .venv`
3. Ative o ambiente: `.\.venv\Scripts\activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Inicie o servidor: `uvicorn src.main:app --reload`
   * Acompanhe a documentação automática em: `http://127.0.0.1:8000/docs`

### 💙 Configurando o Front-End (Flutter)
1. Acesse a pasta: `cd frontend`
2. Obtenha os pacotes: `flutter pub get`
3. Execute o app: `flutter run`

---

## 🔌 Documentação da API (Endpoints)

O motor utiliza o padrão **OpenAPI (Swagger)**.
* `GET /`: Status geral do sistema.
* `GET /api/v1/health`: Verificação de saúde para QA.

---

## 👥 Equipe e Stakeholders

| Nome | Função | Responsabilidades |
| :--- | :--- | :--- |
| **Rogério Bruno** | Gerente de Projeto / Líder Técnico | Arquitetura, Motor de BI e Integração. |
| **Amanda Evellin** | Desenvolvedora Front-End | UI/UX e Componentes Visuais. |
| **Pedro Enrique** | QA - Analista de Testes | Qualidade e Testes Automatizados. |
| **Ronnison Reges** | Professor Orientador | Acompanhamento Metodológico e Avaliação. |

---
*Status: 🟢 Estrutura Base e API Inicial Concluídas.*
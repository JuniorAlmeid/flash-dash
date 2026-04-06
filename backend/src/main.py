from fastapi import FastAPI, File, UploadFile
from tratamento_dados import limparPlanilha
from ia_service import analisar_dados_com_ia
from db_repository import save # ou 'save' como estava no seu
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Adicionando o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que qualquer HTML acesse sua API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analisar-planilha")
async def analisar_rota(arquivo: UploadFile = File(...)):
    
    # 1. Lemos os bytes do arquivo enviado pelo usuário
    conteudo = await arquivo.read()
    
    # 2. Enviamos os bytes e o nome para a função do seu colega
    dados_limpos = limparPlanilha(conteudo, arquivo.filename)
    
    # Se der erro na leitura da planilha, já paramos por aqui
    if dados_limpos["status"] == "error":
        return dados_limpos
    
    # 3. Analisamos com a IA
    texto_resultado = analisar_dados_com_ia(dados_limpos)

    # 4. Salvamos no banco
    save(dados_limpos, texto_resultado)
    
    # 5. Retornamos tudo para o front-end (A IA + Os dados do gráfico)
    return {
        "status": "sucesso",
        "insight_da_ia": texto_resultado,
        "dados_planilha": dados_limpos # O Flutter vai usar isso aqui para desenhar a tela
    }


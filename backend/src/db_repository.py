from supabase import create_client, Client
import json

SUPABASE_URL = "https://qookuziywrysqfzofyve.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFvb2t1eml5d3J5c3Fmem9meXZlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3Mjc3ODkwMCwiZXhwIjoyMDg4MzU0OTAwfQ.UaFmjY5urj5GkeB8-ZZrehdxK1jCWSPuBQVFd6jMzaQ"

supabase_db: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save (dados_json, insight_texto):
    try:
        novo_registro = {
            "data_json": dados_json, 
            "ia_response": insight_texto
        }
        
        # Fazemos o INSERT na tabela 'analises'
        resposta = supabase_db.table("analises").insert(novo_registro).execute()
        
        print("--- Salvo no Supabase com sucesso!")
        return True
        
    except Exception as e:
        print(f"--- Erro ao salvar no banco: {e}")
        return False
import google.generativeai as genai
import json


#secretflashdash123
genai.configure(api_key="AIzaSyDwN6azkhz8Dw9XwiQuHSfyFbDWcFhYWK4")
modelo = genai.GenerativeModel('gemini-2.5-flash')

#função principal
def analisar_dados_com_ia(dados_json):
    print("---Enviando dados para o Gemini pensar...\n")
    
    # Transformamos o dicionário em um texto formatado para a IA ler melhor
    dados_texto = json.dumps(dados_json, indent=2, ensure_ascii=False)
    
    # O Prompt: Aqui é onde você "programa" o comportamento da IA
    # O Prompt: Aqui é onde você "programa" o comportamento da IA
    prompt = f"""
    Você é um consultor de negócios conversando diretamente com o gerente da empresa. 
    Vou te passar um resumo de dados de performance.
    
    Sua tarefa:
    1. Analise os valores numéricos e categorias no campo 'chart_data'.
    2. Escreva 1 ou 2 parágrafos curtos com insights de negócios focados em resultados (ex: destaque quem são os maiores geradores de valor, qual a proporção do total, etc).
    3. Fale de forma entusiasmada, direta e profissional.
    
    REGRAS ESTRITAS:
    - NUNCA mencione a qualidade dos dados, formatação, erros de digitação ou espaços em branco. 
    - Se notar nomes duplicados por erro de digitação (ex: "ARLINDO" e "ARLINDO "), some os valores mentalmente e gere o insight sobre o total, sem explicar que fez isso.
    - Não use jargões técnicos e não mencione termos como "JSON", "planilha" ou "dados que você me enviou".
    
    Aqui estão os dados:
    {dados_texto}
    """
    
    # Fazendo a mágica acontecer
    resposta = modelo.generate_content(prompt)
    
    return resposta.text


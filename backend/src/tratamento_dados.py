import pandas as pd
import io

def limparPlanilha(conteudo_arquivo, nome_arquivo):
    try:
        # 1. Leitura do arquivo vindo da memória
        if nome_arquivo.endswith('.csv'):
            df_raw = pd.read_csv(io.BytesIO(conteudo_arquivo), sep=None, engine='python', header=None)
        else:
            df_raw = pd.read_excel(io.BytesIO(conteudo_arquivo), header=None)

        # 2. Auto-Cleaning (A lógica excelente do seu colega)
        primeira_linha_valida_idx = df_raw.dropna(how='all').index[0]
        novos_nomes_colunas = df_raw.iloc[primeira_linha_valida_idx]
        df = df_raw.iloc[primeira_linha_valida_idx + 1:].copy()
        df.columns = novos_nomes_colunas
        df = df = df.dropna(how='all').reset_index(drop=True)
        df = df[~df.iloc[:, 0].astype(str).str.lower().str.contains('total')]
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

        def tratar_moeda_br(valor):
            if isinstance(valor, str) and 'R$' in valor:
                return float(valor.replace('R$', '').replace('.', '').replace(',', '.').strip())
            return valor

        for col in df.columns:
            df[col] = df[col].apply(tratar_moeda_br)

        # 3. Preparando os dados para o Frontend (Automatizando o Gráfico)
        colunas_categoricas = df.select_dtypes(include=['object']).columns.tolist()
        colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        chart_data = []
        if colunas_categoricas and colunas_numericas:
            dimensao = colunas_categoricas[0] # Ex: Pega a coluna "Vendedor"
            metrica = colunas_numericas[0]    # Ex: Pega a coluna "Valor"

            # Agrupa, soma e pega os 5 maiores para não quebrar o gráfico do Flutter
            df_grouped = df.groupby(dimensao)[metrica].sum().reset_index()
            df_grouped = df_grouped.sort_values(by=metrica, ascending=False).head(5)

            cores = ["#1E293B", "#748AA1", "#3B82F6", "#10B981", "#F59E0B"] # Cores combinando com seu app

            for i, row in df_grouped.iterrows():
                chart_data.append({
                    "label": str(row[dimensao]),
                    "value": float(row[metrica]),
                    "color": cores[i % len(cores)]
                })

        # 4. Retornando no formato JSON exato que você estabeleceu
        return {
            "status": "success",
            "summary": {
                "total_rows": len(df),
                "cleaned_columns": list(df.columns)
            },
            "chart_data": chart_data
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}



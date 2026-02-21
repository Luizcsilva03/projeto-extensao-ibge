import pandas as pd
import os

def analisar_distritos():
    # Caminho do arquivo gerado pelo extrator
    caminho_arquivo = os.path.join("data", "distritos_sp.csv")
    
    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo {caminho_arquivo} não encontrado. Rode o extrator_ibge.py primeiro.")
        return

    print("Carregando os dados locais do IBGE...\n")
    # Lendo o CSV transformando em um DataFrame (tabela)
    df = pd.read_csv(caminho_arquivo)
    
    print(f"📊 Total de distritos mapeados em São Paulo: {len(df)}")
    
    # Filtrando apenas os distritos alvo do seu projeto de extensão
    alvos = ['Vila Maria', 'Vila Guilherme']
    df_alvo = df[df['Nome_Distrito'].isin(alvos)]
    
    print("\n🎯 === Foco do Projeto de Extensão ===")
    if not df_alvo.empty:
        print(df_alvo.to_string(index=False))
    else:
        print("Distritos alvo não encontrados na base.")
        
    print("\n📝 Estrutura da base de dados:")
    print(df.dtypes)

if __name__ == "__main__":
    analisar_distritos()
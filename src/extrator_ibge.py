import requests
import pandas as pd
import os

class ExtratorIBGE:
    def __init__(self):
        # API de Localidades do IBGE - Extremamente estável
        # Busca todos os distritos do município de São Paulo (código 3550308)
        self.url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3550308/distritos"
        self.pasta_destino = "data"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"
        }

    def buscar_dados(self):
        print("Iniciando requisição à API de Localidades do IBGE...")
        try:
            # Adicionado um timeout de 10 segundos como boa prática de backend
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status() 
            dados_json = response.json()
            
            if not dados_json or len(dados_json) == 0:
                print("Aviso: O IBGE não retornou dados.")
                return None
                
            print("✅ Dados dos distritos de SP recebidos com sucesso!")
            return dados_json
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None

    def transformar_e_salvar(self, dados_json, nome_arquivo="distritos_sp.csv"):
        if not dados_json:
            print("Sem dados para processar.")
            return

        print("Transformando dados em DataFrame...")
        try:
            linhas = []
            for distrito in dados_json:
                nome = distrito.get('nome', '')
                id_distrito = distrito.get('id', '')
                
                # Extraindo o nome da microrregião para enriquecer o dado
                microrregiao = distrito.get('municipio', {}).get('microrregiao', {}).get('nome', 'São Paulo')

                linhas.append({
                    'ID_Distrito': id_distrito,
                    'Nome_Distrito': nome,
                    'Regiao': microrregiao
                })

            df = pd.DataFrame(linhas)
            
            # Garantir que a pasta data existe
            os.makedirs(self.pasta_destino, exist_ok=True)
            caminho_completo = os.path.join(self.pasta_destino, nome_arquivo)
            
            # Salvando o CSV
            df.to_csv(caminho_completo, index=False, encoding='utf-8')
            print(f"✅ Arquivo salvo com sucesso em: {caminho_completo}")
            
            # Destacando a Vila Maria e Vila Guilherme se estiverem nos dados
            vilas = df[df['Nome_Distrito'].str.contains('Vila Maria|Vila Guilherme', na=False, case=False)]
            if not vilas.empty:
                print("\n🎯 Distritos alvo localizados na base de dados:")
                print(vilas[['ID_Distrito', 'Nome_Distrito']].to_string(index=False))

        except Exception as e:
            print(f"Erro ao processar o JSON: {e}")

if __name__ == "__main__":
    extrator = ExtratorIBGE()
    dados_brutos = extrator.buscar_dados()
    extrator.transformar_e_salvar(dados_brutos)
    
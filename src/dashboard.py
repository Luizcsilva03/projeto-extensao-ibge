import streamlit as st
import pandas as pd
import numpy as np
import os

# Configuração da página
st.set_page_config(page_title="Dashboard - Comércio Local", layout="wide")

def carregar_dados_ibge():
    caminho = os.path.join("data", "distritos_sp.csv")
    if os.path.exists(caminho):
        return pd.read_csv(caminho)
    return pd.DataFrame()

# 1. Cabeçalho da Dashboard
st.title("📊 Análise Comercial: Vila Maria & Vila Guilherme")
st.markdown("Projeto de Extensão - Capacitação de Microempreendedores Locais baseado em Dados do IBGE.")

# 2. Carregando dados reais do IBGE (que você extraiu)
df_distritos = carregar_dados_ibge()

if not df_distritos.empty:
    alvos = ['Vila Maria', 'Vila Guilherme']
    df_alvo = df_distritos[df_distritos['Nome_Distrito'].isin(alvos)]
    
    st.sidebar.header("📍 Região de Análise")
    st.sidebar.dataframe(df_alvo[['ID_Distrito', 'Nome_Distrito']], hide_index=True)

# 3. Simulando dados de Vendas do Comércio Local para a Oficina
st.subheader("🛒 Perfil de Consumo vs. Faturamento (Exemplo Prático para a Oficina)")
st.write("Estes gráficos cruzam tendências de consumo local com o fluxo de vendas para auxiliar na tomada de decisão dos empresários.")

col1, col2 = st.columns(2)

# Gráfico 1: Vendas por Dia da Semana (Simulado)
with col1:
    st.markdown("**Faturamento Médio por Dia da Semana (R$)**")
    dias_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    vendas = [1200, 1500, 1400, 1800, 2500, 3100, 900] # Pico no fim de semana
    df_vendas = pd.DataFrame({'Dias': dias_semana, 'Faturamento': vendas})
    st.bar_chart(df_vendas.set_index('Dias'))

# Gráfico 2: Perfil Etário do Consumidor da Região (Simulado)
with col2:
    st.markdown("**Distribuição do Público-Alvo na Região (%)**")
    faixas = ['18-25 anos', '26-35 anos', '36-50 anos', '51+ anos']
    percentuais = [15, 35, 30, 20]
    df_idade = pd.DataFrame({'Faixa Etária': faixas, 'Percentual': percentuais})
    # Streamlit desenha gráficos de linha nativamente muito bem
    st.line_chart(df_idade.set_index('Faixa Etária'))

# 4. Insights Automáticos
st.info("💡 **Insight para o Lojista:** O maior volume de vendas ocorre às sextas e sábados. Sabendo que 65% do público da região tem entre 26 e 50 anos, promoções de fim de semana devem ser focadas em produtos de maior valor agregado para famílias e trabalhadores locais.")
# 📊 Projeto de Extensão: Análise de Dados para Microempreendedores

Este repositório contém o código-fonte desenvolvido para o trabalho de extensão universitária do curso de Análise e Desenvolvimento de Sistemas. 

O projeto visa extrair, processar e analisar dados demográficos do **IBGE** para auxiliar micro e pequenas empresas da região da **Vila Guilherme e Vila Maria (São Paulo/SP)** na tomada de decisões estratégicas e compreensão do mercado local.

## 🎯 Objetivo
Automatizar a extração de dados públicos (Censo Demográfico e Indicadores de Renda) consumindo a API do IBGE (SIDRA) utilizando Python, criando uma base sólida para a construção de painéis (Dashboards) voltados para empresários locais.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Bibliotecas:** `pandas` (para manipulação de dados), `requests` (para consumo de API REST)
* **Fonte de Dados:** API de Dados Agregados do IBGE

## 📁 Estrutura do Projeto
* `src/extrator_ibge.py`: Classe responsável por realizar requisições HTTP na API do IBGE e salvar os dados processados em formato `.csv`.
* `src/analise.py`: Script para leitura e análise exploratória inicial dos dados extraídos.
* `data/`: Diretório destinado ao armazenamento local dos datasets gerados (ignorado pelo versionamento por boas práticas).

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Luizcsilva03/projeto-extensao-ibge.git](https://github.com/Luizcsilva03/projeto-extensao-ibge.git)
   cd projeto-extensao-ibge
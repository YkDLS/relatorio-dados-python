# relatorio-dados-python

# 📊 Dashboard de Análise de Salários - Data Science & Tech

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://relatorio-dados-python13-2026.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Graphs-orange)

Este projeto é um dashboard interativo desenvolvido para explorar e analisar tendências salariais globais na área de Dados e Tecnologia. Utilizando dados reais de 2020 a 2025, a aplicação oferece insights sobre remuneração por cargo, senioridade, localização e modelo de trabalho.

🔗 **Acesse o Dashboard Online:** [Clique aqui para visualizar](https://relatorio-dados-python13-2026.streamlit.app/)

---

## 🖼️ Visualização do Projeto

#KPIS
<img width="1053" height="392" alt="image" src="https://github.com/user-attachments/assets/8990c0d8-03ba-4cc2-8253-3c127a0307ef" />

Gráficos 1 e 2
<img width="1343" height="527" alt="Grafico12" src="https://github.com/user-attachments/assets/91f65e1a-accd-4e98-bf78-dc24bfa66c54" />

#Gráficos 3 e 4
<img width="1055" height="439" alt="image" src="https://github.com/user-attachments/assets/b9096973-da0e-4134-ab72-21aa3c0af141" />

#tabela de Dados e Filtros
<img width="1346" height="517" alt="image" src="https://github.com/user-attachments/assets/53d4bf8b-9c05-4332-9ec5-9fb7efb7da6c" />

---

## 🚀 Funcionalidades Principais

### 1. 🌍 Média Salarial Global (Cientistas de Dados)
Um mapa interativo focado na remuneração de **Cientistas de Dados** ao redor do mundo.
- **Cor:** A intensidade da cor representa a média salarial em Dólares (USD) para este cargo específico.
- **Interatividade:** Permite comparar rapidamente quais países oferecem as melhores médias para a profissão de Data Scientist.
- **Filtro Automático:** O gráfico isola os dados de "Data Scientist" para garantir uma comparação justa entre as regiões.

### 2. 🔄 Tradução Inteligente de Cargos
Os dados originais continham centenas de variações de nomes em inglês. Foi desenvolvido um algoritmo de **processamento de texto** para padronizar e traduzir os cargos para o português:
- **Tradução Exata:** Mapeamento direto para cargos comuns (ex: *Data Scientist* → *Cientista de Dados*).
- **Lógica de Inversão e Sufixos:** Identificação dinâmica de estruturas como *"Lead X Engineer"* para transformar corretamente em *"Líder Engenheiro de X"*.
- **Correção Gramatical:** Ajustes automáticos de preposições e gêneros.

### 3. 📈 Análise de Top Cargos
- Ranking dos 10 cargos com as maiores médias salariais anuais.
- Valores convertidos e formatados em Dólar (USD).

### 4. 🔎 Exploração Detalhada
- Tabela interativa com todos os registros brutos.
- Filtros dinâmicos na barra lateral (Ano, Nível de Experiência, etc.).

---

## 🛠️ Tecnologias Utilizadas

- **Python:** Linguagem principal.
- **Streamlit:** Framework para criação do web app interativo.
- **Pandas:** Manipulação, limpeza e tratamento dos dados (ETL).
- **Plotly Express:** Criação de gráficos dinâmicos e mapas interativos.

---

## 📂 Estrutura do Projeto

```bash
/
├── app.py                  # Código principal da aplicação (Frontend + Lógica)
├── dados-imersao-final.csv # Base de dados processada
├── requirements.txt        # Lista de dependências
├── README.md               # Documentação do projeto

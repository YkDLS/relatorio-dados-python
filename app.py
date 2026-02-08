import streamlit as st
import pandas as pd
import plotly.express as px 

#Defini o titulo, icone e layout da página
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",    
    layout="wide"
)

# Carregando os dados
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

def traduzir_cargo(titulo):
    # 1. Dicionário de Tradução EXATA (Mapeamento Direto)
    # Coloque aqui os cargos que aparecem no seu Top 10 para ficarem perfeitos
    mapa_exato = {
        'Data Scientist': 'Cientista de Dados',
        'Data Engineer': 'Engenheiro de Dados',
        'Data Analyst': 'Analista de Dados',
        'Machine Learning Engineer': 'Engenheiro de Machine Learning',
        'Analytics Engineer': 'Engenheiro de Analytics',
        'Research Scientist': 'Cientista Pesquisador',
        'Applied Scientist': 'Cientista Aplicado',
        'Research Team Lead': 'Líder de Equipe de Pesquisa',
        'Analytics Engineering Manager': 'Gerente de Eng. de Analytics',
        'Data Science Tech Lead': 'Líder Técnico de Data Science',
        'Applied AI ML Lead': 'Líder de IA Aplicada e ML',
        'Head of Applied AI': 'Chefe de IA Aplicada',
        'Head of Machine Learning': 'Chefe de Machine Learning',
        'Machine Learning Performance Engineer': 'Eng. de Performance em ML',
        'Director of Product Management': 'Diretor de Gestão de Produtos',
        'Engineering Manager': 'Gerente de Engenharia',
        'AWS Data Architect': 'Arquiteto de Dados AWS',
        'AI Scientist': 'Cientista de IA',
        'Big Data Engineer': 'Engenheiro de Big Data',
        'Computer Vision Engineer': 'Engenheiro de Visão Computacional',
        'NLP Engineer': 'Engenheiro de NLP',
        'Solutions Engineer': 'Engenheiro de Soluções',
        'Systems Engineer': 'Engenheiro de Sistemas',
        'Associate': 'Associado',
        'Data Specialist' : 'Especialista de Dados'
    }
    
    # Se o cargo estiver na lista exata, retorna ele pronto
    if titulo in mapa_exato:
        return mapa_exato[titulo]   
    
    # 
    titulo = titulo.replace('Engineering', 'Engenharia') # Corrige o bug "Engenheiroing"
    titulo = titulo.replace('Science', 'Ciência')
    
    # Tradução dos comuns
    traducoes = {
        'Engineer': 'Engenheiro',
        'Scientist': 'Cientista',
        'Analyst': 'Analista',
        'Manager': 'Gerente',
        'Director': 'Diretor',
        'Lead': 'Líder',
        'Head': 'Chefe',
        'Architect': 'Arquiteto',
        'Consultant': 'Consultor',
        'Research': 'Pesquisa',
        'Applied': 'Aplicado'
    }
    
    for en, pt in traducoes.items():
        titulo = titulo.replace(en, pt)
        
    return titulo

# Aplica a nova função
df['cargo'] = df['cargo'].apply(traduzir_cargo)

#               Filtros
st.sidebar.header("🔍 Filtros")

#Ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

# Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

# Tipo de Contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

# Tamanho da Empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)


#Filtro dentro do DataFrame

df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados)) 
]

#Conteudo da Pagina Principal

st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

#Kpis
st.subheader("Métricas Gerais (Salário Anual em U$D)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio,salario_mediano,salario_maximo, total_registros,cargo_mais_comum = 0,0,0,""


col1,col2,col3,col4 = st.columns(4)
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

# Analise dos Visuais

st.subheader("Gráficos")

col_graf1,col_graf2 = st.columns(2)

#Top 10 cargos com maior salario
with col_graf1:
    # Aqui vai o código do seu gráfico (ex: st.plotly_chart(fig))
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby("cargo")['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation="h",
            title="Top 10 cargos por Salário Médio",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
        )
        grafico_cargos.update_layout(title_x=0.1,yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
         st.warnig("Nenhum dado para exibir no gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title='Distribuição de salários anuais',
            labels={'usd': 'Faixa salarial (USD)', 'count': ' '}
        )
        # ESTAS DUAS LINHAS ABAIXO PRECISAM DE MAIS RECUO:
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

    # Criando a colunas para a terceira linha
col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos Tipos de Trabalho',
            hole=0.5
        )
        
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)     
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with col_graf4:

    # Verifica se há dados filtrados
    if not df_filtrado.empty:
        
        # Calcula a média de TODOS os cargos no país
        pais_stats = df_filtrado.groupby('residencia_iso3')['usd'].agg(['mean', 'count']).reset_index()
        pais_stats.columns = ['residencia_iso3', 'media_salarial_pais', 'qtd_profissionais']

        # 2. Identificando o "Cargo de Maior Valor" por País
        # Agrupa por País e Cargo, calcula a média e ordena
        cargo_stats = df_filtrado.groupby(['residencia_iso3', 'cargo'])['usd'].mean().reset_index()
        cargo_stats = cargo_stats.sort_values(['residencia_iso3', 'usd'], ascending=[True, False])
        
        # Pega apenas o primeiro registro (o maior salário) de cada país
        top_cargos = cargo_stats.drop_duplicates(subset=['residencia_iso3'])
        top_cargos = top_cargos[['residencia_iso3', 'cargo', 'usd']]
        top_cargos.columns = ['residencia_iso3', 'cargo_top', 'media_cargo_top']

        # 3. Juntando as informações
        dados_mapa = pd.merge(pais_stats, top_cargos, on='residencia_iso3')

        # 4. Criando o Gráfico
        fig = px.choropleth(
            dados_mapa,
            locations='residencia_iso3',      # Código ISO do país
            color='media_salarial_pais',      # Cor baseada na média geral do país
            hover_name='residencia_iso3',     # Título do tooltip
            hover_data={
                'residencia_iso3': False,     # Oculta o ISO no tooltip (já está no título)
                'media_salarial_pais': ':$.2f', # Formata moeda
                'cargo_top': True,            # Mostra o cargo top
                'media_cargo_top': ':$.2f',   # Mostra o salário do cargo top
                'qtd_profissionais': True     # Mostra quantos dados temos (bom pra contexto)
            },
            color_continuous_scale='Viridis', # Escala de cor profissional
            title='Média Salarial Global e Cargo Mais Valorizado por País'
        )

        # Ajustes visuais
        fig.update_layout(
            title_x=0, # Alinhado à esquerda como padrão moderno
            margin=dict(l=0, r=0, t=50, b=0), # Remove bordas brancas
            geo=dict(showframe=False, showcoastlines=False, projection_type='equirectangular')
        )
        
        # Melhorando os rótulos do tooltip
        fig.update_traces(
            hovertemplate="<b>%{hovertext}</b><br><br>" +
            "Média Geral do País: %{z:$.2f}<br>" +
            "Cargo Mais Pago: %{customdata[1]}<br>" +
            "Média do Cargo Top: %{customdata[2]:$.2f}<br>" +
            "Profissionais na base: %{customdata[3]}"
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Nenhum dado disponível para gerar o mapa.")
#Tabela com dados Detalhado

st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)



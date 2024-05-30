import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar e exibir a primeira página
def primeira_pagina():
    st.title("Show da Madonna no Rio de Janeiro")
    st.image("madonna.jpg", caption="Madonna")
    st.header("A Prefeitura do Rio e o governo investiram R$ 10 milhões cada no show da Madonna")

    with st.form(key='form1'):
        resposta = st.radio(
            "Você acha que a Prefeitura do Rio e o governo deveriam ter investido essa quantia de dinheiro no show?",
            ("Sim", "Não")
        )
        submit_button = st.form_submit_button(label='Confirmar')

    if submit_button:
        st.session_state.resposta1 = resposta
        st.session_state.pagina = 'segunda'

# Função para carregar e exibir a segunda página
def segunda_pagina():
    st.title("Impacto Econômico do Show da Madonna")
    st.image("pessoas.jpg", caption="Show da Madonna reúne 1,6 milhões de pessoas em Copacabana.")
    st.header("Show da Madonna reúne 1,6 milhões de pessoas em Copacabana.")
    
    valor_real = 300  # Valor real em milhões
    with st.form(key='form2'):
        estimativa = st.number_input(
            "Quanto você acha que o show da Madonna trouxe de retorno financeiro para o Rio de Janeiro (em milhões de reais)?",
            min_value=0, max_value=1000, step=1
        )
        submit_button = st.form_submit_button(label='Confirmar')

    if submit_button:
        st.session_state.estimativa = estimativa
        st.session_state.pagina = 'terceira'
        gerar_graficos(valor_real, estimativa)

# Função para gerar os gráficos na segunda página
def gerar_graficos(valor_real, estimativa):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfico de dispersão
    ax[0].scatter(valor_real, valor_real, color='green', label='Valor Real')
    ax[0].scatter(estimativa, estimativa, color='red', label='Sua Estimativa')
    ax[0].set_title('Dispersão das Estimativas')
    ax[0].set_xlabel('Estimativas (milhões)')
    ax[0].set_ylabel('Valor')
    ax[0].legend()

    # Gráfico de histograma
    ax[1].hist([valor_real, estimativa], bins=10, color=['green', 'red'], alpha=0.7, label=['Valor Real', 'Sua Estimativa'])
    ax[1].set_title('Distribuição das Estimativas')
    ax[1].set_xlabel('Estimativas (milhões)')
    ax[1].set_ylabel('Frequência')
    ax[1].legend()

    st.pyplot(fig)

    with st.container():
        st.header("Acredito que ficou evidente como o turismo é crucial e gera receitas significativas para o Brasil. O show da Madonna, por exemplo, demonstrou claramente o impacto econômico positivo. Você já considerou o quanto o turismo contribui para a economia brasileira de forma mais ampla. Vale destacar que os dados de 2024 são estimativas feitas com algoritmos de previsão, como o ARIMA, baseados em dados históricos?")
        col1, col2 = st.columns([2, 5])
        col1.header("Nos gráficos a seguir, você entenderá melhor como o turismo influencia a economia do Brasil")
        col2.image("carinha.jpg", width=70)

    opcoes_graficos()

# Função para carregar e exibir os gráficos baseados na escolha do usuário
def opcoes_graficos():
    opcoes = st.multiselect(
        "Escolha o gráfico que você deseja ver:",
        ["Número de Turistas no Brasil", "Despesas com Turismo no Brasil", "Retorno Financeiro do Turismo no Brasil"]
    )

    if "Número de Turistas no Brasil" in opcoes:
        df_turistas = pd.read_excel('previsao_turistas_1989_2024.xlsx')
        st.line_chart(df_turistas.set_index('Ano'))

    if "Despesas com Turismo no Brasil" in opcoes:
        df_despesas = pd.read_excel('despesas_pagas_turismo_2020_2024.xlsx')
        st.line_chart(df_despesas.set_index('Ano'))

    if "Retorno Financeiro do Turismo no Brasil" in opcoes:
        df_receita = pd.read_excel('receita_turismo_2019_2024.xlsx')
        st.line_chart(df_receita.set_index('Ano'))

    st.button("Início", on_click=inicio)

# Função para retornar à primeira página
def inicio():
    st.session_state.pagina = 'primeira'

# Configuração inicial do app
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'primeira'

# Controle de navegação entre páginas
if st.session_state.pagina == 'primeira':
    primeira_pagina()
elif st.session_state.pagina == 'segunda':
    segunda_pagina()

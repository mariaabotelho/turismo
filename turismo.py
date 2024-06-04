import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#alguns detalhes de design
def set_style():
    st.markdown(
        """
        <style>
        .stApp {
            background: url('https://raw.githubusercontent.com/mariaabotelho/turismo/main/fundo5.jpeg') no-repeat center center fixed;
            background-size: cover;
        }
        .css-1d391kg {
            background-color: rgba(255, 255, 255, 0.8);
        }
        h1, h2, h3, h4, h5, p, div, span {
            font-family: 'Times New Roman', sans-serif;
        }
        /* Estilizando as opções do multiselect */
        .stMultiSelect .css-1l6x6by, .stMultiSelect .css-1n543e5 {
            background-color: green !important;
            color: white !important;
        }
        .stMultiSelect .css-1dimb5e, .stMultiSelect .css-1ine56y, .stMultiSelect .css-1wa3eu0 {
            color: green !important;
        }
        .stMultiSelect div[role='listbox'] {
            background-color: green !important;
            color: white !important;
        }
        .stMultiSelect div[role='option'] {
            background-color: green !important;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# priemira página
def main_page():
    set_style()
    st.header("Show da Madonna no Rio de Janeiro")
    with st.container():
        st.image("madonnaof.jpg", caption="Poster de divulgação do show da Madonna no Rio de Janeiro.", width=620)
    
    st.write("A Prefeitura do Rio e o governo investiram R$ 10 milhões cada no show da Madonna.")
    
    with st.form(key='form1'):
        answer = st.radio("Você acha que a Prefeitura do Rio e o governo deveriam ter investido essa quantia de dinheiro no show?", ("Sim", "Não"))
        submit_button = st.form_submit_button(label='Confirmar')
    
    if submit_button:
        st.session_state.answer = answer
        st.experimental_rerun()

# segunda página
def second_page():
    set_style()
    with st.container():
        st.image("pessoas.jpg", caption="Foto do show da Madonna no Rio de Janeiro.", width=600)
    
    with st.container():
        st.header("Show da Madonna reuniu 1,6 milhões de pessoas em Copacabana, dos quais cerca de 150 mil eram turistas.")
        st.write("Quanto você acha que o show da Madonna trouxe de retorno financeiro para o Rio de Janeiro?")
        retorno_est = st.number_input("Insira sua estimativa (em milhões de reais)", min_value=0, step=1)
        confirmar_button = st.button("Confirmar")
    
    if confirmar_button:
        st.session_state.retorno_est = retorno_est
        st.experimental_rerun()
    
    if 'retorno_est' in st.session_state:
        real_value = 300  # Valor real do retorno financeiro
        estimativa = st.session_state.retorno_est

        # comparações com st.metric
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Valor real", value=f"{real_value} milhões de reais")
        with col2:
            st.metric(label="Sua estimativa", value=f"{estimativa} milhões de reais")

        # gráfico de proximidade da estimativa com o valor real 
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(['Sua Estimativa', 'Valor Real'], [estimativa, real_value], color='green', marker='o')
        ax.fill_between(['Sua Estimativa', 'Valor Real'], [estimativa, real_value], color='yellow', alpha=0.3)
        ax.set_ylim(0, max(estimativa, real_value) * 1.1)
        ax.set_ylabel('Milhões de reais')
        ax.set_title('Proximidade da Estimativa com o Valor Real')
        st.pyplot(fig)
        
        #container não ta funcionando
        with st.container():
            st.subheader(
                "Acredito que ficou evidente como o turismo é crucial e gera receitas significativas. O show da Madonna, por exemplo, demonstrou claramente o impacto econômico positivo. Você já considerou o quanto o turismo contribui para a economia brasileira de forma mais ampla. Nos gráficos a seguir, você entenderá melhor como o turismo influencia a economia do Brasil"
            )
            col1, col2 = st.columns([3, 1])
            with col1:
                st.caption(
                    "Vale destacar que nossos dados de 2024 são estimativas feitas com algoritmos de previsão, como o ARIMA, baseados em dados históricos"
                )
            with col2:
                st.image("carinhas.jpg", width=120)

        # multiselect p gráficos
        options = st.multiselect(
            "Escolha os gráficos que deseja visualizar:",
            ["Número de Turistas no Brasil", "Despesas com Turismo no Brasil", "Retorno Financeiro do Turismo no Brasil"]
        )

        if "Número de Turistas no Brasil" in options:
            turistas_df = pd.read_excel("turistas_brasil_2019_2024.xlsx")
            turistas_df['Ano'] = turistas_df['Ano'].astype(int)
            st.bar_chart(turistas_df.set_index("Ano")["Turistas"])

        if "Despesas com Turismo no Brasil" in options:
            despesas_df = pd.read_excel("despesas_pagas_turismo_2020_2024.xlsx")
            despesas_df['Ano'] = despesas_df['Ano'].astype(int)
            st.bar_chart(despesas_df.set_index("Ano")["Despesas Pagas (BRL)"])

        if "Retorno Financeiro do Turismo no Brasil" in options:
            receita_df = pd.read_excel("receita_turismo_2019_2024.xlsx")
            receita_df['Ano'] = receita_df['Ano'].astype(int)
            st.bar_chart(receita_df.set_index("Ano")["Receita (BRL)"])

        if st.button("Início 🏠"):
            st.session_state.clear()
            st.experimental_rerun()

# navegação entr as páginas
if 'answer' not in st.session_state:
    main_page()
else:
    second_page()

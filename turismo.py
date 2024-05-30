import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Página Inicial
def main_page():
    st.title("Show da Madonna no Rio de Janeiro")
    st.image("madonna.jpg", caption="Madonna")
    
    st.header("A Prefeitura do Rio e o governo investiram R$ 10 milhões cada no show da Madonna")
    
    with st.form(key='form1'):
        answer = st.radio("Você acha que a Prefeitura do Rio e o governo deveriam ter investido essa quantia de dinheiro no show?", ("Sim", "Não"))
        submit_button = st.form_submit_button(label='Confirmar')
    
    if submit_button:
        st.session_state.answer = answer
        st.experimental_rerun()

# Segunda Página
def second_page():
    st.image("pessoas.jpg", caption="Show da Madonna reúne 1,6 milhões de pessoas em Copacabana.")
    st.header("Show da Madonna reúne 1,6 milhões de pessoas em Copacabana.")
    
    st.write("Quanto você acha que o show da Madonna trouxe de retorno financeiro para o Rio de Janeiro?")
    
    retorno_est = st.number_input("Insira sua estimativa (em milhões de reais)", min_value=0, step=1)
    confirmar_button = st.button("Confirmar")
    
    if confirmar_button:
        st.session_state.retorno_est = retorno_est
        st.experimental_rerun()
    
    if 'retorno_est' in st.session_state:
        real_value = 300  # Valor real do retorno financeiro
        estimativas = [st.session_state.retorno_est]  # Lista para armazenar estimativas
        
        # Gráfico de dispersão
        fig, ax = plt.subplots()
        ax.scatter([1] * len(estimativas), estimativas, color='blue', label='Estimativas')
        ax.scatter([1], [real_value], color='red', label='Valor Real')
        ax.set_title('Estimativas vs Valor Real')
        ax.legend()
        st.pyplot(fig)
        
        # Histograma
        fig, ax = plt.subplots()
        ax.hist(estimativas, bins=20, color='blue', alpha=0.7, label='Estimativas')
        ax.axvline(real_value, color='red', linestyle='dashed', linewidth=2, label='Valor Real')
        ax.set_title('Distribuição das Estimativas')
        ax.legend()
        st.pyplot(fig)

        # Texto com container e imagens
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <h1 style="margin-right: 10px;">Acredito que ficou evidente como o turismo é crucial e gera receitas significativas para o Brasil. O show da Madonna, por exemplo, demonstrou claramente o impacto econômico positivo. Você já considerou o quanto o turismo contribui para a economia brasileira de forma mais ampla. Vale destacar que os dados de 2024 são estimativas feitas com algoritmos de previsão, como o ARIMA, baseados em dados históricos?</h1>
                <img src="carinha.jpg" width="70">
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <h2 style="margin-right: 10px;">Nos gráficos a seguir, você entenderá melhor como o turismo influencia a economia do Brasil</h2>
                <img src="carinha.jpg" width="70">
            </div>
            """,
            unsafe_allow_html=True
        )

        # Gráficos interativos com multiselect
        options = st.multiselect(
            "Escolha os gráficos que deseja visualizar:",
            ["Número de Turistas no Brasil", "Despesas com Turismo no Brasil", "Retorno Financeiro do Turismo no Brasil"]
        )

        if "Número de Turistas no Brasil" in options:
            turistas_df = pd.read_excel("previsao_turistas_1989_2024.xlsx")
            st.line_chart(turistas_df.set_index("Ano")["Turistas"])

        if "Despesas com Turismo no Brasil" in options:
            despesas_df = pd.read_excel("despesas_pagas_turismo_2020_2024.xlsx")
            st.line_chart(despesas_df.set_index("Ano")["Despesas Pagas (BRL)"])

        if "Retorno Financeiro do Turismo no Brasil" in options:
            receita_df = pd.read_excel("receita_turismo_2019_2024.xlsx")
            st.line_chart(receita_df.set_index("Ano")["Receita (BRL)"])

        st.button("Início", on_click=lambda: st.experimental_rerun())

# Gerenciar navegação entre páginas
if 'answer' not in st.session_state:
    main_page()
else:
    second_page()

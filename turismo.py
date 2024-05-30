import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para a página principal
def main_page():
    st.title("Show da Madonna no Rio de Janeiro")
    with st.container():
        st.image("madonna.jpg", caption="Madonna", width=600)
    
    st.header("A Prefeitura do Rio e o governo investiram R$ 10 milhões cada no show da Madonna")
    
    with st.form(key='form1'):
        answer = st.radio("Você acha que a Prefeitura do Rio e o governo deveriam ter investido essa quantia de dinheiro no show?", ("Sim", "Não"))
        submit_button = st.form_submit_button(label='Confirmar')
    
    if submit_button:
        st.session_state.answer = answer
        st.experimental_rerun()

# Função para a segunda página
def second_page():
    with st.container():
        st.image("pessoas.jpg", caption="Show da Madonna reúne 1,6 milhões de pessoas em Copacabana.", width=500)
    st.header("Show da Madonna reúne 1,6 milhões de pessoas em Copacabana.")
    
    st.write("Quanto você acha que o show da Madonna trouxe de retorno financeiro para o Rio de Janeiro?")
    
    retorno_est = st.number_input("Insira sua estimativa (em milhões de reais)", min_value=0, step=1)
    confirmar_button = st.button("Confirmar")
    
    if confirmar_button:
        st.session_state.retorno_est = retorno_est
        st.experimental_rerun()
    
    if 'retorno_est' in st.session_state:
        real_value = 300  # Valor real do retorno financeiro
        estimativa = st.session_state.retorno_est

        st.write("Sua estimativa comparada ao valor real:")
        st.write(f"Valor real: {real_value} milhões de reais")
        st.write(f"Sua estimativa: {estimativa} milhões de reais")

        # Gráfico de proximidade da estimativa com o valor real
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.barh(['Sua Estimativa', 'Valor Real'], [estimativa, real_value], color=['blue', 'green'])
        ax.set_xlim(0, max(estimativa, real_value) * 1.1)
        ax.set_xlabel('Milhões de reais')
        ax.set_title('Proximidade da Estimativa com o Valor Real')
        st.pyplot(fig)
        
        # Texto com container e imagens
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(
                    "Acredito que ficou evidente como o turismo é crucial e gera receitas significativas para o Brasil. O show da Madonna, por exemplo, demonstrou claramente o impacto econômico positivo. Você já considerou o quanto o turismo contribui para a economia brasileira de forma mais ampla. Vale destacar que os dados de 2024 são estimativas feitas com algoritmos de previsão, como o ARIMA, baseados em dados históricos?"
                )
                st.caption(
                    "Nos gráficos a seguir, você entenderá melhor como o turismo influencia a economia do Brasil"
                )
            with col2:
                st.image("carinha.jpg", width=70)

        # Gráficos interativos com multiselect
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

# Gerenciar navegação entre páginas
if 'answer' not in st.session_state:
    main_page()
else:
    second_page()

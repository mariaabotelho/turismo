import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Página Inicial
    st.set_page_config(page_title="Show da Madonna no Rio", layout="wide")

    st.title("A Prefeitura do Rio e o governo investiram R$ 10 milhões cada no show da Madonna")

    st.image("madonna.jpg", use_column_width=True)

    with st.form(key="form1"):
        resposta1 = st.radio(
            "Você acha que a Prefeitura do Rio e o governo deveriam ter investido essa quantia de dinheiro no show?",
            ("Sim", "Não")
        )
        submit_button1 = st.form_submit_button(label="Confirmar")

    if submit_button1:
        st.session_state.resposta1 = resposta1
        st.experimental_rerun()

    if "resposta1" in st.session_state:
        st.title("Show da Madonna reúne 1,6 milhões de pessoas em Copacabana.")
        st.image("pessoas.jpg", use_column_width=True)

        with st.form(key="form2"):
            resposta2 = st.number_input(
                "Quanto você acha que o show da Madonna trouxe de retorno financeiro para o Rio de Janeiro?",
                min_value=0,
                step=1
            )
            submit_button2 = st.form_submit_button(label="Confirmar")

        if submit_button2:
            st.session_state.resposta2 = resposta2
            st.experimental_rerun()

    if "resposta2" in st.session_state:
        st.title("Resultados da Estimativa")
        real_value = 300_000_000

        estimativas = [st.session_state.resposta2]
        st.write("Sua estimativa:", st.session_state.resposta2)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        
        # Gráfico de dispersão
        ax1.scatter(estimativas, [1] * len(estimativas), color="blue")
        ax1.axvline(real_value, color="red", linestyle="--")
        ax1.set_title("Dispersão das Estimativas")
        ax1.set_xlabel("Estimativas")
        ax1.set_ylabel("Frequência")

        # Histograma
        ax2.hist(estimativas, bins=10, color="blue", alpha=0.7)
        ax2.axvline(real_value, color="red", linestyle="--")
        ax2.set_title("Distribuição das Estimativas")
        ax2.set_xlabel("Estimativas")
        ax2.set_ylabel("Frequência")

        st.pyplot(fig)

        st.container()
        st.header("Acredito que ficou evidente como o turismo é crucial e gera receitas significativas para o Brasil.")
        st.subheader("Nos gráficos a seguir, você entenderá melhor como o turismo influencia a economia do Brasil")
        
        col1, col2 = st.columns([1, 9])
        with col1:
            st.image("carinha.jpg", width=70)
        with col2:
            st.write("Acredito que ficou evidente como o turismo é crucial e gera receitas significativas para o Brasil. O show da Madonna, por exemplo, demonstrou claramente o impacto econômico positivo. Você já considerou o quanto o turismo contribui para a economia brasileira de forma mais ampla. Vale destacar que os dados de 2024 são estimativas feitas com algoritmos de previsão, como o ARIMA, baseados em dados históricos?")
        
        opcoes = st.multiselect(
            "Escolha as opções para visualizar os gráficos:",
            ["Número de Turistas no Brasil", "Despesas com Turismo no Brasil", "Retorno Financeiro do Turismo no Brasil"]
        )

        if "Número de Turistas no Brasil" in opcoes:
            df_turistas = pd.read_excel("previsao_turistas_1989_2024.xlsx")
            st.line_chart(df_turistas.set_index("Ano"))

        if "Despesas com Turismo no Brasil" in opcoes:
            df_despesas = pd.read_excel("despesas_pagas_turismo_2020_2024.xlsx")
            st.line_chart(df_despesas.set_index("Ano"))

        if "Retorno Financeiro do Turismo no Brasil" in opcoes:
            df_receita = pd.read_excel("receita_turismo_2019_2024.xlsx")
            st.line_chart(df_receita.set_index("Ano"))

        if st.button("Início 🏠"):
            del st.session_state.resposta1
            del st.session_state.resposta2
            st.experimental_rerun()

if __name__ == "__main__":
    main()

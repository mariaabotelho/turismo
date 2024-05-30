import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para definir o estilo do site
def set_style():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffffff;
        }
        .css-1d391kg {
            background-color: #ffffff;
        }
        h1, h2, h3, h4, h5, h6, p, div, span {
            font-family: 'Arial', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Função para exibir a imagem e texto no container
def display_image_with_text(image_path, caption, header_text, image_width=600):
    container = st.container()
    with container:
        col_img, col_txt = container.columns([1, 2])
        col_img.image(image_path, caption=caption, width=image_width)
        col_txt.header(header_text)

# Função para exibir gráficos de barra
def display_bar_chart(file_path, column_name):
    df = pd.read_excel(file_path)
    df['Ano'] = df['Ano'].astype(int)
    st.bar_chart(df.set_index("Ano")[column_name])

# Página principal
def main_page():
    set_style()
    st.title("Show da Madonna no Rio de Janeiro")
    display_image_with_text(
        "madonna.jpg",
        "Madonna",
        "A Prefeitura do Rio e o governo investiram R$ 10 milhões cada no show da Madonna",
        image_width=600
    )
    
    with st.form(key='form1'):
        answer = st.radio("Você acha que a Prefeitura do Rio e o governo deveriam ter investido essa quantia de dinheiro no show?", ("Sim", "Não"))
        submit_button = st.form_submit_button(label='Confirmar')
    
    if submit_button:
        st.session_state.answer = answer
        st.experimental_rerun()

# Segunda página
def second_page():
    set_style()
    display_image_with_text(
        "pessoas.jpg",
        "Show da Madonna reúne 1,6 milhões de pessoas em Copacabana.",
        "Show da Madonna reúne 1,6 milhões de pessoas em Copacabana.",
        image_width=500
    )
    
    st.write("Quanto você acha que o show da Madonna trouxe de retorno financeiro para o Rio de Janeiro?")
    
    retorno_est = st.number_input("Insira sua estimativa (em milhões de reais)", min_value=0, step=1)
    confirmar_button = st.button("Confirmar")
    
    if confirmar_button:
        st.session_state.retorno_est = retorno_est
        st.experimental_rerun()
    
    if 'retorno_est' in st.session_state:
        real_value = 300
        estimativa = st.session_state.retorno_est

        st.write("Sua estimativa comparada ao valor real:")
        st.write(f"Valor real: {real_value} milhões de reais")
        st.write(f"Sua estimativa: {estimativa} milhões de reais")

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(['Sua Estimativa', 'Valor Real'], [estimativa, real_value], color='green', marker='o')
        ax.fill_between(['Sua Estimativa', 'Valor Real'], [estimativa, real_value], color='yellow', alpha=0.3)
        ax.set_ylim(0, max(estimativa, real_value) * 1.1)
        ax.set_ylabel('Milhões de reais')
        ax.set_title('Proximidade da Estimativa com o Valor Real')
        st.pyplot(fig)
        
        container = st.container()
        with container:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(
                    "Acredito que ficou evidente como o turismo é crucial e gera receitas significativas para o Brasil. O show da Madonna, por exemplo, demonstrou claramente o impacto econômico positivo. Você já considerou o quanto o turismo contribui para a economia brasileira de forma mais ampla. Nos gráficos a seguir, você entenderá melhor como o turismo influencia a economia do Brasil"
                )
            with col2:
                st.image("carinha.jpg", width=100)
            st.caption(
                "Vale destacar que os dados de 2024 são estimativas feitas com algoritmos de previsão, como o ARIMA, baseados em dados históricos"
            )

        options = st.multiselect(
            "Escolha os gráficos que deseja visualizar:",
            ["Número de Turistas no Brasil", "Despesas com Turismo no Brasil", "Retorno Financeiro do Turismo no Brasil"]
        )

        if "Número de Turistas no Brasil" in options:
            display_bar_chart("turistas_brasil_2019_2024.xlsx", "Turistas")

        if "Despesas com Turismo no Brasil" in options:
            display_bar_chart("despesas_pagas_turismo_2020_2024.xlsx", "Despesas Pagas (BRL)")

        if "Retorno Financeiro do Turismo no Brasil" in options:
            display_bar_chart("receita_turismo_2019_2024.xlsx", "Receita (BRL)")

        if st.button("Início 🏠"):
            st.session_state.clear()
            st.experimental_rerun()

# Gerenciar navegação entre páginas
if 'answer' not in st.session_state:
    main_page()
else:
    second_page()

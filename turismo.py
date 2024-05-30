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
            background-color: #f0f8ff;
        }
        h1, h2, h3, h4, h5, h6, p, div, span {
            font-family: 'Arial', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Função para a página principal
def main_page():
    set_style()
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
    set_style()
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

        # Gráfico de proximidade da estimativa com o valor real em linhas
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(['Sua Estimativa', 'Valor Real'], [estimativa, real_value], color='green', marker='o')
        ax.fill_between(['Sua Estimativa', 'Valor Real'], [estimativa, real_value], color='yellow', alpha=0.3)
        ax.set_ylim(0, max(estimativa, real_value) * 1.1)
        ax.set_ylabel('Milhões de reais')
       

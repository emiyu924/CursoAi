import streamlit as st

st.set_page_config(layout="wide")



col1, col2, col3 =st.columns(3)

with col1:
    st.image("pizza1.jpg", use_container_width=True)
    
    with col2:
        st.image("pizza2.jpg", use_container_width=True)
        
        with col3:
           st.image("pizza3.jpg", use_container_width=True)

st.title("Pizzaria Dipadre")
st.subheader("Conheça as melhores pizzas de Americana ")

st.markdown("**Faça a pesquisa e concorra a uma pizza grátis!**")

nome = st.text_input("Digite o seu nome:")
cidade = st.text_input("Digite a sua cidade:")
saborEscolhido = st.selectbox("Qual o seu sabor favorito da casa?", ["Margherita", "Quatro queijos", "Portuguesa", "Calabresa", "Frango Catupiry", "Brigadeiro", "Banana nevada"])
opcaoFinal = st.checkbox("Ao clicar aqui você Verificou as informações e confirma o sabor escolhido")


if st.button("Enviar Pesquisa"):
    if nome and cidade and saborEscolhido and opcaoFinal:
        st.success(f"Obrigada {nome} por participar da sua pesquisa! sua cidade é {cidade} você escolheu o sabor {saborEscolhido}, uma perfeita escolha!.")
        
    else:
        st.error("Ops! Algo está errado, verifique novamente se todos os dados da pesquisa foram preenchidos corretamente")
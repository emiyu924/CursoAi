import streamlit as st

st.title("Bem vindo á minha primeira página WEB")
st.subheader("Desenvolvido por Emilly")

nome = st.text_input("Digite seu nome para iniciarmos:")

if nome:
    st.success(f"Bem vindo {nome}")
    st.balloons()
    
    
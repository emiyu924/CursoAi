import streamlit as st

st.title("Bem vindo ao Cadastro RH")
st.subheader("Para começar digite seu email e senha (em caso de não ter recebido ou ter esquecido a senha, entrar em contato com o responsável pelo seu setor)")

nome = st.text_input("Digite seu nome para iniciarmos:")

if nome:
    st.success(f"Bem vindo {nome}")
    st.balloons()
    

email = st.text_input("Digite seu email:")
senha = st.text_input("Agora digite sua senha:")

if st.button("cadastrar"):

    if email and senha:
     st.success("Login efetuado com sucesso!")
    
else:
    st.error("Digite seus dados para efetuarmos o login")
    
    
    

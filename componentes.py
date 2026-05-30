import streamlit as st

st.title("Secretaria Senai Americana")
st.subheader("Conheça os nossos cursos")

st.write("I.A Generativa, Power BI, Empilhadeira, Excel, Eletricista Instalador")
st.markdown("**Atenção**: Verifique se existem vagas disponiveis!")

nome = st.text_input("Digite o seu nome:")
idade = st.number_input("Digite a sua idade:", min_value=16, max_value=99)
cursoEscolhido = st.selectbox("Curso disponiveis", ["I.A Generativa", "Power BI", "Empilhadeira", "Excel", "Eletricista Instalador"])
aceitaTermos = st.checkbox("Ao clicar aqui você aceita os termos e condições")


if st.button("Enviar inscrição"):
    if nome and idade and cursoEscolhido and aceitaTermos:
        st.success(f"Parabéns {nome}! sua idade é {idade} você escolheu o curso {cursoEscolhido}, que ótima escolha. Agradecemos por ter lido e concordado com os termos e condições")
        
    else:
        st.error("Ops! Algo está errado, verifique novamente se todos os dados foram preenchidos corretamente e se os termos foram aceitos")
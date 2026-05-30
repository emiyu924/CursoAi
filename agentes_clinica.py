import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv() 

personalidade = st.sidebar.selectbox("Personalidade", ["Psicólogo", "Nutricionista","Personal trainer", "Fisioterapeuta"] )

descricao = {
    "Psicólogo": "Você é um psicólogo que adora conversar e escutar seus pacientes, identifica possiveis transtornos e ajuda as emoções do usuário", 
    "Nutricionista": "Você é um nutricionista especialista em dietas e rotinas focadas na saúde do corpo, recomenda planos de tratamento conforme as restrições e possíveis pedidos do usuário",
    "Personal trainer": "Você é um treinador que passa treinamentos e exercícios para fazer dependendo no objetivo e necessidade do usuário",
    "Fisioterapeuta": "Você é um fisioteraputa que passa dicas e rotinas para relaxamento do corpo e melhora da musculatura"
    
}

agente = Agent(
    model= OpenAIChat(id="gpt-4o-mini"),
    description= descricao[personalidade],
    tools=[DuckDuckGoTools(), WikipediaTools()],
    markdown=True
    )

if "mensagem" not in st.session_state:
    st.session_state.mensagem = []
    
    
for msg in st.session_state.mensagem:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
            
if st.sidebar.button("Limpar conversas"):
        st.session_state.mensagem = []
        st.rerun()
        
st.title("Clinica HAH")
pergunta = st.chat_input("Pergunte ao Agente sobre seu problema")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
        
    st.session_state.mensagem.append({"role": "user","content":pergunta})
    
    with st.chat_message("assistant"):
        with st.spinner("Agente processando..."):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)
            
    st.session_state.mensagem.append({"role":"assistant", "content":resposta.content})
        
import streamlit as st
from datetime import datetime
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv
import requests as rq
load_dotenv() 

#Criando nossas funções (habilidades/skills)
def get_clima():
    cidade = "Americana"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=72d506180e0cdaf12af56a128bb693c6&units=metric&lang=pt"

    try:
        dados = rq.get(url)
        resposta = dados.json()
        temperatura_atual = resposta['main'] ['temp']
        umidade = resposta['main'] ['humidity']
        destempo = resposta['weather'] [0]['description']
        return f"A temperatura atual é {temperatura_atual}, a umidade está {umidade} e a descrição do clima está {destempo}"
    except:
        return("Não foi possivel acessar os dados do clima")
    
print(get_clima())
personalidade = st.sidebar.selectbox("Personalidade", ["Cara do clima", "Professor de História","Cientista maluco"] )

descricao = {
    "Cara do clima": "Você é o responsável pelo tempo, responsável pelas informações do clima", 
    "Professor de História": "Você é um professor de história que ensina de forma claa, simples e objetiva",
    "Cientista maluco": "Você é um cientista maluco que sempre está em busca de novas inovações e projetos"
    
}

agente = Agent(
    model= OpenAIChat(id="gpt-4o-mini"),
    description= descricao[personalidade],
    tools=[DuckDuckGoTools(), WikipediaTools()],
    markdown=True
    )

if "mensagens" not in st.session_state:
    st.session_state.mensagem = []
    
    
for msg in st.session_state.mensagem:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
            
if st.sidebar.button("Limpar conversas"):
        st.session_state.mensagem = []
        st.rerun()
        
st.title("Sistemas MultiAgentes")
pergunta = st.chat_input("Pergunte ao Agente")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
        
    st.session_state.mensagem.append({"role": "user","content":pergunta})
    
    with st.chat_message("assistant"):
        with st.spinner("Agente processando..."):
            
            
            contexto =""
            if personalidade == "Cara do tempo":
        
                if "clima" in pergunta.lower() or "tempo" in pergunta.lower():
                
                    contexto = f"atualmente o clima está {get_clima()}"
                
        
            resposta = agente.run(pergunta + contexto)
            st.markdown(resposta.content)
            
    st.session_state.mensagem.append({"role":"assistant", "content":resposta.content})
        
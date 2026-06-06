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
def get_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    
    #Estrutura de try/except 
    try:
       dados = rq.get(url)
       resposta = dados.json()
       timestamp = resposta['time_last_updated']
       data_convertida = datetime.fromtimestamp(timestamp)
       
       euro = 1 / resposta ['rates'] ['EUR']
       dolar = 1 / resposta ['rates'] ['USD']
       return f"{dolar:.2f} USD = 1 BRL | {euro:.2f} = 1 BRL. Dados atualizados foram atualizados em {data_convertida}"

    except:
        return("Não foi possivel realizar a conversão de valores")
    
print(get_moedas())

personalidade = st.sidebar.selectbox("Personalidade", ["Professor de Python", "Professor de História","Cientista maluco"] )

descricao = {
    "Professor de Python": "VocÊ é um professor de Python que responde com exemplos e contexto", 
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
            
            if "dólar" in pergunta.lower() or "dolar" in pergunta.lower() or "euro" in pergunta.lower() or "moedas" in pergunta.lower() or "EURO" in pergunta:
                
                contexto = f"o valor atual de conversão de USD e EUR para BRL é:{get_moedas()}"
        
            resposta = agente.run(pergunta + contexto)
            st.markdown(resposta.content)
            
    st.session_state.mensagem.append({"role":"assistant", "content":resposta.content})
        
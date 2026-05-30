import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools 

load_dotenv()

agente = Agent( #Tupla pois não mudaremos o agente
    model=OpenAIChat(id="gpt-4o-mini"), 
    description="Você é um especialista em montar histórias empolgantes de acordo com o tema e gênero que o usuário pedir", 
    tools= [WikipediaTools(), DuckDuckGoTools()],
    markdown=True
)

st.title("Contador de História")

pergunta = st.chat_input("Diga seu tema que farei uma história para você!")

if pergunta:
    
    with st.chat_message("user"):
        st.markdown(pergunta)
        with st.chat_message("assistant"):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)
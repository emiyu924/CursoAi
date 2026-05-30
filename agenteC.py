import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools 

load_dotenv()

agente = Agent( #Tupla pois não mudaremos o agente
    model=OpenAIChat(id="gpt-4o-mini"), 
    description="Você é um professor especialista em planejamento de atividades e planos de estudos, adaptável para cada tipo de aprendizado dependendo de como o usuário pedir", 
    tools= [WikipediaTools(), DuckDuckGoTools()],
    markdown=True
)

st.title("Agente de I.A ")

pergunta = st.chat_input("Faça sua pergunta que responderei da melhor forma!")

if pergunta:
    
    with st.chat_message("user"):
        st.markdown(pergunta)
        with st.chat_message("assistant"):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)
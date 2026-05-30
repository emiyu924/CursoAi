import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools 

load_dotenv()

agente = Agent( #Tupla pois não mudaremos o agente
    model=OpenAIChat(id="gpt-4o-mini"), 
    description="Você é um professor de Python", 
    tools= [WikipediaTools(), DuckDuckGoTools()],
    markdown=True
)

st.title("Agente de I.A ")

pergunta = st.chat_input("Faça sua pergunta que responderei da melhor forma!")

if pergunta:
    
    with st.chat_message("user"):
        st.markdown(pergunta)
        with st.chat_message("assistant"):
            with st.spinner("Agente processando..."):
                resposta = agente.run(pergunta)
                st.markdown(resposta.content)
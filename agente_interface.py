import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools import duckduckgo 
from agno.tools.wikipedia import WikipediaTools 

load_dotenv()

agente = Agent
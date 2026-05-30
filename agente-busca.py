from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools

#todos os agentes necessitam da chave API, e a função load_dotenv faz a leitura do arquivo no .env
load_dotenv()

agente = Agent(
    #define modelo do meu agente 
    model=OpenAIChat(id="gpt-4o-mini"),
    description="você me responde em inglês",
    add_history_to_context=True,
    tools= [DuckDuckGoTools(), TavilyTools],
    markdown=True
)


while True:
    pergunta = input("Digite a sua pergunta: ")
    if pergunta.lower() in ['exit', 'sair', 'quit', 'cancelar', 'finalizar']:
        print("Encerrando agente.... Bom filho sempre volta para casa! 👀")
        break
    else:
     agente.print_response(pergunta)
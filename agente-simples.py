#sempre vai usar esse código para puxar a chave
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

#todos os agentes necessitam da chave API, e a função load_dotenv faz a leitura do arquivo no .env
load_dotenv()

agente = Agent(
    #define modelo do meu agente 
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)

pergunta_um = input("Digite sua pergunta:")

agente.print_response(pergunta_um)


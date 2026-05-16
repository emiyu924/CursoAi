from dotenv import load_dotenv

load_dotenv()

chave = load_dotenv()

if chave:
    print(f"A chave foi carregada com sucesso!")
else:
    print("Chave com erro de leitura!")
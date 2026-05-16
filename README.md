# 🤖 Explicação do Código — Agente de IA com AGNO

## 📦 Importações

```python
from agno.agent import Agent
```

Importa a classe principal responsável por criar e controlar o agente de IA.

Ela gerencia:

- Modelo de IA
- Ferramentas
- Memória
- Histórico
- Contexto
- Execução das respostas

---

```python
from agno.models.openai import OpenAIChat
```

Importa o modelo da OpenAI utilizado pelo agente.

Nesse caso, será usado o modelo:

```python
gpt-4o-mini
```

Responsável por gerar as respostas inteligentes.

---

```python
from agno.tools.duckduckgo import DuckDuckGoTools
```

Adiciona a ferramenta de busca do DuckDuckGo ao agente.

Permite:

- Pesquisar informações na internet
- Buscar dados atualizados
- Complementar respostas da IA

---

```python
from agno.tools.tavily import TavilyTools
```

Importa a integração com o Tavily Search.

O Tavily é otimizado para IA e fornece:

- Pesquisas contextuais
- Resultados mais relevantes
- Melhor performance para agentes inteligentes

---

```python
from agno.db.sqlite import SqliteDb
```

Importa o banco de dados SQLite utilizado para armazenar:

- Histórico
- Sessões
- Conversas
- Memória do agente

---

```python
from dotenv import load_dotenv
```

Permite carregar variáveis do arquivo `.env`.

Normalmente utilizado para:

- API Keys
- Tokens
- Configurações sensíveis

---

# 🔐 Carregando variáveis de ambiente

```python
load_dotenv()
```

Lê automaticamente o arquivo `.env`.

Exemplo:

```env
OPENAI_API_KEY=sua-chave-aqui
```

---

# 🗄️ Criando o banco de dados

```python
bancoDados = SqliteDb(db_file="temp/registros.db")
```

Cria um banco SQLite local.

Arquivo criado:

```bash
temp/registros.db
```

Esse banco armazenará:

- Histórico das conversas
- Sessões do usuário
- Memória contextual

---

# 🧠 Criando o Agente de IA

```python
agente = Agent(
```

Inicializa o agente principal.

---

## 🔹 Modelo utilizado

```python
model=OpenAIChat(id="gpt-4o-mini"),
```

Define qual modelo da OpenAI será utilizado.

Nesse caso:

- GPT-4o Mini
- Modelo rápido
- Mais econômico
- Ótimo para agentes conversacionais

---

## 🔹 Descrição do agente

```python
description="Você é um especialista em pesquisas acadêmicas..."
```

Funciona como uma personalidade/instrução fixa do agente.

Define:

- Comportamento
- Especialidade
- Tom das respostas
- Objetivo principal

---

## 🔹 Histórico no contexto

```python
add_history_to_context=True,
```

Faz com que o agente lembre mensagens anteriores.

Isso permite:

- Conversas contínuas
- Contexto persistente
- Respostas mais inteligentes

---

## 🔹 Banco de dados

```python
db=bancoDados,
```

Conecta o agente ao banco SQLite criado anteriormente.

Assim ele consegue salvar memória persistente.

---

## 🔹 Sessão do usuário

```python
session_id="2d74ac75-2b92-465c-a5ae-d56ecd5bb793",
```

Identifica uma sessão específica de conversa.

Serve para:

- Separar usuários
- Manter contexto individual
- Recuperar histórico corretamente

---

## 🔹 Quantidade de histórico

```python
num_history_runs=3,
```

Define quantas interações anteriores serão enviadas para o modelo.

Nesse caso:

- Últimas 3 conversas

Isso ajuda a economizar tokens.

---

## 🔹 Ferramentas do agente

```python
tools=[DuckDuckGoTools(), TavilyTools],
```

Adiciona ferramentas externas ao agente.

Ferramentas disponíveis:

| Ferramenta | Função |
|---|---|
| DuckDuckGo | Pesquisa web |
| Tavily | Busca inteligente para IA |

---

## 🔹 Respostas em Markdown

```python
markdown=True
```

Faz com que o agente responda formatando em Markdown.

Exemplo:

- Títulos
- Listas
- Código
- Tabelas

---

# 🔁 Loop principal

```python
while True:
```

Mantém o programa rodando continuamente até o usuário decidir sair.

---

# ⌨️ Entrada do usuário

```python
pergunta = input("Digite a sua pergunta: ")
```

Captura perguntas digitadas no terminal.

---

# ❌ Condição de saída

```python
if pergunta.lower() in ['exit', 'sair', 'quit', 'cancelar', 'finalizar']:
```

Verifica se o usuário deseja encerrar o agente.

Comandos aceitos:

- exit
- sair
- quit
- cancelar
- finalizar

---

# 👋 Encerrando o programa

```python
print("Encerando agente...\nAté mais tarde 🤖")
```

Exibe mensagem de encerramento.

---

# 🛑 Finaliza o loop

```python
break
```

Interrompe o `while True`.

---

# 🚀 Executando o agente

```python
agente.print_response(pergunta)
```

Envia a pergunta para o agente.

O agente então:

1. Processa o contexto
2. Consulta ferramentas se necessário
3. Usa o modelo da OpenAI
4. Gera a resposta
5. Exibe no terminal

---

# 🧩 Fluxo Completo do Sistema

```text
Usuário
   ↓
Input Terminal
   ↓
AGNO Agent
   ↓
GPT-4o-mini
   ↓
Ferramentas
 ├── DuckDuckGo
 └── Tavily
   ↓
Banco SQLite
   ↓
Resposta Final
```

---

# ✅ Resumo

Esse código cria um agente de IA completo com:

- Memória persistente
- Histórico contextual
- Busca na internet
- Modelo GPT-4o-mini
- Banco SQLite
- Respostas formatadas
- Conversa contínua

Ideal para:

- Assistentes inteligentes
- Pesquisa acadêmica
- Chatbots
- Agentes autônomos
- Sistemas RAG simples
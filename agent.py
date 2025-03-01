import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.tools import DuckDuckGoSearchRun

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0)

search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="DuckDuckGo Search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions."
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

try:
    response = agent.run("What is the current price of Bitcoin?")
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")

while True:
    try:
        query = input("Ask me anything (or type 'exit'): ")
        if query.lower() == 'exit':
            break

        response = agent.run(query)
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
        break
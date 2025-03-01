import os
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.tools import DuckDuckGoSearchRun

os.environ["OPENAI_API_KEY"] = "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"

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
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.tools import YouTubeSearchTool
from langchain_community.llms import OpenAI
from langchain_community.tools import YouTubeSearchTool, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Load environment variables (e.g., OPENAI_API_KEY)
load_dotenv()

# Initialize the OpenAI LLM
llm = OpenAI(temperature=0, openai_api_key=os.getenv('OPENAI_API_KEY'))

# Manually define tools
yt_tool = YouTubeSearchTool()
wiki_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

tools = [yt_tool, wiki_tool] 

# Initialize memory with a context window of 5 interactions
memory = ConversationBufferWindowMemory(k=5, return_messages=True)

# Initialize the multi-tool agent with memory
agent = initialize_agent(
    tools=tools,  # Pass the tools list directly
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True  # Set to False to hide intermediate reasoning steps
)

def run_interactive_session():
    """Run an interactive Q&A session with the multi-tool agent."""
    print("Welcome to the Multi-Tool AI Agent!")
    print("I can answer questions using Wikipedia, search YouTube, perform Python calculations, and remember our last 5 interactions.")
    print("Type 'exit' to end the session.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ending session. Goodbye!")
            break
        try:
            response = agent.run(user_input)
            print(f"AI: {response}")
        except Exception as e:
            print(f"AI: Oops, something went wrong! Error: {str(e)}")

if __name__ == "__main__":
    run_interactive_session()
import os
from datetime import datetime

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Define the tool using the @tool decorator
@tool
def get_current_datetime() -> str:
    """
    Returns the current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Initialize the LLM (OpenAI Chat Model)
llm = ChatOpenAI(api_key=api_key, temperature=0, model="gpt-3.5-turbo")

# Bind the tool to the LLM
llm_with_tools = llm.bind_tools([get_current_datetime])

# Ask a question requiring tool usage
user_query = "What is the current time and date?"

# Get response
response = llm_with_tools.invoke(user_query)

# Process response
print("\n  LLM Response:")
print(response)

# Check if a tool call was made
if hasattr(response, "tool_calls") and response.tool_calls:
    print("\n Tool Calls Detected:")
    for call in response.tool_calls:
        tool_name = call["name"]
        tool_args = call.get("args", {})
        if tool_name == "get_current_datetime":
            result = get_current_datetime()
            print(f" Tool Output: {result}")
else:
    print("\n LLM Regular Response:")
    print(response.content)

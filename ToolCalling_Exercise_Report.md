# Tool Calling Report

## 1. `tool_agent_app.py` Code

```python
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
```
requirements.txt

langchain
langchain-core
langchain-openai
python-dotenv

.env File
OPENAI_API_KEY="your_openai_api_key_here"

Explanation of Tool

- The function get_current_datetime() is transformed into a LangChain-compatible tool using the @tool decorator. This decorator:
- Registers the function as callable by the LLM.
- Exposes the docstring as its description, allowing the LLM to understand its purpose and decide when to invoke it.

Observations

Query requiring tool: "What is the current time and date?"
Behavior: The LLM invoked the get_current_datetime tool.
Result: It displayed the current system time correctly.

Query not requiring tool: "Tell me a joke."
Behavior: The LLM responded with a natural language joke.
Result: No tool was used.

This shows that the LLM can independently decide when to use external tools based on user intent.

Benefits of Tool Calling in LLMs

Makes LLMs dynamic, with real-time capabilities (like checking current time, weather, databases).
Enables custom functionality (e.g., calling APIs, controlling devices).
Enhances reliability and relevance of answers in real-world apps.

Challenges & Resolutions:
- Didn't face :)


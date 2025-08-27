# Tool Calling with LangChain

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

This project demonstrates how to integrate **LangChain tool-calling** with OpenAI models, enabling dynamic, real-time responses.  
The example implements a simple tool (`get_current_datetime`) that returns the system’s current date and time. The LLM automatically decides whether to invoke the tool or respond directly.

---

## Features
- 🔧 Register custom tools using the `@tool` decorator  
- 🧠 LLM intelligently decides when to call tools based on user intent  
- ⏰ Example tool fetches current date and time dynamically  
- 💡 Natural fallback responses when no tool is required  

---

## Project Structure
- `tool_agent_app.py` → Main application with tool definition and LLM integration  
- `requirements.txt` → Dependencies list  
- `.env` → Stores your OpenAI API key (not committed to version control)  

---

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY="your_openai_api_key_here"
   ```

---

## Usage

Run the application:
```bash
python tool_agent_app.py
```

### Example Runs

- **Tool Call Example**  
  **Query**: `What is the current time and date?`  
  **Behavior**: The LLM invokes `get_current_datetime`  
  **Output**: Displays the current system time  

- **Direct Response Example**  
  **Query**: `Tell me a joke.`  
  **Behavior**: The LLM responds directly without using any tool  

---

## Requirements
```
langchain
langchain-core
langchain-openai
python-dotenv
```

---

## How It Works
1. `get_current_datetime()` is converted into a LangChain-compatible tool with the `@tool` decorator.  
2. The tool is bound to the OpenAI `gpt-3.5-turbo` model.  
3. If the user query requires the tool, the model calls it. Otherwise, it replies normally.  

---

## Benefits
- Real-time capabilities (time, weather, database queries, etc.)  
- Extensible with custom APIs and services  
- Enhances accuracy and reliability in production applications  

---

## Challenges
No issues encountered during implementation.  

---

## Author
👤 **Syed Darain Hyder Kazmi (sawab_e_darain)**  

- GitHub: [DarainHyder](https://github.com/DarainHyder)  
- LinkedIn: [Syed Darain Hyder Kazmi](https://www.linkedin.com/in/syed-darain-hyder-kazmi)  

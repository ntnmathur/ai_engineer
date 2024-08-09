# url: https://www.datacamp.com/tutorial/run-llama-3-locally
# Terminal

# Download Ollama from https://ollama.com/download
# Run the command on terminal: ollama run llama3

# Create a virtual enviornment for AI called venv
#     python3 -m venv /Users/ntnmathur/venv
#     source /Users/ntnmathur/venv/bin/activate
#     python3 -m pip install ollama
# 	  python3 /Users/ntnmathur/github/ai_engineer/local_llm_setup.py

# import ollama
# response = ollama.chat(
#     model="llama3",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is your knowledge cutoff?",
#         },
#     ],
# )

# if __name__ == "__main__":
# 	print(response["message"]["content"])

import asyncio
from ollama import AsyncClient

model_name="llama3:70b"

async def chat():
    """
    Stream a chat from Llama using the AsyncClient.
    """
    message = {
        "role": "user",
        "content": "Tell me an interesting fact about elephants"
    }
    async for part in await AsyncClient().chat(
        model=model_name, messages=[message], stream=True
    ):
        print(part["message"]["content"], end="", flush=True)


asyncio.run(chat())
# url: https://www.datacamp.com/tutorial/run-llama-3-locally
# Terminal

# Download Ollama from https://ollama.com/download
# Run the command on terimal: ollama run llama3

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

async def chat():
    """
    Stream a chat from Llama using the AsyncClient.
    """
    message = {
        "role": "user",
        "content": "Tell me an interesting fact about elephants"
    }
    async for part in await AsyncClient().chat(
        model="llama3", messages=[message], stream=True
    ):
        print(part["message"]["content"], end="", flush=True)


asyncio.run(chat())
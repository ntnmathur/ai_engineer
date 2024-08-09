from llama_index.llms.ollama import Ollama
import asyncio
from ollama import AsyncClient
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

# Create a virtual enviornment for AI called venv
#     python3 -m venv /Users/ntnmathur/venv
#     source /Users/ntnmathur/venv/bin/activate
#     python3 -m pip install ollama
# 	  python3 /Users/ntnmathur/github/ai_engineer/llamaindex_tutorials/a.ollama_llama3.py


##### Basic printing output
# llm = Ollama(model="llama3", request_timeout=120.0)
# resp = llm.complete("Who is Paul Graham?")
# print(resp)

model_name="llama3.1"

def main() -> None:
	message = input("How can I help you?")
	Settings.llm = Ollama(model=model_name, request_timeout=60.0)
	asyncio.run(print_llm(message))
	# Settings.llm = Ollama(model=model_name, request_timeout=60.0)
	# print(Settings.llm)

async def print_llm(input_message: str) -> None:
    """
    Stream a chat from Llama using the AsyncClient.
    """
    message = {
        "role": "user",
        "content": input_message
    }

    async for part in await AsyncClient().chat(
        model=model_name, messages=[message], stream=True
    ):
        print(part["message"].get("content"), end="", flush=True)


if __name__=='__main__':
    main()
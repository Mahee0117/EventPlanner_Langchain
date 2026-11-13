
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model="qwen2:7b",
    model_provider="ollama",
    base_url="http://localhost:11434",
)


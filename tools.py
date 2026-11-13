import logging
from dotenv import load_dotenv
from langchain_core.tools import tool
from tavily import TavilyClient

load_dotenv()
tavily_client = TavilyClient()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
)

@tool
def search_web(query: str) -> str:
    """Search the web for information."""
    logging.info(f"Searching the web for {query}")
    response = tavily_client.search(query=query, max_results=5)
    if not response.get('results'):
        return "No results found."
    return "\n".join([f"{result['title']}: {result['url']}" for result in response['results']])

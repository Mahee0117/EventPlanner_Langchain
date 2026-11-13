### create agents

from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from models import llm
from tools import search_web
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

logging.info("Initializing agent 1")
sub_agent1 = create_react_agent(
    model=llm,
    tools=[search_web],
    name="sub-agent1"
)

logging.info("Initializing agent 2")
sub_agent2 = create_react_agent(
    model=llm,
    tools=[search_web],
    name="sub-agent2"
)

@tool
def delegate_task1(task: str) -> str:
    """ Search the web for a given topic by delegating the task to sub-agent1"""
    response = sub_agent1.invoke({"messages": [HumanMessage(content=task)]})
    return response["messages"][-1].content

@tool
def delegate_task2(task: str) -> str:
    """ Search the web for a given topic by delegating the task to sub-agent2"""
    response = sub_agent2.invoke({"messages": [HumanMessage(content=task)]})
    return response["messages"][-1].content

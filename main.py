import logging
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

from prompts import EVENT_PLANNER_AGENT
from models import llm
from agents import delegate_task1, delegate_task2

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
)

## asking user for requirements
logging.info("Asking user for requirements")
user_requirement = input("Please enter your requirements and preferences for wedding: ")

## main agent
logging.info("Processing requirements with main agent")

main_agent = create_react_agent(
    model=llm,
    tools=[delegate_task1, delegate_task2],
    prompt=EVENT_PLANNER_AGENT,
)

response = main_agent.invoke({"messages": [HumanMessage(content=user_requirement)]})

print("\nMain agent response:")
print(response["messages"][-1].content)

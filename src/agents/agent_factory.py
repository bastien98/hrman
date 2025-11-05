from strands import Agent
from strands.models import Model


def create_agent(system_prompt: str, model: Model, tools=None) -> Agent:
    if tools is None:
        tools = []
    return Agent(
        model=model,
        system_prompt=system_prompt,
        tools=tools,
    )
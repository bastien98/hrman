from strands import Agent
from src.agents.agent_registery import AgentRegistry


class AgentService:
    def __init__(self, agents: AgentRegistry):
        self.agents = agents

    def process_query(self, query: str):
        context_agent: Agent = self.agents.get("context_agent")
        response = context_agent(query)
        return response




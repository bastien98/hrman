import logging

from strands import Agent


class AgentRegistry:
    def __init__(self):
        self._agents = {}

    def register(self, name: str, agent: Agent):
        self._agents[name] = agent
        logging.info(f"Registered agent: {name}")

    def get(self, name):
        return self._agents.get(name)

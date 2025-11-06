import base64
import os
from strands.models.openai import OpenAIModel
from src.agents.agent_factory import create_agent
from src.agents.agent_registery import AgentRegistry
from src.agents.prompts.context_agent import CONTEXT_AGENT_SYSTEM_PROMPT
from src.infra.utils import retrieve_table_schema_str
from src.services.agent_service import AgentService

#Employee schema string
EMPLOYEE_SCHEMA_STR = retrieve_table_schema_str("employees")

#Observability config (langfuse)
LANGFUSE_AUTH = base64.b64encode(
    f"{os.environ.get('LANGFUSE_PUBLIC_KEY')}:{os.environ.get('LANGFUSE_SECRET_KEY')}".encode()
).decode()
os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = os.environ.get("LANGFUSE_BASE_URL") + "/api/public/otel"
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Basic {LANGFUSE_AUTH}"

# Model configs
default_model_config = OpenAIModel(model_id="gpt-4o")

# Register agents here
agents = AgentRegistry()
agents.register("context_agent", create_agent(CONTEXT_AGENT_SYSTEM_PROMPT, default_model_config))
agent_service = AgentService(agents)


def get_agent_service() -> AgentService:
    return agent_service

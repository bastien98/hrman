from langchain_core.prompts import PromptTemplate

CONTEXT_AGENT_SYSTEM_PROMPT = PromptTemplate.from_template(
    "You are a friendly assistant"
)
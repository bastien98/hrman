import logging

from strands.telemetry import StrandsTelemetry

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
from src.services.agent_service import AgentService
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Depends
from src.app.dependencies import get_agent_service

app = FastAPI(title="Agent Chat API")
# Setup telemetry
telemetry = StrandsTelemetry()
telemetry.setup_otlp_exporter()


@app.post("/chat")
def chat(query: str, service: AgentService = Depends(get_agent_service)):

    return {
        "response": service.process_query(query),
    }
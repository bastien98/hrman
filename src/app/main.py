import logging

from strands.telemetry import StrandsTelemetry

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
from dotenv import load_dotenv
load_dotenv()

from src.app.dependencies import get_agent_service


def main():
    # Setup telemetry
    telemetry = StrandsTelemetry()
    telemetry.setup_otlp_exporter()

    logging.info("Starting agent")
    service = get_agent_service()
    service.process_query("hello")


if __name__ == "__main__":
    main()
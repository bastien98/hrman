import os
from typing import Dict, List, Any
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table

load_dotenv()
logger = logging.getLogger(__name__)


def _get_engine():
    db_user: str = os.environ.get('DB_USER')
    db_pass: str = os.environ.get('DB_PASS')
    db_host: str = os.environ.get('DB_HOST')
    db_port: str = os.environ.get('DB_PORT')
    db_name: str = os.environ.get('DB_NAME')

    if not all([db_user, db_pass, db_host, db_port, db_name]):
        raise ValueError("Missing database environment variables")

    connection_string: str = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    return create_engine(connection_string)


def get_table_schema(table_name: str) -> Dict[str, Any]:
    engine = _get_engine()
    metadata: MetaData = MetaData()
    metadata.reflect(bind=engine, only=[table_name])

    if table_name not in metadata.tables:
        raise ValueError(f"Table '{table_name}' does not exist in the database.")

    table: Table = metadata.tables[table_name]

    columns_metadata: List[Dict[str, str]] = [
        {
            "name": col.name,
            "type": str(col.type),
            "description": col.comment or ""
        }
        for col in table.columns
    ]

    return {"table_name": table_name, "columns": columns_metadata}


def format_schema_for_llm(metadata):
    prompt = f"The table `{metadata['table_name']}` has the following columns:\n"
    for col in metadata['columns']:
        desc = col['description'] if col['description'] else "No description"
        prompt += f"- `{col['name']}` ({col['type']}): {desc}\n"
    prompt += "\nUse this schema to answer queries about this table."
    logging.info("Generated EMPLOYEE_SCHEMA_STR schema prompt:\n%s", prompt)
    return prompt

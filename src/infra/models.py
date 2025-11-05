from dataclasses import field, dataclass
from src.infra.utils import format_schema_for_llm, get_table_schema

EMPLOYEE_SCHEMA_STR = format_schema_for_llm(get_table_schema('employees'))


@dataclass
class Employee:
    first_name: str = field(
        metadata={
            "column_name": "first_name",
            "data_type": "varchar",
            "description": "The employee's first name"
        }
    )
    family_name: str = field(
        metadata={
            "column_name": "last_name",
            "data_type": "varchar",
            "description": "The employee's last name"
        }
    )
    seniority_years: int = field(
        metadata={
            "column_name": "seniority",
            "data_type": "int",
            "comment": "The number of years the employee has worked in the organization"
        }
    )

import json
from typing import Any

def parse_json(raw_json: str) -> dict[str, Any]:
    parsed_json= json.loads(raw_json)

    if not isinstance(parsed_json, dict):
        raise ValueError("Expected JSON")

    return parsed_json
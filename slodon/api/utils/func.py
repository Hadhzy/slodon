# Helper functions for the API

from pathlib import Path
import json

# this project
from slodon.api.utils.types import JSON

LANGUAGE = ""  # DEFAULT LANGUAGE en


def res_notation(notion: str) -> JSON:
    """
    Get the json object from the notation

    ### Arguments
    - notion (str): The notion to get the json object from

    ### Returns
    - JSON
    """
    _language = LANGUAGE or "en"  # hard coded for now
    base = "locales/" + _language
    _not_list = notion.split(".")
    _parent = Path(__file__).parent.absolute()
    _file = Path(_not_list[0])
    with open(f"{_parent}/{base}/{_file}.json", "r") as f:
        _json = json.load(f)

    keys = _not_list[1:]
    result = _json
    for key in keys:
        result = result.get(key)
        if result is None:
            return None
    return result





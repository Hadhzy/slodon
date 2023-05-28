# Represent endpoints and their corresponding json objects
# NOTATION -> file_name.object WITHOUT the extension E.G -> .json
# !NOTE: the URL should contain the language as the first part of the path

from typing import Dict

# this project
import slodon.api.utils.func as func

from slodon.api.utils.types import JSON

RESPONSES: Dict[str, JSON] = {"/test1": func.res_notation("en")}


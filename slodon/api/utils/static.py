# Represent endpoints and their corresponding json objects
# NOTATION -> file_name.object WITHOUT the extension E.G -> .json

from typing import Dict

# this project
from slodon.api.utils.func import res_notation

from slodon.api.utils.types import JSON

RESPONSES: Dict[str, JSON] = {"/test1": res_notation("en")}


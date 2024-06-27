from datetime import datetime
from requests import Response

class Context:
    def __init__(self):
        self.script_init: datetime = None
        self.response: Response = None

def before_scenario(context: Context, scenario):
    context.script_init = datetime.now()
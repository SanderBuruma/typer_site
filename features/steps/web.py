from datetime import datetime, timedelta
import requests
from behave import given, then, when
from features.environment import Context
import random

@given('the user loads a random text')
def step(context: Context):
    context.response = requests.get(r'http://localhost:8000/text/{0}'.format(random.randint(1, 2549)))

@then('the page loads within {ms}ms')
def step(context: Context, ms: str):
    milliseconds = (datetime.now() - context.script_init).microseconds // 1000
    assert milliseconds < int(ms), 'Test took {0} milliseconds, expected {1} milliseconds'.format(milliseconds, ms)
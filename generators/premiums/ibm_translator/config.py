from util.configs import build_generator_premium_config
from util.enums import State
from . import ibm_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=ibm_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=175,  
        state=State.PUBLIC
    )
from util.configs import build_classifier_function_config
from util.enums import State
from . import language_translator, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=language_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=81,  
        state=State.PUBLIC
    )

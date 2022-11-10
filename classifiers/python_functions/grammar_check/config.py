from util.configs import build_classifier_function_config
from util.enums import State
from . import grammar_check, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=grammar_check,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=73,
        state=State.PUBLIC,
    )
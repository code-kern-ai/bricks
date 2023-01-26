from util.configs import build_classifier_function_config
from util.enums import State
from . import spelling_check, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=spelling_check,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=73,
        tabler_icon="TextSpellcheck",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )
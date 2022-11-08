from util.configs import build_extractor_function_config
from util.enums import State
from . import credit_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=credit_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=27,
        state=State.PUBLIC,
    )
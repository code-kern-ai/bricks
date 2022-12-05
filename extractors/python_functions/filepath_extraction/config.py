from util.configs import build_extractor_function_config
from util.enums import State
from . import path_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=path_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=56,
        state=State.PUBLIC,
    )

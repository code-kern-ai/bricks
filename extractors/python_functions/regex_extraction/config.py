from util.configs import build_extractor_function_config
from util.enums import State
from . import regex_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=regex_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=38,
        state=State.PUBLIC,
    )

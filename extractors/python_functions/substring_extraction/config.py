from util.configs import build_extractor_function_config
from util.enums import State
from . import substring_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=substring_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=78,
        state=State.PUBLIC,
    )


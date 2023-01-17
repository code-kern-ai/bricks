from util.configs import build_extractor_function_config
from util.enums import State
from . import digit_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=digit_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=46,
        tabler_icon="Number",
        state=State.PUBLIC,
    )

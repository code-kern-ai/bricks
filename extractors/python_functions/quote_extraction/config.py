from util.configs import build_extractor_function_config
from util.enums import State
from . import quote_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=quote_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=61,
        tabler_icon="Quote",
        state=State.PUBLIC,
    )

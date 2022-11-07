from util.configs import build_extractor_function_config
from util.enums import State
from . import window_search, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=window_search,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=41,
        state=State.PUBLIC,
    )

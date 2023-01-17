from util.configs import build_extractor_function_config
from util.enums import State
from . import hashtag_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=hashtag_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=19,
        tabler_icon="Hash",
        state=State.PUBLIC,
    )

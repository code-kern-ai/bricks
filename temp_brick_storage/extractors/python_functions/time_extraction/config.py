from util.configs import build_extractor_function_config
from util.enums import State
from . import time_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=time_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=39,
        tabler_icon="Clock2",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

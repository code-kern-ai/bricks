from util.configs import build_extractor_function_config
from util.enums import State
from . import percentage_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=percentage_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=149,
        tabler_icon="IconPercentage",
        min_refinery_version="1.9.0",
        state=State.PUBLIC,
    )

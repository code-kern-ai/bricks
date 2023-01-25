from util.configs import build_extractor_function_config
from util.enums import State
from . import email_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=email_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=23,
        tabler_icon="Mail",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

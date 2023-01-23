from util.configs import build_extractor_function_config
from util.enums import State
from . import phone_number_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=phone_number_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=35,
        tabler_icon="Phone",
        state=State.PUBLIC,
    )

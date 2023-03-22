from util.configs import build_generator_function_config
from util.enums import State
from . import textblob_spelling_correction, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=textblob_spelling_correction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=111,
        tabler_icon="FileCheck",
        min_refinery_version="1.7.0",
        state=State.PUBLIC
    )

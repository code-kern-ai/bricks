from util.configs import build_generator_function_config
from util.enums import State
from . import language_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=language_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=81,
        tabler_icon="Language",
        min_refinery_version="1.7.0",
        state=State.PUBLIC
    )

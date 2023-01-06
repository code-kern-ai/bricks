from util.configs import build_generator_function_config
from util.enums import State
from . import syllable_count, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=syllable_count,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=21,
        state=State.PUBLIC,
    )

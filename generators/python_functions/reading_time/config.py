from util.configs import build_generator_function_config
from util.enums import State
from . import reading_time, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=reading_time,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=20,
        state=State.PUBLIC,
    )

from util.configs import build_generator_function_config
from util.enums import State
from . import spelling_correction, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=spelling_correction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=111,
        state=State.PUBLIC
    )

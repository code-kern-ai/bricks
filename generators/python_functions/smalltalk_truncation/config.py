from util.configs import build_generator_function_config
from util.enums import State
from . import smalltalk_truncation, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=smalltalk_truncation,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=124,
        state=State.PUBLIC
    )

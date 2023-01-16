from util.configs import build_generator_function_config
from util.enums import State
from . import soundex_generator, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=soundex_generator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=107,
        tabler_icon="Volume",
        state=State.PUBLIC
    )

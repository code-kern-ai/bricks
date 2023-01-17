from util.configs import build_generator_function_config
from util.enums import State
from . import text_summarisation, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=text_summarisation,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=183,
        tabler_icon="Writing",
        state=State.PUBLIC
    )

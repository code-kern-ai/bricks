from util.configs import build_generator_function_config
from util.enums import State
from . import html_cleanser, INPUT_EXAMPLE

def get_config():
    return build_generator_function_config(
        function=html_cleanser,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=109,
        tabler_icon="SquareRoundedLetterH",
        state=State.PUBLIC,
    )

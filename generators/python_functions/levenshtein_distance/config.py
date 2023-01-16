from util.configs import build_generator_function_config
from util.enums import State
from . import levenshtein_distance, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=levenshtein_distance,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=22,
        tabler_icon="SquareRoundedLetterL",
        state=State.PUBLIC,
    )

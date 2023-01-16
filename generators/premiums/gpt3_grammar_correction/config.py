from util.configs import build_generator_premium_config
from util.enums import State
from . import gpt3_grammar_correction, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=gpt3_grammar_correction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=190,
        tabler_icon="Checks",
        state=State.PUBLIC
    )
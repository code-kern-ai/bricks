from util.configs import build_generator_premium_config
from util.enums import State
from . import gpt3_tldr_summarization, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=gpt3_tldr_summarization,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=195,
        state=State.PUBLIC
    )
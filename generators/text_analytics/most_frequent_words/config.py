from util.configs import build_generator_function_config
from util.enums import State
from . import most_frequent_words, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=most_frequent_words,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=240,
        tabler_icon="Stack3",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )
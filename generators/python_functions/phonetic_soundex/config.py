from util.configs import build_generator_function_config
from util.enums import State
from . import phonetic_soundex, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=phonetic_soundex,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=107,
        tabler_icon="Volume",
        min_refinery_version="1.7.0",
        state=State.PUBLIC
    )

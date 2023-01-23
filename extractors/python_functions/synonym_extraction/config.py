from util.configs import build_extractor_function_config
from util.enums import State
from . import synonym_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=synonym_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=75,
        tabler_icon="LetterS",
        state=State.PUBLIC,
    )

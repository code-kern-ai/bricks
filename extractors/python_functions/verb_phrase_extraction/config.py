from util.configs import build_extractor_function_config
from util.enums import State
from . import verb_phrase_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=verb_phrase_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=238,
        tabler_icon="SquareLetterV",
        min_refinery_version="1.8.0",
        state=State.PUBLIC,
    )
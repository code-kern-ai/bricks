from util.configs import build_extractor_function_config
from util.enums import State
from . import noun_match_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=noun_match_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=44,
        tabler_icon="HexagonLetterN",
        state=State.PUBLIC,
    )

from util.configs import build_extractor_function_config
from util.enums import State
from . import work_of_art_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=work_of_art_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=68,
        state=State.PUBLIC,
    )

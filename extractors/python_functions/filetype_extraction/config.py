from util.configs import build_extractor_function_config
from util.enums import State
from . import filetype_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=filetype_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=272,
        tabler_icon="FileInfo",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

from util.configs import build_generator_function_config
from util.enums import State
from . import url_keyword_parser, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=url_keyword_parser,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=163,
        tabler_icon="Cut",
        min_refinery_version="1.7.0",
        state=State.PUBLIC
    )


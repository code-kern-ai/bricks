from util.configs import build_generator_function_config
from util.enums import State
from . import html_unescape, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=html_unescape,
        input_example=INPUT_EXAMPLE, 
        data_type="text",
        issue_id=233,
        tabler_icon="BrandHtml5",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

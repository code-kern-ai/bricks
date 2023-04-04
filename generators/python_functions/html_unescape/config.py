from util.configs import build_generator_function_config
from util.enums import State
from . import _template, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=_template,
        input_example=INPUT_EXAMPLE, 
        data_type="text",
        issue_id=233,
        tabler_icon="IconHtml",
        min_refinery_version="1.9.0",
        state=State.PUBLIC,
    )

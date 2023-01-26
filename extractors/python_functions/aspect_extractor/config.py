from util.configs import build_extractor_function_config
from util.enums import State
from . import aspect_extractor, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=aspect_extractor,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=30,
        tabler_icon="SquarePlus",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

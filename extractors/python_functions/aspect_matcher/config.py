from util.configs import build_extractor_function_config
from util.enums import State
from . import aspect_matcher, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=aspect_matcher,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=30,
        state=State.PUBLIC,
    )

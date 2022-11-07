from util.configs import build_extractor_function_config
from util.enums import State
from . import gazetteer, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=gazetteer,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=31,
        state=State.PUBLIC,
    )

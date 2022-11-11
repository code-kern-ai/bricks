from util.configs import build_extractor_function_config
from util.enums import State
from . import synonym_extractor, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=synonym_extractor,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=75,
        state=State.PUBLIC,
    )

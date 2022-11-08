from util.configs import build_extractor_function_config
from util.enums import State
from . import metric_extractor, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=metric_extractor,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=52,
        state=State.PUBLIC,
    )

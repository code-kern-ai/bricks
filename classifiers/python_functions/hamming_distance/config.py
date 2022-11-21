from util.configs import build_classifier_function_config
from util.enums import State
from . import hamming_distance, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=hamming_distance,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=110,
        state=State.PUBLIC
    )

from util.configs import build_classifier_function_config
from util.enums import State
from . import euclidean_distance, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=euclidean_distance,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=230,
        tabler_icon="VectorTriangle",
        min_refinery_version="1.7.0",
        state=State.PUBLIC
    )
from util.configs import build_classifier_function_config
from util.enums import State
from . import sentence_complexity, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=sentence_complexity,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=2,
        tabler_icon="Abacus",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

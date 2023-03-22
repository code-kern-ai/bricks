from util.configs import build_classifier_function_config
from util.enums import State
from . import language_detection, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=language_detection,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=1,
        tabler_icon="AlphabetGreek",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )
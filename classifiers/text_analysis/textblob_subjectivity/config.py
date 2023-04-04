from util.configs import build_classifier_function_config
from util.enums import State
from . import textblob_subjectivity, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=textblob_subjectivity,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=28,
        tabler_icon="Books",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

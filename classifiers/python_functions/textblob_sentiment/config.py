from util.configs import build_classifier_function_config
from util.enums import State
from . import textblob_sentiment, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=textblob_sentiment,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=27,
        state=State.PUBLIC,
    )

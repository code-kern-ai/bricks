from util.configs import build_classifier_function_config
from util.enums import State
from . import vader_sentiment, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=vader_sentiment,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=157,
        tabler_icon="MoodCrazyHappy",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
    )
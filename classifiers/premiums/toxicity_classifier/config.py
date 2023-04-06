from util.configs import build_classifier_premium_config
from util.enums import State
from . import toxicity_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_premium_config(
        function=toxicity_classifier,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=80,
        tabler_icon="MoodAngry",
        min_refinery_version="1.8.0",
        state=State.PUBLIC
    )

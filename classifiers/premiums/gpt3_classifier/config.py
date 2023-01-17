from util.configs import build_classifier_premium_config
from util.enums import State
from . import gpt3_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_premium_config(
        function=gpt3_classifier,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=168,
        tabler_icon="MoodHappy",
        state=State.PUBLIC
    )

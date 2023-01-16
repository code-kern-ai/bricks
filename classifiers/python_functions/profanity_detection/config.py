from util.configs import build_classifier_function_config
from util.enums import State
from . import profanity_detection, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=profanity_detection,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=-128,
        tabler_icon="MoodWrrr",
        state=State.PUBLIC,
    )

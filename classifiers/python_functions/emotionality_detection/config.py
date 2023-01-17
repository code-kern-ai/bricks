from util.configs import build_classifier_function_config
from util.enums import State
from . import emotionality_detection, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=emotionality_detection,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=97,
        tabler_icon="MoodSad2",
        state=State.PUBLIC
    )

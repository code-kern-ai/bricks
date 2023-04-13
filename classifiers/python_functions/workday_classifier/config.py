from util.configs import build_classifier_function_config
from util.enums import State
from . import workday_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=workday_classifier,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=161,
        tabler_icon="CalendarEvent",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

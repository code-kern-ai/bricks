from util.configs import build_extractor_function_config
from util.enums import State
from . import metric_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=metric_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=52,
        tabler_icon="RulerMeasure",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

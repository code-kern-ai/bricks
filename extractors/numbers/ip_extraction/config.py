from util.configs import build_extractor_function_config
from util.enums import State
from . import ip_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=ip_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=17,
        tabler_icon="MapPin",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

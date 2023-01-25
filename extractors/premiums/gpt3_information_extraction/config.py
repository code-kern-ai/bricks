from util.configs import build_extractor_premium_config
from util.enums import State
from . import gpt3_information_extraction, INPUT_EXAMPLE

def get_config():
    return build_extractor_premium_config(
        function=gpt3_information_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=193,
        tabler_icon="FileInfo",
        min_refinery_version="1.8.0",
        state=State.PUBLIC
    )

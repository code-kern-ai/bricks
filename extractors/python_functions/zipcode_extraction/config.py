from util.configs import build_extractor_function_config
from util.enums import State
from . import zipcode_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=zipcode_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=47,
        tabler_icon="Zip",
        state=State.PUBLIC,  
    )

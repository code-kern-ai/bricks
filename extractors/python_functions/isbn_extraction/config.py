from util.configs import build_extractor_function_config
from util.enums import State
from . import isbn_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=isbn_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=29,
        tabler_icon="Barcode",
        state=State.PUBLIC,
    )

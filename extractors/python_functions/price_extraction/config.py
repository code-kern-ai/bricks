from util.configs import build_extractor_function_config
from util.enums import State
from . import price_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=price_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=37,
        tabler_icon="CurrencyEuro",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

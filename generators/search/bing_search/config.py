from util.configs import build_generator_premium_config
from util.enums import State
from . import bing_search, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=bing_search,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=208,
        tabler_icon="BrandBing",
        min_refinery_version="1.8.0",
        state=State.PUBLIC
    )

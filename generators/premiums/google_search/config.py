from util.configs import build_generator_premium_config
from util.enums import State
from . import google_search, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=google_search,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=206,
        # tabler_icon="BrandGoogle",
        state=State.PUBLIC
    )

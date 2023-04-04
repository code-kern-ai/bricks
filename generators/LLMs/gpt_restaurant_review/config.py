from util.configs import build_generator_premium_config
from util.enums import State
from . import gpt3_restaurant_review, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=gpt3_restaurant_review,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=202,
        tabler_icon="ChefHat",
        min_refinery_version="1.8.0",
        state=State.PUBLIC,
    )

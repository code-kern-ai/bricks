from util.configs import build_generator_premium_config
from util.enums import State
from . import microsoft_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=microsoft_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=115,
        tabler_icon="BrandWindows",
        state=State.PUBLIC
    )

from util.configs import build_generator_premium_config
from util.enums import State
from . import deepl_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=deepl_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=114,
        tabler_icon="LanguageKatakana",
        min_refinery_version="1.7.0",
        state=State.PUBLIC
    )

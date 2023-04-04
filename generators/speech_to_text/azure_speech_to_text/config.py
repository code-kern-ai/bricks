from util.configs import build_generator_premium_config
from util.enums import State
from . import azure_speech_to_text, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=azure_speech_to_text,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=250,
        tabler_icon="Speakerphone",
        min_refinery_version="1.7.0",
        state=State.PUBLIC
    )

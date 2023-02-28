from util.configs import build_generator_premium_config
from util.enums import State
from . import openai_whisper, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=openai_whisper,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=185,
        tabler_icon="DeviceAudioTape",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

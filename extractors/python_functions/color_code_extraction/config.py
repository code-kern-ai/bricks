from util.configs import build_extractor_function_config
from util.enums import State
from . import INPUT_EXAMPLE, color_code_extraction


def get_config():
    return build_extractor_function_config(
        function=color_code_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=60,  # you need to look this up in the issues https://github.com/code-kern-ai/bricks/issues
        state=State.PUBLIC,  # make this State.PUBLIC when you are ready to publish
    )

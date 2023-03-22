from util.configs import build_extractor_function_config
from util.enums import State
from . import _template, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=_template,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=-1,  # you need to look this up in the issues https://github.com/code-kern-ai/bricks/issues
        tabler_icon="Template", # Add any fitting icon from tabler-icons.io
        min_refinery_version="x.x.x",  # you need to look this up in the issues
        state=State.DRAFT, # in the actual module, set this to PUBLIC before pushing to main!
    )

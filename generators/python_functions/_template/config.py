from util.configs import build_generator_function_config
from util.enums import State
from . import _template


def get_config():
    return build_generator_function_config(
        function=_template,
        data_type="text",
        issue_id=-1,  # you need to look this up in the issues https://github.com/code-kern-ai/bricks/issues
        state=State.DRAFT, # in the actual module, set this to PUBLIC before pushing to main!
    )

from util.configs import build_generator_learner_config
from util.enums import State
from . import _template


def get_config():
    return build_generator_learner_config(
        function=_template,
        issue_id=-1,  # you need to look this up in the issues https://github.com/code-kern-ai/bricks/issues
        tabler_icon="Template",  # Add any fitting icons from https://tabler-icons-react.vercel.app/
        min_refinery_version="x.x.x",
        state=State.DRAFT,  # in the actual module, set this to PUBLIC before pushing to main!
    )

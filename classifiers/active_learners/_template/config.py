from util.configs import build_classifier_learner_config
from util.enums import State
from . import _template


def get_config():
    return build_classifier_learner_config(
        function=_template,
        data_type="text",
        issue_id=-1,  # you need to look this up in the issues https://github.com/code-kern-ai/bricks/issues
        tabler_icon="Template",  # Add any fitting icon from https://tabler-icons-react.vercel.app/
        min_refinery_version="x.x.x",  # you need to look this up in the issues
        state=State.DRAFT,  # in the actual module, set this to PUBLIC before pushing to main!
    )

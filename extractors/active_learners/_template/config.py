from util.configs import build_extractor_learner_config
from util.enums import State
from . import my_tagger, INPUT_EXAMPLE


def get_config():
    return build_extractor_learner_config(
        function=my_tagger,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=0,  # you need to look this up in the issues https://github.com/code-kern-ai/bricks/issues
        state=State.DRAFT,  # make this State.PUBLIC when you are ready to publish
    )

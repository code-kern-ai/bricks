from util.configs import (
    build_classifier_learner_config,
)  # you might need to change this line, depending on your module and extractor type
from util.enums import State
from . import my_lf, INPUT_EXAMPLE


def get_config():
    return build_classifier_learner_config(
        function=my_lf,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=0,  # you need to look this up in the issues https://github.com/code-kern-ai/bricks/issues
        state=State.DRAFT,  # make this State.PUBLIC when you are ready to publish
    )

from util.configs import build_classifier_learner_config
from util.enums import State
from . import random_search


def get_config():
    return build_classifier_learner_config(
        function=random_search,
        data_type="text",
        issue_id=49,
        state=State.PUBLIC,
    )

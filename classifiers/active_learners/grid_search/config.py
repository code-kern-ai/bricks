from util.configs import build_classifier_learner_config
from util.enums import State
from . import grid_search


def get_config():
    return build_classifier_learner_config(
        function=grid_search,
        data_type="text",
        issue_id=48,
        state=State.PUBLIC,
    )

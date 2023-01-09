from util.configs import build_classifier_learner_config
from util.enums import State
from . import bayesian_optimization


def get_config():
    return build_classifier_learner_config(
        function=bayesian_optimization,
        data_type="text",
        issue_id=188,
        state=State.PUBLIC,
    )
from util.configs import build_classifier_learner_config
from util.enums import State
from . import bayesian_optimization


def get_config():
    return build_classifier_learner_config(
        function=bayesian_optimization,
        issue_id=188,
        tabler_icon="ChartDots",
        min_refinery_version="1.8.1",
        state=State.DRAFT.value,
    )

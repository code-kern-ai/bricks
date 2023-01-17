from util.configs import build_classifier_learner_config
from util.enums import State
from . import logistic_regression


def get_config():
    return build_classifier_learner_config(
        function=logistic_regression,
        data_type="text",
        issue_id=42,
        tabler_icon="Contrast2",
        state=State.PUBLIC,
    )

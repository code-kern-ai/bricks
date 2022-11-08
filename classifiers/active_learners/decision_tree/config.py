from util.configs import build_classifier_learner_config
from util.enums import State
from . import decision_tree


def get_config():
    return build_classifier_learner_config(
        function=decision_tree,
        data_type="text",
        issue_id=50,
        state=State.PUBLIC,
    )

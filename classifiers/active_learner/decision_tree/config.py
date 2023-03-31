from util.configs import build_classifier_learner_config
from util.enums import State
from . import decision_tree


def get_config():
    return build_classifier_learner_config(
        function=decision_tree,
        data_type="text",
        issue_id=50,
        tabler_icon="BinaryTree",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

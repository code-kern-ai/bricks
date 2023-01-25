from util.configs import build_classifier_learner_config
from util.enums import State
from . import random_forest


def get_config():
    return build_classifier_learner_config(
        function=random_forest,
        data_type="text",
        issue_id=51,
        tabler_icon="BinaryTree2",
        min_refinery_version="1.7.",
        state=State.PUBLIC,
    )

from util.configs import build_classifier_learner_config
from util.enums import State
from . import decision_tree


def get_config():
    return build_classifier_learner_config(
        function=decision_tree,
        issue_id=50,
        tabler_icon="BinaryTree",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="active_learner",
        gdpr_compliant="true",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery"],
        part_of_group=[
            "active_learner",
            "gdpr_compliant",
        ],
        integrator_inputs={
            "input": "coming soon"
        }
    )
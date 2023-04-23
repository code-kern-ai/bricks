from util.configs import build_classifier_learner_config
from util.enums import State
from . import logistic_regression


def get_config():
    return build_classifier_learner_config(
        function=logistic_regression,
        issue_id=42,
        tabler_icon="Contrast2",
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

from util.configs import build_extractor_learner_config
from util.enums import State
from . import crf_tagger


def get_config():
    return build_extractor_learner_config(
        function=crf_tagger,
        issue_id=43,
        tabler_icon="BracketsContain",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="active_learner",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery"],
        part_of_group=[
            "active_learner",
        ],
        integrator_inputs={
            "input": "coming soon"
        }
    )

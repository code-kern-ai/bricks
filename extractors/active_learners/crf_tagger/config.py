from util.configs import build_extractor_learner_config
from util.enums import State
from . import crf_tagger


def get_config():
    return build_extractor_learner_config(
        function=crf_tagger,
        data_type="text",
        issue_id=43,
        state=State.PUBLIC,
    )

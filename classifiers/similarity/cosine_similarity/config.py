from util.configs import build_classifier_function_config
from util.enums import State
from . import cosine_similarity, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=cosine_similarity,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=79,
        tabler_icon="WaveSine",
        min_refinery_version="1.7.0",
        state=State.PUBLIC
    )

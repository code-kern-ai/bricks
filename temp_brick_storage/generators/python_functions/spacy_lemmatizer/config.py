from util.configs import build_generator_function_config
from util.enums import State
from . import spacy_lemmatizer, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=spacy_lemmatizer,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=228,
        tabler_icon="Transform",
        min_refinery_version="1.7.0",
        state=State.PUBLIC
    )

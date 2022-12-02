from util.configs import build_extractor_function_config
from util.enums import State
from . import iban_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=iban_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=143,
        state=State.DRAFT,  # in the actual module, set this to PUBLIC before pushing to main!
    )

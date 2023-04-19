from util.configs import build_classifier_function_config
from util.enums import State, SelectionType, BricksVariableType, RefineryDataType
from . import sumy_website_summarizer, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        # strapi information
        function=sumy_website_summarizer,
        input_example=INPUT_EXAMPLE,
        issue_id=284,
        tabler_icon="MoodCrazyHappy",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
        type="python_function",
        gdpr_compliant="true",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "_template_func",
            "gdpr_compliant",
        ],  # first entry should be parent directory
    )
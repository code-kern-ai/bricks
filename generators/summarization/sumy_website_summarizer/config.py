from util.configs import build_generator_function_config
from util.enums import State, SelectionType, BricksVariableType, RefineryDataType
from . import sumy_website_summarizer, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        # strapi information
        function=sumy_website_summarizer,
        input_example=INPUT_EXAMPLE,
        issue_id=284,
        tabler_icon="Filter",
        min_refinery_version="1.9.2",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "summarization",
        ],  # first entry should be parent directory
        integrator_inputs={
            "name": "sumy_website_summarizer",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "url",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "AGE": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "english",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value
                    ]
                },
                "SENTENCE_COUNT": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 5,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_INT.value
                    ]
                }
            }
        }
    )
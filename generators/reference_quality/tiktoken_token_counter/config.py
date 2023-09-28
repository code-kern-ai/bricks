from util.configs import build_classifier_function_config
from util.enums import State, BricksVariableType, RefineryDataType, SelectionType
from . import tiktoken_token_counter, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        # strapi information
        function=tiktoken_token_counter,
        input_example=INPUT_EXAMPLE,
        issue_id=359,
        tabler_icon="SortAscendingNumbers",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "reference_quality",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "tiktoken_token_counter",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "ENCODING_NAME": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "cl100k_base",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )
from util.configs import build_generator_function_config
from util.enums import State, BricksVariableType, RefineryDataType, SelectionType
from . import tiktoken_token_counter, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        # strapi information
        function=tiktoken_token_counter,
        input_example=INPUT_EXAMPLE,
        issue_id=359,
        tabler_icon="SortAscendingNumbers",
        min_refinery_version="2.0.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "text_analytics",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "tiktoken_token_counter",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "ENCODING_NAME": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "cl100k_base",
                    "allowedValues": ["cl100k_base", "p50k_base", "r50k_base"],
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )
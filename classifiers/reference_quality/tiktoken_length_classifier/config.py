from util.configs import build_classifier_function_config
from util.enums import State, BricksVariableType, RefineryDataType, SelectionType
from . import tiktoken_length_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        # strapi information
        function=tiktoken_length_classifier,
        input_example=INPUT_EXAMPLE,
        issue_id=347,
        tabler_icon="ListNumbers",
        min_refinery_version="2.0.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "reference_quality",
        ],  # first entry should be parent directory
        cognition_init_mapping={
            "short": "Needs fix",
            "medium": "Sufficient",
            "long": "Needs fix"
        },
        # bricks integrator information
        integrator_inputs={
            "name": "tiktoken_length_classifier",
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

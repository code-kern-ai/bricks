from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import levenshtein_distance, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=levenshtein_distance,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=22,
        tabler_icon="SquareRoundedLetterL",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["distance", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "levenshtein_distance",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "BASE_SENTENCE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "This is a base sentence to compare to.",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "WEIGHT_INSERTION": {
                    "selectionType": SelectionType.INT.value,
                    "defaultValue": 1,
                    "description": "Optional",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_INT.value
                    ]
                },
                "WEIGHT_DELETION": {
                    "selectionType": SelectionType.INT.value,
                    "defaultValue": 1,
                    "description": "Optional",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_INT.value
                    ]
                },
                "WEIGHT_SUBSTITUTION": {
                    "selectionType": SelectionType.INT.value,
                    "defaultValue": 1,
                    "description": "Optional",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_INT.value
                    ]
                }
            }
        }
    )
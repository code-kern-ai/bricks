from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import levenshtein_distance, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=levenshtein_distance,
        input_example=INPUT_EXAMPLE,
        issue_id=22,
        tabler_icon="SquareRoundedLetterL",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="true",
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "distance",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "levenshtein_distance",
            "refineryDataType": RefineryDataType.FLOAT.value,
            "variables": {
                "BASE_SENTENCE": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "This is a base sentence to compare to.",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "WEIGHT_INSERTION": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 1,
                    "optional": "true",
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
                "WEIGHT_DELETION": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 1,
                    "optional": "true",
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
                "WEIGHT_SUBSTITUTION": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 1,
                    "optional": "true",
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
            },
        },
    )

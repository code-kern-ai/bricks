from util.configs import build_extractor_function_config
from util.enums import State, BricksVariableType, RefineryDataType, SelectionType
from . import aspect_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=aspect_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=30,
        tabler_icon="SquarePlus",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "functions",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "aspect_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "WINDOW": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 4,
                    "description": "choose any window size here",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
                "SENSITIVITY": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 0.5,
                    "description": "choose any value between 0 and 1",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_FLOAT.value],
                },
                "NEGATIVE_LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "negative",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "POSITIVE_LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "positive",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

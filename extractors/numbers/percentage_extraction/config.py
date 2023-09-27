from util.configs import build_extractor_function_config
from util.enums import State, SelectionType, BricksVariableType, RefineryDataType
from . import percentage_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=percentage_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=149,
        tabler_icon="Percentage",
        min_refinery_version="1.9.0",
        state=State.PUBLIC.value,
        type="python_function",

        available_for=["refinery", "common"],
        part_of_group=[
            "numbers",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping="none",
        integrator_inputs={
            "name": "percentage_extraction",
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
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "isbn",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "REGEX": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "(-?\d+(?:[.,]\d*)?|-?[.,]\d+)%",
                    "description": "Choose any regex here",
                    "optional": "false",
                    "addInfo": [BricksVariableType.REGEX.value],
                },
            },
        },
    )

from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import substring_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=substring_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=78,
        tabler_icon="Blockquote",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "words",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "substring_extraction",
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
                "SUBSTRING": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "example",
                    "description": "The substring to search for in a longer text.",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "substring",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

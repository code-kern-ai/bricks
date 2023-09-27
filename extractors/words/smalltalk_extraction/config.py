from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import smalltalk_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=smalltalk_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=59,
        tabler_icon="MessageCircle2",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "words",
        ],  # first entry should be parent directory
        # bricks integrator information 
        integrator_inputs={
            "name": "smalltalk_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "globalComment": "currently only english language is supported here\nreach out to us if you would like to request other languages to be supported",
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
                    "defaultValue": "smalltalk",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

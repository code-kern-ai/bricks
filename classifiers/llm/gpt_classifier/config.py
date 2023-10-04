from util.configs import build_classifier_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import gpt_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_premium_config(
        function=gpt_classifier,
        input_example=INPUT_EXAMPLE,
        issue_id=168,
        tabler_icon="MoodHappy",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
        type="premium",
        available_for=["refinery", "common"],
        part_of_group=[
            "llm",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "gpt_classifier",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "API_KEY": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "CLASSIFY_BY": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "emotional sentiment",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "TEMPERATURE": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 0,
                    "allowedRange": [0, 100],
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_FLOAT.value],
                },
                "LABELS": {
                    "selectionType": SelectionType.LIST.value,
                    "description": "change this to the labels you want to classify by",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value
                    ]
                }
            },
        },
    )

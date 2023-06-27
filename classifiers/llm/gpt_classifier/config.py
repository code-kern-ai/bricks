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
        gdpr_compliant="false",
        type="premium",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "llm",
            "not_gdpr_compliant",
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
                "MAX_TOKENS": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 64,
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
                "TOP_P": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 1,
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_FLOAT.value],
                },
                "FREQUENCY_PENALTY": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 0,
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_FLOAT.value],
                },
                "PRESENCE_PENALTY": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 0,
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_FLOAT.value],
                },
            },
        },
    )

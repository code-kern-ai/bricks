from util.configs import build_classifier_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import gpt_cross_encoder, INPUT_EXAMPLE


def get_config():
    return build_classifier_premium_config(
        function=gpt_cross_encoder,
        input_example=INPUT_EXAMPLE,
        issue_id=357,
        tabler_icon="ArrowsCross",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
        type="premium",
        available_for=["refinery", "common"],
        part_of_group=[
            "reference_relevance",
            "llm",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "gpt_cross_encoder",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": ["Yes", "No"],
            "variables": {
                "QUESTION": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "REFERENCE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "reference",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "API_KEY": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "API_BASE": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "https://api.openai.com/v1",
                    "optional": "true",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "API_TYPE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "open_ai",
                    "allowedValues": ["open_ai", "azure"],
                    "description": "or 'azure'",
                    "optional": "true",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "API_VERSION": {
                    "selectionType": SelectionType.STRING.value,
                    "optional": "true",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "ENGINE": {
                    "selectionType": SelectionType.STRING.value,
                    "optional": "true",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "TEMPERATURE": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 0,
                    "addInfo": [
                        BricksVariableType.GENERIC_FLOAT.value
                    ]
                }
            }
        }
    )
from util.configs import build_extractor_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import gpt3_information_extraction, INPUT_EXAMPLE

def get_config():
    return build_extractor_premium_config(
        function=gpt3_information_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=193,
        tabler_icon="FileInfo",
        min_refinery_version="1.8.0",
        state=State.PUBLIC,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["LLMs", "not_gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "gpt_information_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "API_KEY": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
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
                "EXTRACTION_KEYWORD": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "names",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "TEMPERATURE": {
                    "selectionType": SelectionType.INT.value,
                    "defaultValue": 0,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_INT.value
                    ]
                },
                "MAX_TOKENS": {
                    "selectionType": SelectionType.INT.value,
                    "defaultValue": 64,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_INT.value
                    ]
                },
                "TOP_P": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 1,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_FLOAT.value
                    ]
                },
                "FREQUENCY_PENALTY": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 0,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_FLOAT.value
                    ]
                },
                "PRESENCE_PENALTY": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 0,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_FLOAT.value
                    ]
                }
            }
        }
    )

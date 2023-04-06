from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import azure_speech_to_text, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=azure_speech_to_text,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=250,
        tabler_icon="Speakerphone",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["speech_to_text", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "azure_speech_to_text",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "API_KEY": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "<you-api-key-here>",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "RESOURCE_REGION": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "northeurope",
                    "description": "region where your resource is deployed",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "LANGUAGE": {
                    "selectionType": SelectionType.STRING.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value
                    ]
                }
            }
        }
    )

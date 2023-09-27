from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import azure_speech_to_text, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=azure_speech_to_text,
        input_example=INPUT_EXAMPLE,
        issue_id=250,
        tabler_icon="Speakerphone",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "speech_to_text",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "azure_speech_to_text",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "API_KEY": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "RESOURCE_REGION": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "northeurope",  # might be good as choice
                    "description": "region where your resource is deployed",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "LANGUAGE": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "en-US",
                    "description": "language of the audio file",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

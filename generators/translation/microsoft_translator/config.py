from util.configs import build_generator_premium_config
from util.enums import State
from . import microsoft_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=microsoft_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=115,
        tabler_icon="BrandWindows",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="True",
        type="premium",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["translation", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "microsoft_translator",
            "refineryInputType": "text",
            "outputs": ["translated text"],
            "constants": {
                "inputAttribute": { # previously YOUR_ATTRIBUTE, never optional
                    "selectionType": "string",
                    "defaultValue": "your-text",
                },  
                "apiKey": {
                    "selectionType": "string",
                    "defaultValue": "YOUR_API_KEY",
                    "description": "The Azure Cognitive service API key.",
                    "optional": "False",
                },
                "originalLanguage": {
                    "selectionType": "string",
                    "defaultValue": "en",
                    "description": "The language of the text that is to be translated.",
                    "optional": "False",
                },
                "targetLanguage": {
                    "selectionType": "string",
                    "defaultValue": "de",
                    "description": "The language to translate to.",
                    "optional": "False",
                },
            },
        },
    )

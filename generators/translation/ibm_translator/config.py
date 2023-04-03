from util.configs import build_generator_premium_config
from util.enums import State
from . import ibm_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=ibm_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=175,
        tabler_icon="LanguageHiragana",
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
            "name": "ibm_translator",
            "refineryDataType": "text",
            "outputs": ["translated text"],
            "variables": {
                "YOUR_ATTRIBUTE": { # previously YOUR_ATTRIBUTE, never optional
                    "selectionType": "string",
                    "defaultValue": "",
                    "refineryType": "attribute",
                }, 
                "API_KEY": {
                    "selectionType": "string",
                    "defaultValue": "<your-api-key>",
                    "description": "The IBM Watson translation service API key.",
                    "optional": "False",
                },
                "ibmUrl": {
                    "selectionType": "string",
                    "defaultValue": "<your-resource-url>",
                    "description": "The URL for the IBM Watson Language Translator resource.",
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
                    "description": "The language to translate to. The original language is automatically detected.",
                    "optional": "False",
                },
            },
        },
    )
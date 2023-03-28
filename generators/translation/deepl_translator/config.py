from util.configs import build_generator_premium_config
from util.enums import State
from . import deepl_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=deepl_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=114,
        tabler_icon="LanguageKatakana",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        gdpr_compliant=True,
        kern_token_proxy_usable=False,
        docker_image=None,
        available_for=["refinery", "common"],
        part_of_group=["spelling", "gdpr_compliant"],
        # bricks integrator information
        integrator_inputs={
            "name": "spelling_check",
            "refineryInputType": "text",
            "outputs": ["translated text"],
            "constants": {
                "inputAttribute": { # previously YOUR_ATTRIBUTE, never optional
                    "selectionType": "text",
                    "defaultValue": "your-text",
                },   
                "apiKey": {
                    "selectionType": "string",
                    "defeaultValue": "YOUR_API_KEY",
                    "description": "The DeepL Premium API key.",
                    "optional": "False",
                },
                "targetLanguage": {
                    "selectionType": "string",
                    "defaultValue": "EN",
                    "description": "The language to translate to. The original language is automatically detected.",
                    "optional": "False",
                },
            },
        },
    )
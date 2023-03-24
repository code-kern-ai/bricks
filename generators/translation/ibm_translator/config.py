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
        state=State.PUBLIC,
        gdpr_compliant=True,
        kern_token_proxy_usable=False,
        docker_image=None,
        available_for=["refinery", "common"],
        part_of_group=["spelling", "gdpr_compliant"],
        # bricks integrator information
        outputs=["contains mistakes", "no mistakes"],
        integrator_inputs={
            "name": "spelling_check",
            "refineryInputType": "text",
            "constants": {
                "inputRecordAttribute": {
                    "default": "text",
                    "optional": False,
                }, 
                "apiKey": {
                    "defaultValue": "YOUR_API_KEY",
                    "type": "string",
                    "optional": False,
                    "description": "The API key for the IBM Watson Language Translator service.",
                },
                "ibmUrl": {
                    "defaultValue": "https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID",
                    "type": "string",
                    "optional": False,
                    "description": "The URL for the IBM Watson Language Translator resource.",
                },
                "originalLanguage": {
                    "defaultValue": "en",
                    "type": "string",
                    "optional": False,
                    "description": "The language of the text that is to be translated.",
                },
                "targetLanguage": {
                    "defaultValue": "de",
                    "type": "string",
                    "optional": False,
                    "description": "The language to translate to.",
                },
            },
        },
    )
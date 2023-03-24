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
                    "description": "The Azure Cognitive service API key.",
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

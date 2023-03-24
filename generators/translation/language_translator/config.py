from util.configs import build_generator_function_config
from util.enums import State
from . import language_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=language_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=81,
        tabler_icon="Language",
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
                    "defaultValue": "text",
                    "optional": False,
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

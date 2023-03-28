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
        state=State.PUBLIC.value,
        gdpr_compliant="True",
        type="premium",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["translation", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "language_translator",
            "refineryInputType": "text",
            "outputs": ["translated text"],
            "constants": {
                "inputAttribute": { # previously YOUR_ATTRIBUTE, never optional
                    "selectionType": "string",
                    "defaultValue": "your-text",
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

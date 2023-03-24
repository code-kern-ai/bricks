from util.configs import build_classifier_function_config
from util.enums import State
from . import spelling_check, INPUT_EXAMPLE

def get_config():
    return build_classifier_function_config(
        # strapi information
        function=spelling_check,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=73,
        tabler_icon="TextSpellcheck",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        type="python_function",
        gdpr_compliant="True",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["spelling", "gdpr_compliant"],
        # bricks integrator information
        outputs=["contains mistakes", "no mistakes"],
        integrator_inputs={
            "name": "spelling_check",
            "refineryInputType": "text",
            "constants": {
                "inputRecordAttribute": {
                    "defaultvalue": "text",
                    "optional": False,
                },  
                "labelMistake": {
                    "defaultValue": "contains mistakes",
                    "type": "string",
                    "optional": False,
                    "description": "The label for the output if the text contains spelling mistakes.",
                },
                "labelNoMistake": {
                    "defaultValue": "no mistakes",
                    "type": "string",
                    "optional": False,
                    "description": "The label for the output if the text does not contain spelling mistakes.",
                },
            },
        },
    )
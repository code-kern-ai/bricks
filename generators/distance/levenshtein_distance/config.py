from util.configs import build_generator_function_config
from util.enums import State
from . import levenshtein_distance, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=levenshtein_distance,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=22,
        tabler_icon="SquareRoundedLetterL",
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
                "baseSentence": {
                    "defaultValue": "The sun is not made out of pancakes.",
                    "type": "string",
                    "optional": False,
                    "description": "The label for the output if the text contains spelling mistakes.",
                },
                "weightInsertion": {
                    "defaultValue": 1,
                    "type": "int",
                    "optional": False,
                    "description": "Weight for the insertion parameter.",
                },
                "weightDeletion": {
                    "defaultValue": 1,
                    "type": "int",
                    "optional": False,
                    "description": "Weight for the deletion parameter.",
                },
                "weightSubstitution": {
                    "defaultValue": 1,
                    "type": "int",
                    "optional": False,
                    "description": "Weight for the deletion parameter.",
                },
            },
        },
    )
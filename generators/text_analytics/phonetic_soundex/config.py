from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import phonetic_soundex, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=phonetic_soundex,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=107,
        tabler_icon="Volume",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["text_analytics", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "phonetic_soundex",
            "refineryDataType": RefineryDataType.TEXT.value,
            "globalComment": "Currently only english language is supported here\nReach out to us if this should be extended for other languages",
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )

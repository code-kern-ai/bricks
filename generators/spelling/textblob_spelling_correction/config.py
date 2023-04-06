from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import textblob_spelling_correction, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=textblob_spelling_correction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=111,
        tabler_icon="FileCheck",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["distance", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "textblob_spelling_correction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "globalComment": "currently only english language is supported here",
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

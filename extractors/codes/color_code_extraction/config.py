from util.configs import build_extractor_function_config
from util.enums import State, BricksVariableType, RefineryDataType, SelectionType
from . import INPUT_EXAMPLE, color_code_extraction


def get_config():
    return build_extractor_function_config(
        function=color_code_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=60,  # you need to look this up in the issues https://github.com/code-kern-ai/bricks/issues
        tabler_icon="ColorSwatch",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["codes", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "color_code_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "color",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )

from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import regex_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=regex_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=38,
        tabler_icon="Regex",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["functions", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "regex_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "REGEX": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "\\$[0-9]+",
                    "description": "Choose any regex here",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.REGEX.value
                    ]
                },
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
                    "defaultValue": "money",
                    "description": "Choose any available label here",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )

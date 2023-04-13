from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import person_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=person_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=34,
        tabler_icon="User",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,  
        gdpr_compliant="true",
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=["personal_identifiers", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "person_extraction",
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
                    "defaultValue": "name",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )
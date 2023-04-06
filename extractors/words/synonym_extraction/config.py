from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import synonym_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=synonym_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=75,
        tabler_icon="LetterS",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["words", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "synonym_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "globalComment": "currently only english language is supported here\nreach out to us if this should be extended for other languages",
            "variables": {
                "TARGET_WORD": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "soccer",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
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
                    "defaultValue": "synonym",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )

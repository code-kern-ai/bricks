from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import synonym_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=synonym_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=75,
        tabler_icon="LetterS",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="true",
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "words",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "synonym_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "globalComment": "currently only english language is supported here\nreach out to us if this should be extended for other languages",
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "TARGET_WORD": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "soccer",
                    "optional": "false",
                    "description": "The word for which synonyms should be extracted.",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "synonym",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

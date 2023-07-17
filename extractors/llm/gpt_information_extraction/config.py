from util.configs import build_extractor_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import gpt_information_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_premium_config(
        function=gpt_information_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=193,
        tabler_icon="FileInfo",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
        gdpr_compliant="false",
        type="premium",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "llm",
            "not_gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "gpt_information_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "API_KEY": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                    "defaultValue": "names",
                },
                "EXTRACTION_KEYWORD": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "names",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "TEMPERATURE": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 0,
                    "allowedValues": [0, 100],
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
            },
        },
    )

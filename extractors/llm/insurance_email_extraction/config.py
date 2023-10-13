from util.configs import build_extractor_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import insurance_email_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_premium_config(
        function=insurance_email_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=332,
        tabler_icon="mail-opened-filled",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "llm",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "insurance_email_extraction",
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
                    "selectionType": SelectionType.LIST.value,
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

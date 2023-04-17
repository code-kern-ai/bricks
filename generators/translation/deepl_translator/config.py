from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import deepl_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=deepl_translator,
        input_example=INPUT_EXAMPLE,
        issue_id=114,
        tabler_icon="LanguageKatakana",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="true",
        type="premium",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "translation",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "deepl_translator",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "API_KEY": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "description": "Deepl API Key",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "TARGET_LANGUAGE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "only iso format",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

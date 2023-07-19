from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import ibm_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=ibm_translator,
        input_example=INPUT_EXAMPLE,
        issue_id=175,
        tabler_icon="LanguageHiragana",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="premium",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "translation",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "ibm_translator",
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
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "IBM_INSTANCE_ID": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "<RESOURCE_INSTANCE_ID_GOES_HERE>",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "ORIGIN_LANG": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "en",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "TARGET_LANG": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "de",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import ibm_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=ibm_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=175,
        tabler_icon="LanguageHiragana",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="True",
        type="premium",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["translation", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "ibm_translator",
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
                "IBM_URL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "<RESOURCE_URL_GOES_HERE",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "ORIGIN_LANG": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "en",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "TARGET_LANG": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "de",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )
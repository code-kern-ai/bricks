from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import google_search, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=google_search,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=206,
        tabler_icon="BrandGoogle",
        min_refinery_version="1.8.0",
        state=State.PUBLIC,
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["search", "not_gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "google_search",
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
                "LOCATION": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "Germany",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "LANGUAGE": {
                    "selectionType": SelectionType.STRING.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value
                    ]
                },
                "GEOLOCATION": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "de",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "API_KEY": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "<API-KEY-GOES-HERE>",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "RESPONSE_SIZE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "full",
                    "description": "choose \"compact\" to only get text snippet of the first result",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )

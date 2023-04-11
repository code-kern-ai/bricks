from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import nyt_news_search, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=nyt_news_search,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=209,
        tabler_icon="News",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["search", "not_gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "nyt_news_search",
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
                "API_KEY": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "<api-key-goes-here>",
                    "description": "go here for free API key https://developer.nytimes.com/",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "OUTPUT_SIZE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "full",
                    "description": "choose \"compact\" to only get the text of the first result",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )
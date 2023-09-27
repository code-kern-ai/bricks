from util.configs import build_classifier_premium_config
from util.enums import State, SelectionType, BricksVariableType, RefineryDataType
from . import distilbert_stock_news_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_premium_config(
        function=distilbert_stock_news_classifier,
        input_example=INPUT_EXAMPLE,
        issue_id=304,
        tabler_icon="ZoomMoney",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="premium",

        available_for=["refinery", "common"],
        part_of_group=[
            "llm",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping=None,
        integrator_inputs={
            "name": "distilbert_stock_news_classifier",
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
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
            }
        }
    )
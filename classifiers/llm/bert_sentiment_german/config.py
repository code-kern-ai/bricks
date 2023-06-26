from util.configs import build_classifier_premium_config
from util.enums import State, SelectionType, BricksVariableType, RefineryDataType
from . import bert_sentiment_german, INPUT_EXAMPLE


def get_config():
    return build_classifier_premium_config(
        function=bert_sentiment_german,
        input_example=INPUT_EXAMPLE,
        issue_id=311,
        tabler_icon="Sausage",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="false",
        type="premium",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "llm",
            "sentiment",
            "not_gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "bert_sentiment_german",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "Positive",
                "Neutral",
                "Negative",
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "API_KEY": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
            }
        }
    )
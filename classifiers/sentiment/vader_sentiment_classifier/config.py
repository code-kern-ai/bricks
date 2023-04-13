from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, SelectionType, BricksVariableType
from . import vader_sentiment_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        # strapi information
        function=vader_sentiment_classifier,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=157,
        tabler_icon="MoodCrazyHappy",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
        type="python_function",
        gdpr_compliant="true",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "sentiment",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "vader_sentiment_classifier",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "positive",
                "neutral",
                "negative",
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

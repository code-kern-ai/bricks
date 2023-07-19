from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import textblob_sentiment, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        # strapi information
        function=textblob_sentiment,
        input_example=INPUT_EXAMPLE,
        issue_id=27,
        tabler_icon="MoodSmileBeam",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "sentiment",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "textblob_sentiment",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "very positive",
                "positive",
                "neutral",
                "negative",
                "very negative",
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

from util.configs import build_classifier_premium_config
from util.enums import State, SelectionType, BricksVariableType, RefineryDataType
from . import deberta_review_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_premium_config(
        function=deberta_review_classifier,
        input_example=INPUT_EXAMPLE,
        issue_id=302,
        tabler_icon="MoodNerd",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="premium",

        available_for=["refinery", "common"],
        part_of_group=[
            "llm",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping="none",
        integrator_inputs={
            "name": "deberta_review_classifier",
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
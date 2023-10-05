from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import chunked_sentence_complexity, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=chunked_sentence_complexity,
        input_example=INPUT_EXAMPLE,
        issue_id=351,
        tabler_icon="ThreeDCubeSphere",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "reference_quality",
            "text_analysis"
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "chunked_sentence_complexity",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "very easy",
                "easy",
                "fairly easy",
                "standard",
                "fairly difficult",
                "difficult",
                "very difficult",
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "TARGET_LANGUAGE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "supported iso codes",
                    "defaultValue": "en",
                    "allowedValues": ["en", "de", "es", "fr", "it", "nl", "ru"],
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

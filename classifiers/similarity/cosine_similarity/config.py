from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import cosine_similarity, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=cosine_similarity,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=79,
        tabler_icon="WaveSine",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        integrator_inputs={
            "name": "cosine_similarity",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "Not similar",
                "Somewhat similar",
                "Very similar"
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "SUBJECT_TEXT": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "Ten amazing facts about the sun",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )

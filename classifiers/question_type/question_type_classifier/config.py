from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import question_type_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=question_type_classifier,
        input_example=INPUT_EXAMPLE,
        issue_id=344,
        tabler_icon="ZoomQuestion",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "question_type"
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "question_type_classifier",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": ["Keyword-question", "Statement-question", "Interrogative-question"],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "MODEL_NAME": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "KernAI/multilingual-e5-question-type",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "REQUEST_URL": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "https://free.api.kern.ai/inference",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )
from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import communication_style_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=communication_style_classifier,
        input_example=INPUT_EXAMPLE,
        issue_id=343,
        tabler_icon="CircleDotted",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "communication_style"
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "communication_style_classifier",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": ["Action-seeking", "Fact-oriented", "Information-seeking", "Self-revealing"],
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
                    "defaultValue": "KernAI/multilingual-e5-communication-style",
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
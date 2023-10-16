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
            "query_check"
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "question_type_classifier",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "text",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "API_KEY": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )
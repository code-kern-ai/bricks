from util.configs import build_classifier_function_config
from util.enums import State, BricksVariableType, RefineryDataType, SelectionType
from . import sentence_complete_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        # strapi information
        function=sentence_complete_classifier,
        input_example=INPUT_EXAMPLE,
        issue_id=349,
        tabler_icon="LanguageKatakana",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "reference_quality",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping = {
            "incomplete": "Needs fix",
            "complete": "null"
        },
        integrator_inputs={
            "name": "sentence_complete_classifier",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
            }
        }      
    )

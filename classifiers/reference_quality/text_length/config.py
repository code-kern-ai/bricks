from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, SelectionType, BricksVariableType
from . import text_length, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=text_length,
        input_example=INPUT_EXAMPLE,
        issue_id=348,
        tabler_icon="RulerMeasure",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "reference_quality",
            "text_analysis"
        ],  # first entry should be parent directory
        # mapping lables for cognition
        cognition_init_mapping={
            "short": "Needs fix",
            "medium": "null",
            "long": "null",
        },
        # bricks integrator information
        integrator_inputs={
            "name": "text_length",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "short",
                "medium", 
                "long"
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.STRING.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                }
            },
        },
    )

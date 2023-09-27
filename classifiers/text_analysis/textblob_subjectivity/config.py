from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, SelectionType, BricksVariableType
from . import textblob_subjectivity, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=textblob_subjectivity,
        input_example=INPUT_EXAMPLE,
        issue_id=28,
        tabler_icon="Books",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",

        available_for=["refinery", "common"],
        part_of_group=[
            "text_analysis",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping="none",
        integrator_inputs={
            "name": "textblob_subjectivity",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "subjective",
                "rather subjective",
                "neutral",
                "rather objective",
                "objective",
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                }
            },
        },
    )

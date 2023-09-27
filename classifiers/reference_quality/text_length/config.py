from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, SelectionType, BricksVariableType
from . import text_length, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=text_length,
        input_example=INPUT_EXAMPLE,
        issue_id=28,
        tabler_icon="Books",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "reference_quality",
            "text_analysis"
        ],  # first entry should be parent directory
        # mapping information for cognition
        cognition_mapping={
            "short": "Needs fix",
            "medium": "Sufficient",
            "long": "Sufficient",
        },
        # bricks integrator information
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

from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import hashtag_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=hashtag_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=19,
        tabler_icon="Hash",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",

        available_for=["refinery", "common"],
        part_of_group=[
            "symbols",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping="none",
        integrator_inputs={
            "name": "hashtag_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "hashtag",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

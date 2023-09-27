from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import hamming_distance, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=hamming_distance,
        input_example=INPUT_EXAMPLE,
        issue_id=110,
        tabler_icon="ArrowsMoveHorizontal",
        min_refinery_version="1.7.0",
        state=State.DRAFT.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "distance",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "hamming_distance",
            "refineryDataType": RefineryDataType.FLOAT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "BASE_SENTENCE": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "This is the base sentence you want to find the distances to.",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

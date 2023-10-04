from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import manhattan_distance, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=manhattan_distance,
        input_example=INPUT_EXAMPLE,
        issue_id=231,
        tabler_icon="Stairs",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "distance",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "manhattan_distance",
            "refineryDataType": RefineryDataType.FLOAT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "SUBJECT_TEXT": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "Insert the sentence you want to compare your records to here!",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
            },
        },
    )

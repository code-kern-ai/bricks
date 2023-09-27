from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import reading_time, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=reading_time,
        input_example=INPUT_EXAMPLE,
        issue_id=20,
        tabler_icon="ClockPlay",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",

        available_for=["refinery", "common"],
        part_of_group=[
            "text_analytics",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping=None,
        integrator_inputs={
            "name": "reading_time",
            "refineryDataType": RefineryDataType.FLOAT.value,
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

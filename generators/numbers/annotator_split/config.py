from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import annotator_split, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=annotator_split,
        input_example=INPUT_EXAMPLE,
        issue_id=240,
        tabler_icon="Dice-3",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "numbers",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "annotator_split",
            "refineryDataType": RefineryDataType.INTEGER.value,
            "variables": {
                "N_SPLIT": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "only text fields",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

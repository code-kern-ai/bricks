from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import string_lenght, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=string_lenght,
        input_example=INPUT_EXAMPLE,
        issue_id=337,
        tabler_icon="ruler-measure",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "text_analytics",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "string_lenght",
            "refineryDataType": RefineryDataType.INTEGER.value,
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

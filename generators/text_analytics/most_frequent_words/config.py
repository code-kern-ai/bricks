from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import most_frequent_words, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=most_frequent_words,
        input_example=INPUT_EXAMPLE,
        issue_id=240,
        tabler_icon="Stack3",
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
            "name": "most_frequent_words",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "only text fields",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "N_WORDS": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 5,
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
            },
        },
    )

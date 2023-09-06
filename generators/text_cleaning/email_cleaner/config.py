from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import email_cleaner, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=email_cleaner,
        input_example=INPUT_EXAMPLE,
        issue_id=328,
        tabler_icon="square-rounded-letter-e",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "text_cleaning",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "email_cleaner",
            "refineryDataType": RefineryDataType.TEXT.value,
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
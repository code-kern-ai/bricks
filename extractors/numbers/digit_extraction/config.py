from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import digit_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=digit_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=46,
        tabler_icon="Number",
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
            "name": "digit_extraction",
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
                "MAX_NUMBER_LENGTH": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 4,
                    "description": "maximum amount of digits to be considered relevant",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "digit",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

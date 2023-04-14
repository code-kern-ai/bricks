from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import phonetic_soundex, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=phonetic_soundex,
        input_example=INPUT_EXAMPLE,
        issue_id=107,
        tabler_icon="Volume",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="true",
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "text_analytics",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "phonetic_soundex",
            "refineryDataType": RefineryDataType.TEXT.value,
            "globalComment": "This is meant for names",
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

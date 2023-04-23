from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import smalltalk_truncation, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=smalltalk_truncation,
        input_example=INPUT_EXAMPLE,
        issue_id=124,
        tabler_icon="MessageDots",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="true",
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "summarization",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "smalltalk_truncation",
            "refineryDataType": RefineryDataType.TEXT.value,
            "globalComment": "currently only english language is supported here",
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

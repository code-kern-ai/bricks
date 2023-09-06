from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import pdf_scanner, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=pdf_scanner,
        input_example=INPUT_EXAMPLE,
        issue_id=329,
        tabler_icon="file-type-pdf",
        min_refinery_version="1.7.1",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "sentiment",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "pdf_scanner",
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

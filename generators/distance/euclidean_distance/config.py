from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import euclidean_distance, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=euclidean_distance,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=230,
        tabler_icon="VectorTriangle",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="true",
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "distance",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "euclidean_distance",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "SUBJECT_TEXT": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "Ten amazing facts about the sun",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

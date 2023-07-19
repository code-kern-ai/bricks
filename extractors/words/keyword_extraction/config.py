from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import keyword_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=keyword_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=55,
        tabler_icon="Key",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "words",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "keyword_extraction",
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
                "KEYWORDS": {
                    "selectionType": SelectionType.LIST.value,
                    "defaultValue": "keyword1",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "keyword",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

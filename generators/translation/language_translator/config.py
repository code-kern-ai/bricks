from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import language_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=language_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=81,
        tabler_icon="Language",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="false",
        type="premium",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "translation",
            "not_gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "language_translator",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "ORIGINAL_LANGUAGE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "only iso format",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "TARGET_LANGUAGE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "only iso format",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )

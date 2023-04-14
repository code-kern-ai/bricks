from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import cosine_similarity, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=cosine_similarity,
        input_example=INPUT_EXAMPLE,
        issue_id=79,
        tabler_icon="WaveSine",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="true",
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "similarity",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        integrator_inputs={
            "name": "cosine_similarity",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": ["Not similar", "Somewhat similar", "Very similar"],
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
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
            },
        },
    )

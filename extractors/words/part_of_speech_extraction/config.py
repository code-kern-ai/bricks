from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import part_of_speech_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=part_of_speech_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=53,
        tabler_icon="TopologyStar3",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["words", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "part_of_speech_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "ADJ",
                "ADP",
                "ADV",
                "AUX",
                "CONJ",
                "CCONJ",
                "DET",
                "INTJ",
                "NOUN",
                "NUM",
                "PART",
                "PRON",
                "PROP",
                "PUNCT",
                "SCONJ",
                "SYM",
                "VERB",
                "X",
                "SPACE"
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )

from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import phonetic_transcriptor, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=phonetic_transcriptor,
        input_example=INPUT_EXAMPLE,
        issue_id=278,
        tabler_icon="AlphabetGreek",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "phonetic_transcription",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "phonetic_transcriptor",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LANGUAGE_CODE": {
                    "selectionType": SelectionType.STRING.value,
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            },
        },
    )

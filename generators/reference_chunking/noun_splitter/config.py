from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import noun_splitter, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=noun_splitter,
        input_example=INPUT_EXAMPLE,
        issue_id=384,
        tabler_icon="ArrowMerge",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "reference_chunking",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "noun_splitter",
            "refineryDataType": RefineryDataType.EMBEDDING_LIST.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )
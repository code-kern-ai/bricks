from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import text_summarization, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=text_summarization,
        input_example=INPUT_EXAMPLE,
        issue_id=183,
        tabler_icon="Writing",
        min_refinery_version="1.7.0",
        state=State.DRAFT.value,
        type="python_function",

        available_for=["refinery", "common"],
        part_of_group=[
            "summarization",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping=None,
        integrator_inputs={
            "name": "text_summarization",
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

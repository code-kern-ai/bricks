from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import newline_splitter, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=newline_splitter,
        input_example=INPUT_EXAMPLE,
        issue_id=367,
        tabler_icon="Slice",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "reference_chunking",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "domain_parser",
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

            },
        },
    )

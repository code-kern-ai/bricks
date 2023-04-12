from util.configs import build_generator_function_config
from util.enums import State
from . import manhattan_distance, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=manhattan_distance,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=231,
        tabler_icon="Stairs",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )

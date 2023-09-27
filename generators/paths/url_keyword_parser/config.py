from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import url_keyword_parser, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=url_keyword_parser,
        input_example=INPUT_EXAMPLE,
        issue_id=163,
        tabler_icon="Cut",
        min_refinery_version="1.8.1",
        state=State.PUBLIC.value,
        type="python_function",

        available_for=["refinery", "common"],
        part_of_group=[
            "paths",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping="none",
        integrator_inputs={
            "name": "url_keyword_parser",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "only text like attributes",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "INCLUDE_DOMAIN": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "false",
                    "description": "include URL domain in keyword scan",
                    "addInfo": [BricksVariableType.GENERIC_BOOLEAN.value],
                },
                "INCLUDE_PARAMETER": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "true",
                    "description": "inlude URL parameter in keyword scan",
                    "addInfo": [BricksVariableType.GENERIC_BOOLEAN.value],
                },
                "CHECK_VALID_URL": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "false",
                    "description": "ensure valid URL pattern",
                    "addInfo": [BricksVariableType.GENERIC_BOOLEAN.value],
                },
                "REMOVE_NONE_ENGLISH": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "false",
                    "description": "only use words that are part of nltk.corpus words",
                    "addInfo": [BricksVariableType.GENERIC_BOOLEAN.value],
                },
                "REMOVE_STOPWORDS": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "true",
                    "description": "only uses words that are not part of nltk.corpus stopwords",
                    "addInfo": [BricksVariableType.GENERIC_BOOLEAN.value],
                },
                "REMOVE_HEX_LIKE": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "true",
                    "description": "remove things that look like hex or numbers",
                    "addInfo": [BricksVariableType.GENERIC_BOOLEAN.value],
                },
                "TEXT_SEPARATOR": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": ", ",
                    "description": "joins resulting keywords on",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "SPLIT_REGEX": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "\\W",
                    "description": "possible regex, default is any none word char e.g. \\W|_ to include underscores",
                    "addInfo": [BricksVariableType.REGEX.value],
                },
                "WORD_WHITE_LIST": {
                    "selectionType": SelectionType.STRING.value,
                    "description": "optional, specify words that are exempt form remove checks",
                    "optional": "true",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
            },
        },
    )

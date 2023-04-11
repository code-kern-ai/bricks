from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import url_keyword_parser, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=url_keyword_parser,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=163,
        tabler_icon="Cut",
        min_refinery_version="1.8.1",
        state=State.PUBLIC.value,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["paths", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "url_keyword_parser",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "only text like attributes",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "INCLUDE_DOMAIN": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "False",
                    "description": "include URL domain in keyword scan",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_BOOLEAN.value
                    ]
                },
                "INCLUDE_PARAMETER": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "True",
                    "description": "inlude URL parameter in keyword scan",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_BOOLEAN.value
                    ]
                },
                "CHECK_VALID_URL": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "False",
                    "description": "ensure valid URL pattern",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_BOOLEAN.value
                    ]
                },
                "REMOVE_NONE_ENGLISH": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "False",
                    "description": "only use words that are part of nltk.corpus words",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_BOOLEAN.value
                    ]
                },
                "REMOVE_STOPWORDS": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "True",
                    "description": "only uses words that are not part of nltk.corpus stopwords",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_BOOLEAN.value
                    ]
                },
                "REMOVE_HEX_LIKE": {
                    "selectionType": SelectionType.BOOLEAN.value,
                    "defaultValue": "True",
                    "description": "remove things that look like hex or numbers",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_BOOLEAN.value
                    ]
                },
                "TEXT_SEPERATOR": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": ", ",
                    "description": "joins resulting keywords on",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "SPLIT_REGEX": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "\\W",
                    "description": "possible regex, default is any none word char e.g. \\W|_ to include underscores",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.REGEX.value
                    ]
                },
                "WORD_WHITE_LIST": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "optional, specify words that are exempt form remove checks",
                    "optional": "true",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )

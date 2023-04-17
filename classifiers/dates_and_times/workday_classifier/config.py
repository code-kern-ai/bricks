from util.configs import build_classifier_function_config
from util.enums import State, SelectionType, RefineryDataType, BricksVariableType
from . import workday_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=workday_classifier,
        input_example=INPUT_EXAMPLE,
        issue_id=161,
        tabler_icon="CalendarEvent",
        min_refinery_version="1.7.0",
        state=State.DRAFT.value,  # change to public once refinery exec env requirements are met
        type="python_function",
        gdpr_compliant="true",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "dates_and_times",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "workday_classifier",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "Workday",
                "Holiday",
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "COUNTRY_ID": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "DE",
                    "description": "Uses ISO country codes",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
            },
        },
    )

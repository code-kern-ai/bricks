from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import pegasus_summarization, INPUT_EXAMPLE


def get_config():
      return build_generator_premium_config(
            function=pegasus_summarization,
            input_example=INPUT_EXAMPLE,
            issue_id=321,
            tabler_icon="TextResize",
            min_refinery_version="1.7.0",
            state=State.PUBLIC.value,
            type="premium",
            kern_token_proxy_usable="false",
            docker_image="none",
            gdpr_compliant="false",
            available_for=["refinery", "common"],
            part_of_group=[
                  "llm",
                  "summarization"
                  "not_gdpr_compliant",
            ],  # first entry should be parent directory
            # bricks integrator information
            integrator_inputs={
            "name": "pegasus_summarization",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                  "API_KEY": {
                        "selectionType": SelectionType.STRING.value,
                        "defaultValue": "<API_KEY_GOES_HERE>",
                        "addInfo": [BricksVariableType.GENERIC_STRING.value],
                  },
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
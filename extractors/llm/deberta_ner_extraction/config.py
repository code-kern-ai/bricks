from util.configs import build_extractor_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import deberta_ner_extraction, INPUT_EXAMPLE


def get_config():
      return build_extractor_premium_config(
            function=deberta_ner_extraction,
            input_example=INPUT_EXAMPLE,
            issue_id=307,
            tabler_icon="Article",
            min_refinery_version="1.7.0",
            state=State.PUBLIC.value,
            type="premium",
            kern_token_proxy_usable="false",
            docker_image="none",
            available_for=["refinery", "common"],
            part_of_group=[
                  "llm",
                  "words"
            ],  # first entry should be parent directory
            # bricks integrator information
            integrator_inputs={
            "name": "deberta_ner_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                  "person",
                  "organization", 
                  "location",
                  "building", 
                  "event",
                  "product", 
                  "art",
                  "other",
            ],
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
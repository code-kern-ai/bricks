from util.configs import build_extractor_learner_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import crf_tagger


def get_config():
    return build_extractor_learner_config(
        function=crf_tagger,
        issue_id=43,
        tabler_icon="BracketsContain",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="active_learner",
        gdpr_compliant="true",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery"],
        part_of_group=[
            "active_learner",
            "gdpr_compliant",
        ],
        integrator_inputs={
            "name": "MyCRF",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "EMBEDDING": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "text-classification-distilbert-base-uncased",
                    "description": "pick this from the options above",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "MIN_CONFIDENCE": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 0.8,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_FLOAT.value
                    ]
                },
                "LABELS": {
                    "selectionType": SelectionType.STRING.value,
                    "description": "optional, you can specify a list to filter the predictions (e.g. [\"label-a\", \"label-b\"])",
                    "optional": "true",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )

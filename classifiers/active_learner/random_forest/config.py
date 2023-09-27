from util.configs import build_classifier_learner_config
from util.enums import State, RefineryDataType, SelectionType, BricksVariableType
from . import random_forest


def get_config():
    return build_classifier_learner_config(
        function=random_forest,
        issue_id=51,
        tabler_icon="BinaryTree2",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="active_learner",
        available_for=["refinery"],
        part_of_group=[
            "active_learner",
        ],
        integrator_inputs={
            "name": "MyRF",
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
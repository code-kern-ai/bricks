from util.configs import build_classifier_learner_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType

from . import bayesian_optimization


def get_config():
    return build_classifier_learner_config(
        function=bayesian_optimization,
        issue_id=188,
        tabler_icon="ChartDots",
        min_refinery_version="1.8.1",
        state=State.DRAFT.value,
        type="active_learner",
        available_for=["refinery"],
        part_of_group=[
            "active_learner",
        ],
        integrator_inputs={
            "name": "MyBayesian",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "EMBEDDING": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "text-classification-distilbert-base-uncased",
                    "description": "pick this from the options above",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "MIN_CONFIDENCE": {
                    "selectionType": SelectionType.FLOAT.value,
                    "defaultValue": 0.8,
                    "addInfo": [
                        BricksVariableType.GENERIC_FLOAT.value
                    ]
                },
                "ITERATIONS": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 100,
                    "description": "this can be modified by the user",
                    "addInfo": [
                        BricksVariableType.GENERIC_INT.value
                    ]
                },
                "LABELS": {
                    "selectionType": SelectionType.STRING.value,
                    "description": "optional, you can specify a list to filter the predictions (e.g. [\"label-a\", \"label-b\"])",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
)


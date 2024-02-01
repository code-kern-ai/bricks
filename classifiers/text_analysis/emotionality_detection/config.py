from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, SelectionType, BricksVariableType
from . import emotionality_detection, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=emotionality_detection,
        input_example=INPUT_EXAMPLE,
        issue_id=97,
        tabler_icon="MoodSad2",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "text_analysis",
        ],  # first entry should be parent directory
        # bricks integrator information
              integrator_inputs={
            "name": "emotionality_detection",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                  "anger", 
                  "disgust",
                  "fear",
                  "joy",
                  "sadness", 
                  "neutral",
                  "suprise"
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
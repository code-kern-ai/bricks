from enum import Enum


class State(Enum):
    DRAFT = "draft"
    PUBLIC = "public"
    
class SelectionType(Enum):
    STRING = "string"
    CHOICE = "choice"
    RANGE = "range"
    INTEGER = "integer"
    FLOAT = "float"

class BricksVariableType(Enum):
    ATTRIBUTE = "attribute",
    LANGUAGE = "language",
    LABELING_TASK = "labeling_task",
    LABEL = "label",
    EMBEDDING = "embedding",
    LOOKUP_LIST = "lookup_list",
    REGEX = "regex",
    GENERIC_STRING = "generic_string",
    GENERIC_INT = "generic_int",
    GENERIC_FLOAT = "generic_float",
    GENERIC_BOOLEAN = "generic_boolean",
    UNKNOWN = "unknown",

class RefineryDataType(Enum):
    CATEGORY = "category"
    TEXT = "text"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
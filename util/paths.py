from re import finditer


def camel_case_to_snake_case(text):
    matches = finditer(".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)", text)
    return "_".join([match.group(0) for match in matches]).lower()


def snake_case_to_camel_case(text):
    text_cased = "".join([word.capitalize() for word in text.split("_")])
    return text_cased[0].lower() + text_cased[1:]

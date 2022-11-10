```python
import language_tool_python
from typing import Dict, Any

def grammar_check(record: Dict[str, Any]):
    lang = language_tool_python.LanguageTool("en-US")
    text = record["error_text"]
    my_match = lang.check(text)
    start = []
    end = []
    mistakes = []
    corrections = []
    for rules in my_match:
        if len(rules.replacements) > 0:
            start.append(rules.offset)
            end.append(rules.errorLength + rules.offset)
            mistakes.append(text[rules.offset : rules.errorLength + rules.offset])
            corrections.append(rules.replacements[0])
    corrected_text = list(text)
    for n, _ in enumerate(start):
        for i, _ in enumerate(text):
            corrected_text[start[n]] = corrections[n]
            if start[n] < i < end[n]:
                corrected_text[i] = ""

    corrected_text = "".join(corrected_text)

    return {
        "mistakes": mistakes,
        "corrections": corrections,
        "correctedText": corrected_text,
    }
```
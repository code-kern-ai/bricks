```python
import epitran
import jieba
import re
from typing import Dict, List

def phonetic_transcriptor(text: str, language_code: str) -> Dict[str, List[str]]:
    # Tokenize based on language group
    language_group = language_code.split('-')[1]
    # Handle the case of Chinese lanugage separatly 
    if language_code in ('cmn-Hans', 'cmn-Hant'):
        text_without_punctuation = ''.join(re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf\u20000-\u2a6df]+', text))
        # Use tokenizer for Chinese
        tokens = [*jieba.cut(text_without_punctuation)]
        # Provide path to CEDICT - dictionary database that provides English definitions for Chinese characters
        cedict_path = "cedict_1_0_ts_utf-8_mdbg.txt"
        epi = epitran.Epitran(language_code, cedict_file=cedict_path)             
        result = [epi.transliterate(token) for token in tokens]
        return {"tokens": tokens,
                "phonetic_transcriptions": result}

    if language_group == 'Arab':
        # Tokenize Arabic script using regex
        tokens = re.findall(r'[\u0600-\u06FF]+', text)
    elif language_group == 'Beng':
        # Tokenize Bengali script using regex
        tokens = re.findall(r'[\u0980-\u09FF]+', text)
    elif language_group == 'Cyrl':
        # Tokenize Cyrillic script using regex
        tokens = re.findall(r'[\u0400-\u04FF]+', text)
    elif language_group == 'Deva':
        # Tokenize Devanagari script using regex
        tokens = re.findall(r'[\u0900-\u0963\u0966-\u097F]+', text)
    elif language_group == 'Ethi':
        # Tokenize Ethiopic script using regex
        tokens = re.findall(r'[\u1200-\u137F]+', text)
    elif language_group == 'Guru':
        # Tokenize Gurmukhi script using regex
        tokens = re.findall(r'[\u0A00-\u0A7F]+', text)
    elif language_group == 'Khmr':
        # Tokenize Khmer script using regex
        tokens = re.findall(r'[\u1780-\u17FF]+', text)
    elif language_group == 'Laoo':
        # Tokenize Lao script using regex
        tokens = re.findall(r'[\u0E80-\u0EFF]+', text)
    elif language_group == 'Latn':
        # Tokenize Latin script using 
        tokens = re.findall(r'\b\w+\b', text)
    elif language_group == 'Mlym':
        # Tokenize Malayalam script using 
        tokens = re.findall(r'[\u0D00-\u0D7F]+', text)
    elif language_group == 'Mymr':
        # Tokenize Burmese script using regex
        tokens = re.findall(r'[\u1000-\u109F]+', text)
    elif language_group == 'Orya':
        # Tokenize Oriya script using regex
        tokens = re.findall(r'[\u0B00-\u0B7F]+', text)
    elif language_group == 'Sinh':
        # Tokenize Sinhala script using regex
        tokens = re.findall(r'[\u0D80-\u0DFF]+', text)
    elif language_group == 'Syrc':
        # Tokenize Syriac script using regex
        tokens = re.findall(r'[\u0700-\u074F]+', text)
    elif language_group == 'Taml':
        # Tokenize Tamil script using regex
        tokens = re.findall(r'[\u0B80-\u0BFF]+', text)
    elif language_group == 'Telu':
        # Tokenize Telugu script using regex
        tokens = re.findall(r'[\u0C00-\u0C7F]+', text)
    elif language_group == 'Thai':
        # Tokenize Thai script using regex
        tokens = re.findall(r'[\u0E00-\u0E7F]+', text)
    
    epi = epitran.Epitran(language_code)
    result = [epi.transliterate(token) for token in tokens]
    return {"tokens": tokens,
            "phonetic_transcriptions": result}
    
# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = [
        "Clouds drift across the clear blue sky.",
        "Wolken ziehen über den klaren blauen Himmel.",
        "云彩在晴朗的蓝天中飘过。",
        "बादल साफ़ नीले आकाश में तैरते हैं।"]
    language_codes = ["eng-Latn", "deu-Latn-np", "cmn-Hans", "hin-Deva"]
    for text, language_code in zip (texts, language_codes):
        print(f"Phonetic transcription for \"{text}\" is: {phonetic_transcriptor(text, language_code)}")

example_integration()
```

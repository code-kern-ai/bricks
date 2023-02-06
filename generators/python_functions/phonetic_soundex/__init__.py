import unicodedata
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "word": "Viking."
}

class PhoneticSoundexModel(BaseModel):
    word: str
    # if required, add more attributes here

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def phonetic_soundex(req: PhoneticSoundexModel):
    """Converts an english word into a phonetic SoundEx representation, for example to store names."""

    input_ = req.word

    soundex_list = []
    for word in input_.split():
        word = unicodedata.normalize("NFKD", word)
        word = word.upper()

        replacements = (
            ("BFPV", "1"),
            ("CGJKQSXZ", "2"),
            ("DT", "3"),
            ("L", "4"),
            ("MN", "5"),
            ("R", "6"),
        )
        result = [word[0]]
        count = 1

        # find would-be replacment for first character
        for lset, sub in replacements:
            if word[0] in lset:
                last = sub
                break
        else:
            last = None

        for letter in word[1:]:
            for lset, sub in replacements:
                if letter in lset:
                    if sub != last:
                        result.append(sub)
                        count += 1
                    last = sub
                    break
            else:
                if letter != "H" and letter != "W":
                    # leave last alone if middle letter is H or W
                    last = None
            if count == 4:
                break

        result += "0" * (4 - count)
        soundex_list.append("".join(result))
    
    return {"SoundEx": " ".join(soundex_list)}
```python
import textstat
from typing import List, Tuple
import re
import spacy

def difficult_words_extraction(text: str, extraction_keyword: str, syllable_threshold: int) -> List[Tuple[str, int]]:
      """
      @param text: text to extract from
      @param syllable_threshold: threshold for the number of syllables in a word
      """
      nlp = spacy.load("en_core_web_sm")
      doc = nlp(text)

      difficult_words = textstat.difficult_words_list(text, syllable_threshold)

      text = text.replace(".", " .").replace(",", " ,").replace("!", " !").replace("?", " ?") # add space before punctuation

      difficult_word_positions = []
      for word in difficult_words: 
            start, end = re.search(rf"({word})", text).span() # get the position of the word in the text
            span = doc.char_span(start, end, alignment_mode="expand")
            difficult_word_positions.append([extraction_keyword, span.start, span.end])
      return difficult_word_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
      texts = ["My cat is eleven years old.", "My Dad plays the saxophone.", "My brother mows the lawn with our lawnmower.", "The butterfly is colorful."]
      extraction_keyword = "difficult_word"
      syllable_threshold = 3
      for text in texts:
            found = difficult_words_extraction(text, extraction_keyword, syllable_threshold)
            if found:
                  print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
            else:
                  print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()

```
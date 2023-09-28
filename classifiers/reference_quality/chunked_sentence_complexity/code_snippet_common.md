```python
from collections import Counter
import textstat
import spacy

# Load the Spacy model
nlp = spacy.load('en_core_web_sm')

def sentence_complexity(text: str, language: str = "en")->str:    
    """
    @param text: text to check
    @return: either 'very difficult', 'difficult', 'fairly difficult', 'standard', 'fairly easy', 'easy' or 'very easy' depending on the score
    """
    textstat.set_lang(language)
    return lookup_label(textstat.flesch_reading_ease(text))

def lookup_label(score:int) -> str:
    if score < 30:
        return "very difficult"
    if score < 50:
        return "difficult"
    if score < 60:
        return "fairly difficult"
    if score < 70:
        return "standard"
    if score < 80:
        return "fairly easy"
    if score < 90:
        return "easy"        
    return "very easy"

def calculate_sentence_complexity(text: str) -> str:
    # Use Spacy for sentence tokenization
    doc = nlp(text)
    
    complexities = []
    for sent in doc.sents:
        # Apply the complexity function to each sentence
        complexity = sentence_complexity(sent.text)
        complexities.append(complexity)
    
    # find the item with the highest count
    counter = Counter(complexities)
    max_item = max(counter.items(), key=lambda x: x[1])

    # check if there are other items with the same count
    same_count_items = [item for item, count in counter.items() if count == max_item[1]]

    if len(same_count_items) > 1:
        print("Couldn't find highest value")
    else:
        return max_item[0]

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Doctors from Stockhold University invent cure for rare disease.", "Mary had a little lamb.", """Once upon a time, in a small town, there lived a little girl named Lily. She was known for her kindness and love for nature. Every morning, she would wake up early and go to the garden to water her plants. She had a variety of flowers, but her favorite were the sunflowers. They stood tall and bright, bringing joy to everyone who saw them.

One day, a new family moved into the house next door. They had a son named Max. Max was shy and found it hard to make friends in the new town. Seeing this, Lily decided to help. She invited Max to help her in the garden. Together, they planted more sunflowers and watered them daily.

As the sunflowers grew, so did their friendship. Max was no longer the shy boy he used to be. He made many friends and was happy in his new home. And Lily was glad she could help. Doctors from Stockhold University invent cure for rare disease. From then on, they became the best of friends, all thanks to the sunflowers in Lily's garden.
"""]
    target_language = "en"
    textstat.set_lang("en") #en, de, es, fr, it, nl, ru
    for text in texts:
        print(f"\"{text}\" is {calculate_sentence_complexity(text)}")

example_integration()
```
```python
from collections import Counter
import textstat
import spacy

def sentence_complexity(text: str)-> str:    
    """
    @param text: text to check
    @return: either 'very difficult', 'difficult', 'fairly difficult', 'standard', 'fairly easy', 'easy' or 'very easy' depending on the score
    """
    score = textstat.flesch_reading_ease(text)
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

def chunked_sentence_complexity(text: str, language: str = "en", spacy_model: str = "en_core_web_sm") -> str:
    """
    @param text: 
    @param language: iso language code
    @spacy model: name of a language model from SpaCy 
    @return: aggregated reading ease score of a whole text
    """
    textstat.set_lang(language)
    nlp = spacy.load(spacy_model)
    doc = nlp(text)
    
    complexities = []
    for sent in doc.sents:
        # Apply the complexity function to each sentence
        complexity = sentence_complexity(sent.text)
        complexities.append(complexity)

    counter = Counter(complexities)
    
    # aggregating the complexity
    complexity_scores = {"very easy": 1, "easy": 2, "fairly easy": 3, "standard": 4, "fairly difficult": 5, "difficult": 6, "very difficult": 7}

    total_score = 0
    total_count = 0
    for comp, count in counter.items():
        total_score += complexity_scores[comp] * count
        total_count += count

    # weighted average complexity
    average_complexity = total_score / total_count

    # create a reverse mapping from scores to complexity levels
    reverse_mapping = {v: k for k, v in complexity_scores.items()}

    # find the closest complexity level to the average complexity
    closest_complexity = min(reverse_mapping.keys(), key=lambda x: abs(x - average_complexity))
    return reverse_mapping[closest_complexity]
    

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 


def example_integration():
    texts = [
    """
    In a small town, there lived a humble baker named Thomas. He was known for his delicious pastries, which were loved by everyone in the town. Every morning, he would wake up early to prepare the dough for his pastries. He would then bake them in his old but reliable oven.
    One day, a stranger came to the town. He had heard about Thomas's pastries and wanted to try them. He went to the bakery and ordered a pastry. As he took his first bite, his eyes lit up with delight. He praised Thomas for his skill and promised to spread the word about his bakery.
    Word of Thomas's pastries spread far and wide. People from neighboring towns started visiting his bakery. Despite the increase in customers, Thomas remained humble. He continued to wake up early every morning to prepare his pastries, ensuring that each one was made with care.
    Thomas's story is a reminder that passion and dedication can lead to success. It shows that humility and hard work are respected and rewarded. His delicious pastries were not just food items but a source of joy for everyone who tasted them.
    """
    ]
    language = "en" # other languages: de, es, fr, it, nl, ru
    spacy_model = "en_core_web_sm"
    for text in texts:
        print(f"\"{text}\" is {chunked_sentence_complexity(text, language, spacy_model)}")

example_integration()
```
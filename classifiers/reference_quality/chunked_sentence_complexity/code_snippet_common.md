```python
import textstat
import spacy

def get_mapping_complexity(score: int)-> str:    
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

spacy_models_loaded = {}

def get_spacy(spacy_model: str):
    global spacy_models_loadeda
    if spacy_model not in spacy_models_loaded:
        spacy_models_loaded[spacy_model] = spacy.load(spacy_model)
    return spacy_models_loaded[spacy_model]

def chunked_sentence_complexity_v2(text: str, language: str = "en", spacy_model: str = "en_core_web_sm") -> str:
    """
    @param text: 
    @param language: iso language code
    @spacy model: name of a language model from SpaCy 
    @return: aggregated reading ease score of a whole text
    """
    textstat.set_lang(language)
    nlp = get_spacy(spacy_model)
    doc = nlp(text)

    complexities = [textstat.flesch_reading_ease(sent.text) for sent in doc.sents]
    avg = int(round(sum(complexities) / len(complexities)))
    return get_mapping_complexity(avg)


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
        print(f"\"{text}\" is {chunked_sentence_complexity(text, language)}")

example_integration()
```
```python
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

# replace this list with a list containing your data
text = ["""There was a time when he would have embraced the change that was coming. In his youth, he sought 
    adventure and the unknown, but that had been years ago. He wished he could go back and learn to find the 
    excitement that came with change but it was useless. That curiosity had long left him to where he had come to 
    loathe anything that put him out of his comfort zone."""]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def summarize(record):
    nlp = spacy.load("en_core_web_sm")
    summarized_text = []
    for entry in record["text"]:
        doc = nlp(entry)
        word_frequencies={}
        for word in doc:
            if word.text.lower() not in list(STOP_WORDS):
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1
        max_frequency=max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word]=word_frequencies[word]/max_frequency
        sentence_tokens= [sent for sent in doc.sents]
        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():                            
                        sentence_scores[sent]=word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent]+=word_frequencies[word.text.lower()]
        select_length=int(len(sentence_tokens)*0.5)
        summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
        final_summary=[word.text for word in summary]
        summarized_text.append(''.join(final_summary))
    return {"summaries": summarized_text}
```
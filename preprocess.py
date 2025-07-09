import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import string

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    text = text.lower()
    doc = nlp(text)
    
    # Remove stopwords, punctuation, and lemmatize
    tokens = [
        token.lemma_ 
        for token in doc 
        if token.text not in STOP_WORDS 
        and token.text not in string.punctuation
    ]
    
    return " ".join(tokens)
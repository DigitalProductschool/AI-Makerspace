from keybert import KeyBERT
import pandas as pd

stoppath = "stop-list-deutsch.txt"

def load_stop_words(stop_word_file):
    stop_words = []
    for line in open(stop_word_file):
        if line.strip()[0:1] != "#":
            for word in line.split():
                stop_words.append(word)
    return stop_words


def generate_key_words(desc):
    stop_words = load_stop_words(stoppath)
    kw_model = KeyBERT(model="xlm-r-bert-base-nli-stsb-mean-tokens")
    kwr = kw_model.extract_keywords(desc, keyphrase_ngram_range=(1, 3), stop_words=stop_words,use_maxsum=False, nr_candidates=20, top_n=int(0.2*len(desc.split())))
    
    keywords = []
    for w in kwr:
        keywords.append(w[0])
    
    return pd.DataFrame([[keywords]], columns=['AI_keywords'])
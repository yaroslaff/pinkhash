# generate dictionaries for eng1

import nltk
from nltk.corpus import wordnet as wn
from pathlib import Path

def clean_up(words_set: set):
    bad_characters = set("0123456789_-\'.")

    def has_bad_characters(word):
        return any(char in bad_characters for char in word)

    return {word for word in words_set if not has_bad_characters(word)}



def get_words(pos):
    # Get all noun synsets
    synsets = wn.all_synsets(pos=pos)

    # Extract words from synsets
    lemmas = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            lemmas.add(lemma.name().lower())  # Add the noun to the set to avoid duplicates

    clean_up(lemmas)

    # Convert to a sorted list if desired
    word_list = sorted(clean_up(lemmas))
    return word_list

def main():
    try:
        nltk.data.find('corpora/wordnet.zip')  # Check for the WordNet data
    except LookupError:
        print("WordNet not found. Downloading...")
        nltk.download('wordnet')

    nouns_list = get_words(wn.NOUN)
    # save list to .txt file
    Path('eng1-nouns.txt').write_text('\n'.join(nouns_list))

    adj_list = get_words(wn.ADJ)
    # save list to .txt file
    Path('eng1-adjective.txt').write_text('\n'.join(adj_list))

if __name__ == "__main__":
    main()
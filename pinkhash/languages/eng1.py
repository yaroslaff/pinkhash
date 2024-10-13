#
# wordnet/nltk dictionary
#

from ..lang import Language, language_mgr
from pathlib import Path
import os

script_dir = os.path.dirname(os.path.abspath(__file__))



class Eng1(Language):

    name="eng1"
    description=f"wordnet-based english language (adj+noun)"
    def_nwords=5


    def __init__(self):
        self.nouns = None
        self.adjectives = None

    def load_wordlists(self):
        self.nouns = (Path(script_dir) / Path('eng1-nouns.txt')).read_text().splitlines()
        self.adjectives = (Path(script_dir) / Path('eng1-adjective.txt')).read_text().splitlines()


    def convert(self, number: int):
        words = list()

        if self.nouns is None:
            # load wordlists on first conversion
            self.load_wordlists()

        remainder = number % len(self.adjectives)
        words.append(self.adjectives[remainder])
        number = number // len(self.adjectives)

        remainder = number % len(self.nouns)
        words.append(self.nouns[remainder])

        return words

language_mgr.add(Eng1.name, Eng1())




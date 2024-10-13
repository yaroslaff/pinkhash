#
# wordnet/nltk dictionary
#

from ..alphabet import Alphabet, alphabet_mgr
from pathlib import Path
import os

script_dir = os.path.dirname(os.path.abspath(__file__))



class Eng1(Alphabet):

    name="eng1"
    description=f"wordnet-based english alphabet (adj+noun)"
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

alphabet_mgr.add(Eng1.name, Eng1())




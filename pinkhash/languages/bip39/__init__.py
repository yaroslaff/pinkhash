#
# bip39 language
#

from ...lang import Language, language_mgr
from pathlib import Path
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))




class Bip39(Language):

    name="bip39"
    description=f"bip39-based language"
    def_nwords=5
    dictionary = None

    options = {
        'en': 'english.txt',
        'fr': 'french.txt',
        'es': 'spanish.txt',
        'pt': 'portuguese.txt',
        'it': 'italian.txt',
        'ko': 'korean.txt',
        'cz': 'czech.txt',
        'zh-hant':  'chinese_traditional.txt',
        'zh-hans': 'chinese_simplified.txt',
    }


    def __init__(self):
        self.description = f'Bip39, options are: {" ".join(self.options.keys())}'

    def load_wordlist(self, option: str):
        option = option or 'en'

        try:
            basename = self.options[option]
        except KeyError:
            print(f"Unknown language option {option}. Use one of: {' '.join(self.options.keys())}", file=sys.stderr)
            sys.exit(1)
        
        self.dictionary = (Path(script_dir) / Path(basename)).read_text().splitlines()
        
    def convert(self, number: int, option=None):
        words = list()
        if self.dictionary is None:
            self.load_wordlist(option=option)

        sz = len(self.dictionary)

        while True:
            remainder = number % sz
            words.append(self.dictionary[remainder])
            number = number // sz

            if number == 0:
                break

        return words

language_mgr.add(Bip39.name, Bip39())




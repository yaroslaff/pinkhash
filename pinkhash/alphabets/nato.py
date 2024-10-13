#
# Nato (ICAO) Alphabet
#

from ..alphabet import Alphabet, alphabet_mgr

nato_alphabet = [
    'Alpha',
    'Bravo',
    'Charlie',
    'Delta',
    'Echo',
    'Foxtrot',
    'Golf',
    'Hotel',
    'India',
    'Juliett',
    'Kilo',
    'Lima',
    'Mike',
    'November',
    'Oscar',
    'Papa',
    'Quebec',
    'Romeo',
    'Sierra',
    'Tango',
    'Uniform',
    'Victor',
    'Whiskey',
    'Xray',
    'Yankee',
    'Zulu'
]

class Nato(Alphabet):

    name="nato"
    description="NATO (ICAO) Phonetic Alphabet"
    def_nwords=5

    def __init__(self):
        pass

    def convert(self, number: int):
        words = list()

        sz = len(nato_alphabet)

        while True:
            remainder = number % sz
            words.append(nato_alphabet[remainder])
            number = number // sz

            if number == 0:
                break

        return words

alphabet_mgr.add(Nato.name, Nato())




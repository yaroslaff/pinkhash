
# abstract class for any alphabet such as Nato
class Alphabet():
    name = None
    description = "Abstract class for any alphabets"
    def_nwords=3

    def __init__(self):
        pass

class AlphabetManager():
    alphabets = dict()
    def __init__(self):
        pass

    def add(self, name: str, alphabet: Alphabet):
        self.alphabets[name] = alphabet

    def __repr__(self):
        return f'Alphabet Manager({self.alphabets.keys()})'
    
    def get_alphabet(self, name: str):
        return self.alphabets[name]


alphabet_mgr = AlphabetManager()

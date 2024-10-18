from .exception import PinkHashError

# abstract class for any language such as Nato
class Language():
    name = None
    description = "Abstract class for any languages"
    def_nwords=3

    def __init__(self):
        pass

class LanguageManager():
    languages = dict()
    def __init__(self):
        pass

    def add(self, name: str, alphabet: Language):
        self.languages[name] = alphabet

    def __repr__(self):
        return f'Language Manager({self.languages.keys()})'
    
    def get_language(self, name: str):
        try:
            return self.languages[name]
        except KeyError:
            raise PinkHashError(f'Language {name} not found')


language_mgr = LanguageManager()


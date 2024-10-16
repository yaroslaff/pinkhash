import hashlib
import io
from typing import Any, Optional

__version__ = '0.0.7'
default_language = 'bip39'

from .languages import nato, rfc1751, eng1, bip39
from .lang import language_mgr, Language
from .exception import PinkHashError

class PinkHash():
    
    language: Language = None
    nbytes: int
    nwords: int


    def __init__(self, language_name: str=None, option: str=None, nbytes: int = 8, nwords: Optional[int] = None, donothash=False):
        
        self.nbytes = nbytes
        # donothash - if data is already bytes of hash
        self.donothash = donothash
        self.option = option
        self.language = language_mgr.get_language(language_name or default_language)
        self.nwords = nwords or self.language.def_nwords

    def any2bytes(self, data: Any):
        # do not do anything if already bytes
        if isinstance(data, bytes):
            if self.donothash:
                return data
            hash_object = hashlib.sha1()
            hash_object.update(data)
            data = hash_object.digest()
            return data

        # if anything else
        if isinstance(data, str):
            # convert data to hash
            hash_object = hashlib.sha1()
            hash_object.update(data.encode('utf-8'))
            data = hash_object.digest()
            return data

        elif isinstance(data, io.IOBase):
            # read data from file
            data = data.read()
            
        else:
            print(f"Data type {type(data)} not supported yet")


    def convert(self, data: Any):
        data = self.any2bytes(data)
        last_bytes = data[-self.nbytes:]
        number = int.from_bytes(last_bytes, byteorder='little')
        pinkhash = self.language.convert(number = number, option=self.option)[:self.nwords]
        return ' '.join(pinkhash)

    def __repr__(self):
        return 'Pink Elephant'

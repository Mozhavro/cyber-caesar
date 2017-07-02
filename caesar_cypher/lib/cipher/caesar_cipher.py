from .alphabet import Alphabet
from . import caesar_default_config


class CaesarCipher:

    def __init__(self, allowed_alphabets=None):
        # TODO: protect from unexpected format: raise ValueError if not collection of alphabets
        self.allowed_alphabets = allowed_alphabets or caesar_default_config.allowed_alphabets

    def encrypt(self, text, rotate):
        if not isinstance(rotate, int):
            raise ValueError

        result = ''
        for char in text:
            shifted = None
            for alpha in self.allowed_alphabets:
                if shifted:
                    break
                shifted = alpha.shift(char, rotate)

            if shifted:
                result = result + shifted
            else:
                result = result + char

        return result


    def decrypt(self, text, key):
        if not isinstance(key, int):
            raise ValueError

        return self.encrypt(text, -key)
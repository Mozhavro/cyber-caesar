# from .cipher_abstract import AbstractCipher
from .alphabet import Alphabet

en_alphabet = Alphabet("a", "z")
en_alphabet_up = Alphabet("A", "Z")


def encrypt(text, rotate):
    pass


def decrypt(text, key):
    pass
import abc


class AbstractCipher(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def encrypt(text, key):
        pass

    @staticmethod
    @abc.abstractmethod
    def decrypt(text, key):
        pass
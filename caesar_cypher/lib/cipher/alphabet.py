class Alphabet:
    """Cyclic iterable class, that represents alphabet."""

    def __init__(self, start, end):
        """Alphabet represented by the bounds of characters ASCII codes,
        not the sequences of characters:
        start - alphabet first character
        end - alphabet last character
        other - any characters you want! list of additional characters"""
        self.start = ord(start)
        self.end = ord(end)
        self.codes = tuple(range(self.start, self.end+1))
        self.length = self.count_characters() + 1

    def get_all_characters(self):
        return "".join([chr(code) for code in self.codes])

    def shift(self, char, shift):
        """If character is in alphabet, returns character with index of
        original character index + shift, otherwise, returns original None."""
        if self.is_char_in_alphabet(char):
            original_char_code = ord(char)
            original_index = self.codes.index(original_char_code)
            shifted_index = (original_index + shift) % len(self.codes)
            return chr(self.codes[shifted_index])

        return None

    def is_char_in_alphabet(self, char):
        return self.start <= ord(char) <= self.end

    def get_character_position(self, char):
        alphabet = self.get_all_characters()
        try:
            position = alphabet.index(char)
            return alphabet.index(char)
        except ValueError:
            return None

    def count_characters(self):
        return self.end - self.start

    def __getitem__(self, item):
        return chr(self.codes[item%len(self.codes)])
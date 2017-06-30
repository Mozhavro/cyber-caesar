class Alphabet:
    """Cyclic iterable class, that represents alphabet."""

    def __init__(self, start, end):
        """Alphabet is represented by the bounds of characters ASCII codes,
        not the sequences of characters:
        start - alphabet first character
        end - alphabet last character
        other - any characters you want! list of additional characters"""
        self.start = ord(start)
        self.end = ord(end)
        self.codes = tuple(range(self.start, self.end+1))

    def get_all_characters(self):
        return "".join([chr(code) for code in self.codes])

    def shift(self, char, shift):
        """Returns character with index of original character index + shift"""
        original_char_code = ord(char)
        original_index = self.codes.index(original_char_code)
        shifted_index = (original_index + shift) % len(self.codes)
        return chr(self.codes[shifted_index])

    def __getitem__(self, item):
        return chr(self.codes[item%len(self.codes)])


if __name__=="__main__":
    alph = Alphabet("a", "z")
    print(alph.get_all_characters())
    print(alph.shift("a", 2))
    print(alph.shift("y", 4))
    print(alph.shift("b", -2))
    print(alph[0])
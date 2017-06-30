from alphabet import Alphabet

allowed_alphabets = (
    Alphabet("a", "z"),
    Alphabet("A", "Z")
)


def encrypt(text, rotate):
    if not isinstance(rotate, int):
        raise ValueError

    result = ''
    for char in text:
        shifted = None
        for alpha in allowed_alphabets:
            if shifted:
                break
            shifted = alpha.shift(char, rotate)

        if shifted:
            result = result + shifted
        else:
            result = result + char

    return result


def decrypt(text, key):
    if not isinstance(key, int):
        raise ValueError

    return encrypt(text, -key)


if __name__=="__main__":
    print(encrypt("sdf323fsfdASDF xxx dfs sdf", 3))
import unittest
from .caesar_cipher import CaesarCipher


class CesarCipherTest(unittest.TestCase):

    def test_encrypt(self):
        caesar = CaesarCipher()

        text = "abc"
        rotate = 1

        encrypted = caesar.encrypt(text, rotate)
        self.assertEqual(encrypted, "bcd")

    def test_encrypt_cyclic(self):
        """When the end of alphabet is reached, shift should be continued from it's start."""
        caesar = CaesarCipher()

        text = "abcz"
        rotate  = 1

        encrypted = caesar.encrypt(text, rotate)
        self.assertEqual(encrypted, "bcda")

    def test_encrypt_negative_rotate(self):
        caesar = CaesarCipher()

        """Shift back"""
        text = "bcz"
        rotate  = -1

        encrypted = caesar.encrypt(text, rotate)
        self.assertEqual(encrypted, "aby")

    def test_encrypt_negative_rotate_cyclic(self):
        """For the negative rotate, when the start of alphabet is reached, shift should be continued from it's end."""
        caesar = CaesarCipher()

        text = "abcz"
        rotate  = -1

        encrypted = caesar.encrypt(text, rotate)
        self.assertEqual(encrypted, "zaby")

    def test_encrypt_text_with_whitespaces(self):
        """Whitespaces should be left untouched"""
        caesar = CaesarCipher()

        text = "abc bcd zzz"
        rotate = 1

        encrypted = caesar.encrypt(text, rotate)
        self.assertEqual(encrypted, "bcd cde aaa")

    def test_decrypt(self):
        """In case of cesar cipher, decryption should mean rotation of characters to negative value of rotation key."""
        caesar = CaesarCipher()

        text = "bcd"
        rotate = 1

        encrypted = caesar.decrypt(text, rotate)
        self.assertEqual(encrypted, "abc")

    def test_sanity(self):
        """Encryption + decription should keep the original text"""
        caesar = CaesarCipher()

        original_text = "bcd"
        rotate = 1

        encrypted = caesar.encrypt(original_text, rotate)
        decrypted = caesar.decrypt(encrypted, rotate)

        self.assertEqual(original_text, decrypted)

    def test_encrypt_invalid_rotation_key(self):
        with self.assertRaises(ValueError):
            caesar = CaesarCipher()
            encrypted = caesar.encrypt('sdfds', 'sdfsdf')

    def test_encrypt_invalid_rotation_key2(self):
        caesar = CaesarCipher()
        with self.assertRaises(ValueError):
            encrypted = caesar.encrypt('sdfds', 1.23)


if __name__=="__main__":
    unittest.main()
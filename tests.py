from unittest import TestCase
import cesar_cipher


class CesarCipherTest(TestCase):

    def test_encrypt(self):
        text = "abc"
        rotate = 1

        encrypted = cesar_cipher.encrypt(text, rotate)
        self.assertEqual(encrypted, "bcd")

    def test_encrypt_cyclic(self):
        """When the end of alphabet is reached, shift should be continued from it's start."""
        text = "abcz"
        rotate  = 1

        encrypted = cesar_cipher.encrypt(text, rotate)
        self.assertEqual(encrypted, "bcda")

    def test_encrypt_negative_rotate(self):
        """Shift back"""
        text = "bcz"
        rotate  = -1

        encrypted = cesar_cipher.encrypt(text, rotate)
        self.assertEqual(encrypted, "aby")

    def test_encrypt_negative_rotate_cyclic(self):
        """For the negative rotate, when the start of alphabet is reached, shift should be continued from it's end."""
        text = "abcz"
        rotate  = -1

        encrypted = cesar_cipher.encrypt(text, rotate)
        self.assertEqual(encrypted, "zaby")

    def test_encrypt_text_with_whitespaces(self):
        """Whitespaces should be left untouched"""
        text = "abc bcd zzz"
        rotate = 1

        encrypted = cesar_cipher.encrypt(text, rotate)
        self.assertEqual(encrypted, "bcd cde aaa")

    def test_decrypt(self):
        """In case of cesar cipher, decryption should mean rotation of characters to negative value of rotation key."""
        text = "bcd"
        rotate = 1

        encrypted = cesar_cipher.decrypt(text, rotate)
        self.assertEqual(encrypted, "abc")

    def test_characters_validation(self):
        """Everything except alphabetical characters and whitespaces is invalid"""
        invalid_input = "fnds323254s"
        with self.assertRaises(ValueError):
            rotated = cesar_cipher(invalid_input, 1)

    def test_sanity(self):
        """Encryption + decription should keep the original text"""
        original_text = "bcd"
        rotate = 1

        encrypted = cesar_cipher.encrypt(original_text, rotate)
        decrypted = cesar_cipher.decrypt(encrypted, rotate)

        self.assertEqual(original_text, decrypted)
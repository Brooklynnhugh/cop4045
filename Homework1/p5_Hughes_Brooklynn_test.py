import unittest
from p5_Hughes_Brooklynn import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipherAndFrequency(unittest.TestCase):

    # -------------------------------------------------------------------------
    # Tests for caesar_cipher()
    # -------------------------------------------------------------------------
    def test_caesar_cipher_basic_encryption(self):
        """Test simple lowercase encryption with standard shift."""
        self.assertEqual(caesar_cipher("hello", 3), "khoor")

    def test_caesar_cipher_case_preservation(self):
        """Test that uppercase and lowercase letters preserve casing."""
        self.assertEqual(caesar_cipher("Hello World", 3), "Khoor Zruog")

    def test_caesar_cipher_non_alphabetic_preservation(self):
        """Test that spaces, numbers, and punctuation are untouched."""
        self.assertEqual(caesar_cipher("Hello, World! 123", 5), "Mjqqt, Btwqi! 123")

    def test_caesar_cipher_wrap_around(self):
        """Test alphabet wrap-around (z -> a)."""
        self.assertEqual(caesar_cipher("xyzXYZ", 3), "abcABC")

    def test_caesar_cipher_large_shift(self):
        """Test shifts greater than 26 using modulo arithmetic."""
        self.assertEqual(caesar_cipher("abc", 29), "def")  # 29 % 26 == 3

    def test_caesar_cipher_negative_shift(self):
        """Test negative shifts."""
        self.assertEqual(caesar_cipher("def", -3), "abc")

    # -------------------------------------------------------------------------
    # Tests for caesar_decipher()
    # -------------------------------------------------------------------------
    def test_caesar_decipher_basic(self):
        """Test standard decryption returning original text."""
        self.assertEqual(caesar_decipher("khoor", 3), "hello")

    def test_caesar_decipher_roundtrip(self):
        """Test encrypting and immediately decrypting restores exact message."""
        original = "Python 3.12 Unit Testing!"
        shift = 13
        encrypted = caesar_cipher(original, shift)
        decrypted = caesar_decipher(encrypted, shift)
        self.assertEqual(decrypted, original)

    # -------------------------------------------------------------------------
    # Tests for letter_frequency()
    # -------------------------------------------------------------------------
    def test_letter_frequency_counts(self):
        """Test accurate counting of lowercase letters."""
        text = "Hello World"
        freq = letter_frequency(text)
        
        self.assertEqual(freq['l'], 3)
        self.assertEqual(freq['o'], 2)
        self.assertEqual(freq['h'], 1)
        self.assertEqual(freq['a'], 0)  # Unused letters should be 0

    def test_letter_frequency_ignores_non_alpha(self):
        """Test that numbers, spaces, and symbols are excluded from counts."""
        text = "ABC 123!!! ###"
        freq = letter_frequency(text)
        
        self.assertEqual(freq['a'], 1)
        self.assertEqual(freq['b'], 1)
        self.assertEqual(freq['c'], 1)
        self.assertEqual(len(freq), 26)

    def test_letter_frequency_empty_string(self):
        """Test frequency analysis on non-alphabetic string."""
        freq = letter_frequency("12345 !@#$%")
        self.assertEqual(sum(freq.values()), 0)


if __name__ == "__main__":
    unittest.main()

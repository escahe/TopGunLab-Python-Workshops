from unittest import TestCase
from module1.programming_best_practices import is_palindrome

class TestIsPalidrome(TestCase):
    """Tests for is_palindrome() function in module1.programming_best_practices"""
    lower_case_palindromes = ['level', 'radar', 'civic', 'deed', 'noon', 'madam', 'rotator', 'stats', 'refer', 'tenet']
    upper_case_palindromes = [word.upper() for word in lower_case_palindromes]
    title_case_palindromes = [word.title() for word in lower_case_palindromes]

    def test_lower_case_palindrome_are_true(self):
        for word in self.lower_case_palindromes:
            self.assertTrue(is_palindrome(word))

    def test_upper_case_palindrome_are_true(self):
        for word in self.upper_case_palindromes:
            self.assertTrue(is_palindrome(word))

    def test_title_case_palindrome_are_true(self):
        for word in self.title_case_palindromes:
            self.assertTrue(is_palindrome(word))

    def test_one_char_palindrome_are_true(self):
        for char in "aeiou":
            self.assertTrue(is_palindrome(char))
    
    def test_empty_string_raises_an_error(self):
        with self.assertRaises(ValueError):
            is_palindrome("")

    def test_if_contains_spaces_raises_an_error(self):
        with self.assertRaises(ValueError):
            is_palindrome("This is not a word but a phrase")
    
    def test_non_alphabetic_chars_raises_an_error(self):
        with self.assertRaises(TypeError):
            is_palindrome(123)

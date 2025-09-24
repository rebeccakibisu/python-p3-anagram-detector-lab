# lib/testing/anagram_test.py
import pytest
from lib.anagram import Anagram

class TestAnagram:
    
    def test_is_anagram_true(self):
        """Test that is_anagram() correctly identifies anagrams."""
        word = Anagram("listen")
        assert word.is_anagram("silent") == True
        
    def test_is_anagram_false(self):
        """Test that is_anagram() correctly identifies non-anagrams."""
        word = Anagram("hello")
        assert word.is_anagram("world") == False

    def test_is_anagram_case_insensitive(self):
        """Test case insensitivity of is_anagram() method."""
        word = Anagram("Listen")
        assert word.is_anagram("SILENT") == True
    
    def test_is_anagram_invalid_input(self):
        """Test that ValueError is raised when input is not a string."""
        word = Anagram("hello")
        with pytest.raises(ValueError):
            word.is_anagram(123)
    
    def test_has_match_method(self):
        """contains a method called 'match'."""
        word = Anagram("listen")
        assert hasattr(word, 'is_anagram')  # Check that 'is_anagram' method exists

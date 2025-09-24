# lib/anagram.py
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Normalize to lowercase for comparison

    def is_anagram(self, other_word):
        """Check if the word is an anagram of the other_word."""
        if not isinstance(other_word, str):
            raise ValueError("Input should be a string")
        return sorted(self.word) == sorted(other_word.lower())

#spell check program
from spellchecker import SpellChecker

spell = SpellChecker()

def correct_word(word):
    # This part of code check if the word is misspelled
    if not spell.correction(word) == word:
        return spell.correction(word)
    else:
        # This part is for if the word is not misspelled, find the nearest words
        return spell.candidates(word)
    
enter_words=input("Enter Word Here :- ")
print(correct_word(enter_words))

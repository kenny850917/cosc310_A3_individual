from spellchecker import SpellChecker
import re
spell = SpellChecker()

# find those words that may be misspelled
sentence = 'something is happenning here, and it is nott amazzing'
wordList = re.sub("[^\w]", " ",  sentence).split()
misspelled = spell.unknown(wordList)

for words in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(words))

    # Get a list of `likely` options
    print(spell.candidates(words))

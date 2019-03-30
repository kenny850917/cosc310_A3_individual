from spellchecker import SpellChecker
import re


def spell_ck():
    spell = SpellChecker()

# find those words that may be misspelled
    sentence ='this is happeningg'
    wordList = re.sub("[^\w]", " ",  sentence).split()
    misspelled = spell.unknown(wordList)

    for words in misspelled:
        # Get the one `most likely` answer
        print("for "+words + " did you mean "+spell.correction(words))
        input = input('enter "y" if the correction is what you want')
        while input == 'y':
            re_enter = input('correct the spelling and try again')
            spell_ck(re_enter)


        # Get a list of `likely` options
        #print(spell.candidates(words))



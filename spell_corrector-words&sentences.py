# Neha Joby 8/15
# Spelling Corrector with textblob

from textblob import Word
import re

def check_word_spelling(word):
    """
    Spell corrector for individual words.
    :param word:
    :return:
    """
    word = Word(word)
    result = word.spellcheck()
    if word == result[0][0]:
        print()
    else:
        print(f'\nSpelling of "{word}" is not correct.')
        print(f'Correct spelling: "{result[0][0]}"')


word = input('Enter a word: ')
check_word_spelling(word)


def check_sentence_spelling(sentence):
    """
    Spell corrector for sentences.
    :param sentence:
    :return:
    """
    words = sentence.split()
    words = [word.lower() for word in words]
    words = [re.sub(r'[^A-Za-z0-9]+', '', word) for word in words]
    for word in words:
        result = check_word_spelling(word)
    print(result)


sentence = input('Enter a sentence: ')
check_sentence_spelling(sentence)

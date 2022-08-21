"""This file runs both classes and corrects the spelling mistakes on the user's text file."""

from errors import Errors
from correct_errors import CorrectErrors

# Run Errors class
sp_mistakes = Errors(dictionary_file_name = input('\nEnter the dictionary file: '), text_file = input('Enter the text file: '))
errors_result = sp_mistakes.run_functions()
knownWords = sp_mistakes.read_dictionary(sp_mistakes.dict_file)
print('\n')


# Run CorrectErrors class
correct_word = ['']
correct_sp_mistakes = CorrectErrors(errors_result)
correct_sp_mistakes.real_word(errors_result,knownWords)
for word in errors_result:
    mispelledLst = correct_sp_mistakes.fix_errors(word) 
    correct_word.extend(correct_sp_mistakes.validate(mispelledLst, knownWords))

print('The CORRECTED WORDS are:')
for i in correct_word:
    if (i != ''):
        print(i)
print('\n')

def get_corrections(corrections):
    """Gets corrections for each misspelled word from the spelling module.

    Returns:
        corrections: a list of the corrections for each word
    """
    for word in correct_sp_mistakes:
        corrections[word] = CorrectErrors.fix_errors(word)
    return corrections


# Edit the corrected mistakes in the user's text file
def edit_file(error_list, correct_word):
    """Replace all mispelled words with the corrected errors.

    Args:
        error_list: result of Errors class
        correct_word: result of CorrectErrors class
    """
    # Open text file to search for incorrectly spelled word.
    with open('sample_passage.txt', 'r') as f:
        text = f.read()
        text = text.replace(error_list, correct_word)
    # Open text file to write correctly spelled word into the file
    with open('sample_passage.txt', 'w') as f:
        f.write(text)

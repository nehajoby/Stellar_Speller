from errors import Errors
from correct_errors import CorrectErrors

# Run Errors class
sp_mistakes = Errors(dictionary_file_name = input('\nEnter the dictionary file: '), text_file = input('Enter the text file: '))
errors_result = sp_mistakes.run_functions()
knownWords= sp_mistakes.read_dictionary(sp_mistakes.dict_file)
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

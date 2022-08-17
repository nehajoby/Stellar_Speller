from errors import Errors

mistakes = Errors(dictionary_file_name = input('\nEnter the dictionary file: '), text_file = input('Enter the text file: '))
mistakes.run_functions()

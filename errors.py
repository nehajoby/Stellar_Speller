class Errors:

    """This class processes user input by reading the user inputted file and comparing it to the dictionary 
       to create a list of spelling errors which must be corrected. 
    """    
    
    def __init__(self, dictionary_file_name, text_file, errors=''):
        """This function initializes the Errors class.

        Args:
            dictionary_file_name: the name of the dictionary
            text_file: the name of user input text file
            errors: a list of spelling errors in the text file
        """
        self.dict_file = dictionary_file_name
        self.txt_file = text_file
        self.errors = errors
        

    def read_dictionary(self, dict_file):
        """This function reads the dictionary file.

        Args:
            dict_file: the name of the dictionary (dictionary.txt)

        Returns:
            dictionary_words: a list of words in the dictionary
        """
        dictionary_words = []
        input_file = open(dict_file, 'r')
        for line in input_file:
            word = line.strip()
            dictionary_words.append(word)
        input_file.close()
        return dictionary_words


    def read_txt_file(self, text_file_name):
        """This function reads the user's text file.

        Args:
            text_file_name: the name of the user input text file (sample_passage.txt)

        Returns:
            words: a list of words in the text file
        """
        words = []
        input_file = open(text_file_name, 'r')
        for line in input_file:
            words_on_line = line.strip().split()
            for word in words_on_line:
                words.append(word.strip('.,!/":;?').lower())
        input_file.close()
        return words


    def find_errors(self, dictionary_words, text_words):
        """This function finds the errors in the text file by comparing words to 
           dictionary_words to see which ones don't match which are the misspelled words.

        Args:
            dictionary_words: a list of words in the dictionary
            text_words: a list of words in the text file

        Returns:
            misspelled_words: a list of words in the text file that do not match 
            any words found in the dictionary
        """
        misspelled_words = []
        for word in text_words:
            if word not in dictionary_words:
                misspelled_words.append(word)
        return misspelled_words


    def print_errors(self, error_list):
        """This function prints the misspelled words.

        Args:
            error_list: misspelled words found in the find_errors function
        """
        print('\nThe MISSPELLED WORDS are: ')
        for word in error_list:
            print(word)


    def run_functions(self):
        """This file runs all the above functions.

        Returns:
            error_list: the result of the final function print_errors
        """
        dictionary_list = self.read_dictionary(self.dict_file)
        text_list = self.read_txt_file(self.txt_file)
        error_list = self.find_errors(dictionary_list, text_list)
        self.errors = self.print_errors(error_list)
        return error_list

    def __str__(self):
        """This function returns the errors as a string of errors which will be 
           corrected in the CorrectErrors class.

        Returns:
            self.errors: a list of spelling errors in the text file
        """
        return f'{self.errors}'

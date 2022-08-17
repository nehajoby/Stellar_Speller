class Errors:

    """This class reads the user inputted file and compares it with the dictionary to create a list of 
       spelling errors which must be corrected.
    """    
    def __init__(self, dictionary_file_name, text_file, errors=''):
        self.dict_file = dictionary_file_name
        self.txt_file = text_file
        self.errors = errors
        

    def read_dictionary(self, dict_file):
        dictionary_words = []
        input_file = open(dict_file, 'r')
        for line in input_file:
            word = line.strip()
            dictionary_words.append(word)
        input_file.close()
        return dictionary_words


    def read_txt_file(self, text_file_name):
        words = []
        input_file = open(text_file_name, 'r')
        for line in input_file:
            words_on_line = line.strip().split()
            for word in words_on_line:
                words.append(word.strip('.,!/":;?').lower())
        input_file.close()
        return words


    def find_errors(self, dictionary_words, text_words):
        misspelled_words = []
        for word in text_words:
            if word not in dictionary_words:
                misspelled_words.append(word)
        return misspelled_words


    def print_errors(self, error_list):
        print('The misspelled words are: ')
        for word in error_list:
            print(word)


    def run_functions(self):
        dictionary_list = self.read_dictionary(self.dict_file)
        text_list = self.read_txt_file(self.txt_file)
        error_list = self.find_errors(dictionary_list, text_list)
        self.errors = self.print_errors( error_list)

    def __str__(self):
        return f'\n{self.errors}'

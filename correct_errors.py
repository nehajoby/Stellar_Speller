class CorrectErrors:
    """This class corrects the incorrect misspelled words found by the Errors class. The functions in this class 
       spell checking each given word by finding different spelling mistakes and cross-checking the corrected 
       words with all the words in the dictionary. 
    """
    def __init__(self, word, lst=''):
        """This function initializes the CorrectErrors class.

        Args:
            word: incorrect mispelled word from Errors class
            lst: correct fixed word
        """
        self.word = word
        self.commonlst = lst


    def real_word(self, words, words1):
        """This function compares the correct words with words from the dictionary
           to check if the correct words are real words.

        Args:
            words: fixed words
            words1: _description_

        Returns:
            common: a list of corrected words that match words from the dictionary.
        """
        # Convert lists into sets to avoid duplicates
        unique_words = set(words)
        known_words = set(words1)

        # Find the intersection of the two sets
        common = set(unique_words).intersection(known_words)
        common.discard('a')
        common.discard('i')
        return list(common)


    def capitalization(self, word):
        """This function capitalizes the first letter of each sentence at the start 
           of a new line and after every period.

        Args:
            word: incorrect misspelled word

        Returns:
            cap: correct capitalized word
        """
        # Create an empty set to store the word
        cap = set()

        # Split word into a list of characters
        split = [char for char in self.word]

        # Find the order of the first character and change it to its capitalized order.
        num = ord(split[0])
        capital = num - 32
        letter_new = chr(capital)

        # Replace the first letter with the capitalized one and add the word to the set.
        split[0] = letter_new
        new = ''.join(split)
        cap.add(new)
        return cap


    def single_transpose(self, word):
        """This function finds single transpositions and replaces them with 
           a direct match from the dictionary.

        Args:
            word: incorrect misspelled word

        Returns:
            transpose: correct transposed word
        """
        # Establish an empty set to store words
        transpose = set('')

        # Split word into a list of characters
        split = [char for char in word]

        # Go through list of characters.
        for i in range(len(split) - 1):
            # For every index, replace with the next index and make the next index the original
            split[i], split[i + 1] = split[i + 1], split[i]

            # Convert list back into string and append to list
            transpose.add(''.join(split))

            # Undo the transpose for the next index
            split[i + 1], split[i] = split[i], split[i + 1]
        return transpose


    def double_the_trouble(self, word):
        """This function replaces misspelled double letters with a single letter, 
           or misspelled triple letters with a double letter.

        Args:
            word: incorrect misspelled word

        Returns:
            dups: correct double/triple letter removed word
        """
        count = {}
        for s in word:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1

        # Establish an empty set to store words
        dups = set()

        if count == 1:          # If there are no double letters -> completely skip this function
            return word

        elif count == 2:        # If there is a double letter -> Individually replace every letter 
                                # in the word with the same letter twice and add new word to set
            for char in self.word:
                new = self.word.replace(char, char * 2)
                dups.add(new)

        elif count == 3:        # If there is a triple letter -> Individually replace every letter 
                                # appearing 3 times consecutively with the letter twice and add new word to set
            for char in self.word:
                if char * 3 in self.word:
                    new = self.word.replace(char * 3, char * 2)
                    dups.add(new)

        return dups


    def insertion(self, word):
        """This function adds a missing letter in any word to correct a misspell.

        Args:
            word: incorrect misspelled word

        Returns:
            added: correct word with inserted letter
        """
        # Establish an empty set to store words
        added = set()

        # Create a string of the alphabet
        letters = 'abcdefghijklmnopqrstuvwxyz'

        # Individually add every letter in the alphabet next to every letter in the word and add new word to the set.
        for char in word:
            for le in letters:
                new = word.replace(char, char + le)
                added.add(new)
        return added



    def deletion(self, word):
        """This fucntion deletes a letter in any word to correct a misspell.

        Args:
            word: incorrect misspelled word

        Returns:
            delted: correct word with deleted letter
        """
        # Establish an empty set to store words
        deleted = set()

        # Individually delete every letter in the word and add new word to the set.
        for char in word:
            new = word.replace(char, '')
            if new not in deleted:
                deleted.add(new)
        return deleted


    def letter_swap(self, word):
        """This fucntion swaps out one letter for another to make the word correct.

        Args:
            word: incorrect misspleled word

        Returns:
            swaps: correct word with swapped letter
        """
        # Establish an empty set to store words
        swaps = set()

        # Create a string of the alphabet
        letters = 'abcdefghijklmnopqrstuvwxyz'

        # Replace every letter in the word with every letter of the alphabet and add to set
        for char in self.word:
            for le in letters:
                new = word.replace(char, le)
                swaps.add(new)
        return swaps


    def fix_errors(self, word):
        """This function runs all the above functions.

        Args:
            word: incorrect misspelled word

        Returns:
            all_errors: a set of all the corrected words
        """
        # Create set of all errors by finding the union of all the sets of corrections
        all_errors = self.single_transpose(word) | self.double_the_trouble(word) | self.insertion(word) | self.deletion(word) | self.letter_swap(word)
        return all_errors


    def validate(self, mispelledLst, kWords):
        """This fucntion returns a list of the corrected words that match up to the dictionary.

        Args:
            mispelledLst: a list of corrected words that ran through the fix_errors function
            kWords: a list of words from the dictionary

        Returns:
            lst: a list of the corrected words that match up to the dictionary.
        """
        # Passes word through the fix_errors function and then every word in the result through the function again.
        lst = ['']
        lst.extend(self.real_word(mispelledLst, kWords))
        return lst

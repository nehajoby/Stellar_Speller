# Stellar_Speller
The easy and convenient spell-checker to fix all your daily spelling mistakes!

PROGRAM SETUP & SYSTEM INSTRUCTIONS

1. Software Installation:
   Visual Studio Code (VS Code) - Download and install from here: https://code.visualstudio.com/download.
   Python - Download and install from here: https://www.python.org/downloads/.

3. Set Up Project Code Files from the GitHub Repository:
   Download the following files:
   `stellar_speller_main.py`
   `errors.py`
   `correct_errors.py`

4. Dictionary:
   If the text you want to spell check is in English, you can download the text file `dictionary.txt` which is a list of words all from the English language. If you are not using English, you can go online and download any text file which contains a dictionary of all the words in your language.

   Save these files into a dedicated folder on your desktop or a location of your choice.

6. User Input Text File:
   Create a text file containing the passage you want to check for spelling errors.
   For example, name it `sample_passage.txt`.

8. Launch VS Code:
   Open VS Code.
   Navigate to the folder where you saved the Stellar Speller project files.
   Also, open your user input text passage (e.g., `sample_passage.txt`) in VS Code.

10. Run the Code:
    In VS Code, open the `stellar_speller_main.py` file.
    Execute the file to start the spell-checking process.

12. All set!
    Now you have no more spelling mistakes :)



Link to full project report:  https://docs.google.com/document/d/1WJtULZIcVA_41pi6nJj-8NZNWb6fXQVKoE6hfmmejpM/edit?usp=sharing.


stellar_speller_main.py - Runs both classes and corrects the spelling mistakes on the user's text file.

errors.py - The Errors class processes user input by reading the user inputted file and comparing it to the dictionary to create a list of spelling errors which must be corrected.

correct_errors.py - The CorrectErrors class corrects the incorrect misspelled words found by the Errors class. The functions in this class spell checking each given word by finding different spelling mistakes and cross-checking the corrected words with all the words in the dictionary.

dictionary.txt - The dictionary that Stellar Speller uses to compare misspelled words with the correct spelling. This text file is a list of 181,080 words from the English language which includes, but is not limited to, all plurals, suffixes, prefixes of every word. I downloaded this text file from Dr. Phillip M. Feldman’s website English Spelling Dictionaries.

sample_passage.txt - A sample user input text file that I used to make sure the program works.

corrected_passage.txt - The edited version of sample_passage.txt with correct spellings produced by Stellar Speller.

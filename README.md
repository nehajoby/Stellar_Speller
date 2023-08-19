# Stellar_Speller
The easy and convenient spell-checker to fix all your daily spelling mistakes!

STELLAR SPELLER SETUP INSTRUCTIONS

1. Software Installation:
Visual Studio Code (VS Code) - Download and install from here: https://code.visualstudio.com/download.
Python - Download and install from here: https://www.python.org/downloads/.

3. Set Up Project Files from the GitHub Repository:
Download the following files:
`stellar_speller_main.py`
`errors.py`
`correct_errors.py`
`dictionary.txt` (For English language users)
Save these files into a dedicated folder on your desktop or a location of your choice.

4. User Input Text File:
Create a text file containing the passage you want to check for spelling errors. 
For example, name it `sample_passage.txt`.

5. Launch VS Code:
Open VS Code.
Navigate to the folder where you saved the Stellar Speller project files.
Also, open your user input text passage (e.g., `sample_passage.txt`) in VS Code.

6. Run the Code:
In VS Code, open the `stellar_speller_main.py` file.
Execute the file to start the spell-checking process.

7. All set!
You can now proceed with the spell-checking using the Stellar Speller. Enjoy :)



Link to full project report:  https://docs.google.com/document/d/11HFOw1-YGaJOae5MZ1fyPvMFWUceCOkywo2IHA3Qwqg/edit?usp=sharing.


stellar_speller_main.py - Runs both classes and corrects the spelling mistakes on the user's text file.

errors.py - The Errors class processes user input by reading the user inputted file and comparing it to the dictionary to create a list of spelling errors which must be corrected.

correct_errors.py - The CorrectErrors class corrects the incorrect misspelled words found by the Errors class. The functions in this class spell checking each given word by finding different spelling mistakes and cross-checking the corrected words with all the words in the dictionary.

dictionary.txt - The dictionary that Stellar Speller uses to compare misspelled words with the correct spelling. This text file is a list of 181,080 words from the English language which includes, but is not limited to, all plurals, suffixes, prefixes of every word. I downloaded this text file from Dr. Phillip M. Feldman’s website English Spelling Dictionaries.

sample_passage.txt - A sample user input text file that I used to make sure the program works.

corrected_passage.txt - The edited version of sample_passage.txt with correct spellings produced by Stellar Speller.

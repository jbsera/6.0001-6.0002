# Problem Set 2, hangman.py
# Name: Joy Bhattacharya
# Collaborators: Hannah Donner
# Time spent:18

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.    
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    x=0
    for i in secret_word: #Iterate over every character in secret_word
        if i in letters_guessed: #if the character is in the letters_guessed
            x+=1 #increment a temporary variable by 1
    if x==len(secret_word): #After the for loop, check if the temporary variable equals the total number of characters in secret_word, meaning that all the characters in secret_word were found in letters_guessed  
        return True
    else: #if not, return False
        return False 
        
    
def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    x="" #initializing the string to have 0 characters originally 
    for i in secret_word: #iterate over every character in secret_word
        if i in letters_guessed: #if the character in secret_word is in letters_guessed then add the character i to the x string 
            x+=i
        else: #else since the character is not in letters_guessed, add an asterisk to the string x
            x+="*"
    return x #returning the final string with correct guesses and characters yet to be guessed
        


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
        
    alphabet=string.ascii_lowercase 
    letters_remaining=list(alphabet) #Turns the alphabet into a list assigned to the variable letters_remaining 
    
    for i in alphabet: #Iterate over every letter in the alphabet 
      if i in letters_guessed: #If the letter in the alphabet is also in the letters that have been guessed, remove that letter from your list of letters remaining 
         letters_remaining.remove(i) #This removes the letter in the order that it was found in the list, preserves alphabetical order
    return (''.join(letters_remaining)) #This converts the letters_remaining back into a string

def help_function(secret_word,get_available_letters, letters_guessed):
    '''
    secret_word : string of the secret word you're trying to guess
    letters_remaining : the letters remaining that you haven't guessed

    Returns a revealed character that you haven't guessed when user asks for a hint
    '''
    choose_from=''#initializing choose_from as an empty string 
    for i in secret_word:#iterate over every letter in the secret word 
        if i in get_available_letters(letters_guessed):#find the letters that secret words has in common with the letters remaining
            choose_from+=i #add these letters to the string of letters to choose from
    new = random.randint(0, len(choose_from)-1) #randomly choose one of the letters from choose_from
    revealed_letter = choose_from[new] #create a variable called revealed_letter that equals your randomly chosen character from choose_from
    letters_guessed.append(revealed_letter) #add the revealed letter to the list of total letters_guessed
    return revealed_letter


def hangman(secret_word, with_help):
    '''
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '^'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol ^, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    letters_guessed=[] #initialize letters_guessed as an empty list 
    alphabet=list(string.ascii_letters) #make the alphabet equal to the list of all lowercase and uppercase letters 
    vowels="aeiou" #set a string of vowels for later conditional tests
    guesses_remaining=10 #initial amount of guesses is 10
    print("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("If you need a hint, enter (^). You will lose 3 guesses for every hint")
    while True: #keeps going through this while loop until you win or lose 
        print("---------------------")
        print('You have', guesses_remaining, 'guesses left.')
        print("Available letters:",(get_available_letters(letters_guessed)))
        guess=(input("Please guess a letter:"))
        guess=guess.lower() #converts guess to a lowercase letter 
        if guess in letters_guessed: #if you have already guessed the letter, you get an error message and aren't penalized
            print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
            guesses_remaining=guesses_remaining
        elif guess=="^" and with_help==True: #If you enter ^ to get a hint
            if guesses_remaining<=2:#Gives you an error message if you don't have enough guesses.  
                print("Oops! Not enough guesses left:", get_word_progress(secret_word, letters_guessed))
                guesses_remaining=guesses_remaining
            else: #If you have enough guesses, it shows you the letter revealed and the newly revealed parts of the secret word 
                print("Letter revealed:",(help_function(secret_word,get_available_letters, letters_guessed)))
                print(get_word_progress(secret_word, letters_guessed))
                guesses_remaining-=3
        elif guess not in alphabet:#error message if your guess wasn't in the alphabet 
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, letters_guessed) )
            guesses_remaining=guesses_remaining
        elif guess in secret_word:#adds your guess to letters guessed and shows the revealed characters in secret word 
            letters_guessed.append(guess)
            print("Good guess:", get_word_progress(secret_word, letters_guessed))
            guesses_remaining=guesses_remaining
        elif guess not in secret_word: #for valid guesses that aren't in the secret word
            if guess in vowels: #if your incorrect guess is a vowel, subtract two guesses
                letters_guessed.append(guess) #add letter to letters_guessed
                print("Oops! That letter is not in my word:",get_word_progress(secret_word, letters_guessed))
                guesses_remaining-=2
            else: #if your incorrect guess is a consonant, only subtract one guess
                letters_guessed.append(guess) #add letter to letters_guessed
                print("Oops! That letter is not in my word:",get_word_progress(secret_word, letters_guessed)) 
                guesses_remaining-=1
        if guesses_remaining<=0 and has_player_won(secret_word, letters_guessed)==False: #if you ran out of guesses when the secret word hasn't been completely guessed, you lose. The while loop breaks and the secret word is revealed to you. 
            print("--------------")
            print("Sorry, you ran out of guesses. The word was", secret_word)
            break
        if has_player_won(secret_word, letters_guessed)==True: #if you've won, the while loop breaks and you get your final score. 
            print("-----------------")
            print("Congratulations, you won!")
            final_score=(2*len(set(secret_word))*guesses_remaining)+(3*len(secret_word)) #calculates your final score. len(set()) gives you the number of unique letters in the word
            print("Your total score for this game is:",final_score)
            break
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

hangman("apple", True)

# =============================================================================
# if __name__ == "__main__":
#     # To test your game, uncomment the following two lines.
#         secret_word = choose_word(wordlist)
#         with_help = True
#         hangman(secret_word, with_help)
# =============================================================================

    # After you complete with_help functionality, change with_help to True
    # and try entering "^" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    
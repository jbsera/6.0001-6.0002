# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:09:35 2020

@author: joyse
"""
import string 
import random

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
    for i in str(secret_word): #iterate over every character in secret_word
        if i in str(letters_guessed): #if the character in secret_word is in letters_guessed then add the character i to the x string 
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
        
    alphabet="abcdefghijklmnopqrstuvwxyz" 
    letters_remaining=list(alphabet) #Turns the alphabet into a list assigned to the variable letters_remaining 
    
    for i in alphabet: #Iterate over every letter in the alphabet 
      if i in letters_guessed: #If the letter in the alphabet is also in the letters that have been guessed, remove that letter from your list of letters remaining 
         letters_remaining.remove(i) #This removes the letter in the order that it was found in the list, preserves alphabetical order
    return (''.join(letters_remaining)) #This converts the letters_remaining back into a string


def helper_function(secret_word, letters_remaining):
    '''
    Parameters
    ----------
    secret_word : string
        
    letters_remaining : The string of 
        

    Returns
    -------
    None.

    '''
    #we suggest writing a helper function that chooses a letter to reveal. It should take two arguments: the secret word and the string of available letters (from get_available_letters). This helper function should create a string choose_from, containing the unique letters that are in both the secret word and the available letters. You can then use the following statements to pick a random character revealed_letter from that string:

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
    
    letters_guessed=[]
    alphabet=list(string.ascii_letters)
    vowels="aeiou"
    guesses_remaining=10
    print("Hello, are you ready to play Hangman?")
    print("I'm thinking of a word that's", len(secret_word), "letter(s) long.")
    print("If you need a hint, enter (^). You will lose 3 guesses for every hint")

#First guess
    while True:
        print("---------------------")
        print('You have', guesses_remaining, 'guesses remaining.')
        print("You have these choices remaining:",(get_available_letters(letters_guessed)))
        print("The secret word is:", get_word_progress(secret_word, letters_guessed))
        guess=(input("Guess a letter:"))
        guess=guess.lower()
        if guess in letters_guessed:
            print("You have already guessed that letter, try again")
            guesses_remaining=guesses_remaining
        elif len(str(guess))!=1:
            print("Guess only one character at a time please, try again")
            guesses_remaining=guesses_remaining
        #elif guess=="^" and with_help=True:
            #if guesses_remaining<=2:
                #print("You do not have 3 guesses remaining. Try another guess")
                #guesses_remaining=guesses_remaining
            #else: 
                #guesses_remaining-=3
        elif guess not in alphabet:
            print("That is not a letter, try again.")
            guesses_remaining=guesses_remaining
        elif guess in str(secret_word):
            letters_guessed.append(guess)
            print("That was a good guess")
            guesses_remaining=guesses_remaining
        elif guess not in str(secret_word):
            if guess in str(vowels):
                letters_guessed.append(guess)
                print("That letter is not in the word.")
                guesses_remaining-=2
            else:
                letters_guessed.append(guess)
                print("That letter is not in the word.") 
                guesses_remaining-=1
        if guesses_remaining<=0:
            print("You have lost :(")
            print("The secret word was:", secret_word)
            break
        elif has_player_won(secret_word, letters_guessed)==True:
            print("You have won! You guessed the secret word:", secret_word)
            final_score=(2*len(set(secret_word))*guesses_remaining)+(3*len(secret_word))
            print("Final score:",final_score)
            break
wordlist = load_words()
if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)


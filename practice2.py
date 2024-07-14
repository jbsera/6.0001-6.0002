# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 15:12:10 2020

@author: joyse
"""
import string 
message_text='L dp 42 bhduv rog'
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist
WORDLIST_FILENAME = 'words.txt'
valid_words=load_words(WORDLIST_FILENAME)
def get_valid_words():
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        X=valid_words[:]
        return X

def make_shift_dict(input_shift, decrypt=False):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter and number.

        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift, as well as
        every number to one shifted down by the same amount. If 'a' is
        shifted down by 2, the result is 'c' and '0' shifted down by 2 is '2'.

        The dictionary should contain 62 keys of all the uppercase letters,
        all the lowercase letters, and all numbers mapped to their shifted values.

        input_shift: the amount by which to shift every letter of the
        alphabet and every number (0 <= shift < 26)

        decrypt: if the shift dict will be used for decrypting. affects digit shift function

        Returns: a dictionary mapping letter/number (string) to
                 another letter/number (string).
        '''
        if decrypt==True:
            input_shift=-input_shift
        shift_dict={}
        lower_case_letters=[]
        upper_case_letters=[]
        numbers=[]
        for letter in string.ascii_lowercase:
            lower_case_letters.append(letter)
            lower_case_copy=lower_case_letters[:]
        for index in range(len(lower_case_letters)):       
            lower_case_copy[index]=lower_case_letters[(index+input_shift)%26]
        for letter in string.ascii_uppercase:
            upper_case_letters.append(letter)
            upper_case_copy=upper_case_letters[:]
        for index in range(len(upper_case_letters)):      
            upper_case_copy[index]=upper_case_letters[(index+input_shift)%26]
        for number in string.digits:
            numbers.append(number)
            numbers_copy=numbers[:]
        for index in range(len(numbers)):
            numbers_copy[index]=numbers[(index+input_shift)%10]
        for index in range(len(lower_case_letters)):
            shift_dict[lower_case_letters[index]]=lower_case_copy[index]
        for index in range(len(upper_case_letters)):
            shift_dict[upper_case_letters[index]]=upper_case_copy[index]
        for index in range(len(numbers)):
            shift_dict[numbers[index]]=numbers_copy[index]
        return shift_dict 

def apply_shift(shift_dict):
        '''
        Applies the Caesar Cipher to self.message_text with the shift
        specified in shift_dict. Creates a new string that is self.message_text,
        shifted down by some number of characters, determined by the shift
        value that shift_dict was built with.

        shift_dict: a dictionary with 62 keys, mapping
            lowercase and uppercase letters and numbers to their new letters
            (as built by make_shift_dict)

        Returns: the message text (string) with every letter/number shifted using
            the input shift_dict

        '''
        X=[]
        message_text='Agnnqy 3'
        for element in message_text:
            if element not in shift_dict:
                X.append(element)
            else:
                X.append(shift_dict[element])
        message_text=''.join(X)
        return message_text
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list
def decrypt_message():
        '''
        Decrypts self.message_text by trying every possible shift value and
        finding the "best" one.

        We will define "best" as the shift that creates the max number of
        valid English words when we use apply_shift(shift) on the message text.
        If a is the original shift value used to encrypt the message, then
        we would expect (26 - a) to be the  value found for decrypting it.

        Note: if shifts are equally good, such that they all create the
        max number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return.

        Returns: a tuple of the best shift value used to originally encrypt
        the message (a) and the decrypted message text using that shift value
        '''
        
        L={}
        Y=[]
        for input_shift in range(27): #for every possible input shift
            x=0
            Total_valid_words=0
            encryption_dict=make_shift_dict(input_shift, True)
            encrypted_message=apply_shift(encryption_dict)
            word_string=encrypted_message.split(' ')
            for word in word_string: #for every word in the decrypted message text that's found from applying the specific shift dictionary to the original message text
                if is_word(get_valid_words(),word): #use a counter for every word that is a valid word 
                    x+=1
                if x>0:
                    print(word)
            Total_valid_words=x
            print(input_shift,Total_valid_words)
            L[input_shift]=Total_valid_words
        max_valid_words=max(L.values())
        for key in L:
            if L[key]==max_valid_words:
                Y.append(key)
        for i in Y:
            decrypted_message=apply_shift(make_shift_dict(i,True))
            break
        Y.append(decrypted_message)
        Tuple_answer=tuple(Y)
        return Tuple_answer

            
print(decrypt_message())
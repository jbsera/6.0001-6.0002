# Problem Set 4B
# Name: Joy Bhattacharya
# Collaborators: Sang (Jess) Eu Han 
# Time Spent: 6 hours 
# Late Days Used: x

import string

### HELPER CODE ###
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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

def get_digit_shift(input_shift, decrypt):
    '''
    calculate the digit shift based on if decrypting or not
    decrypt: boolean, if decrypting or not
    Returns: digit_shift, the digit shift based on if decrypting or not
    '''
    if decrypt:
        digit_shift = 10 - (26-input_shift)%10
    else:
        digit_shift = input_shift
    return digit_shift

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #initializes data attributes
        self.message_text=input_text 
        self.valid_words=load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        X=self.valid_words[:] #creates a copy of the list for valid words
        return X

    def make_shift_dict(self, input_shift, decrypt=False):
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
        if decrypt==True: #if you are trying to decrypt, you'll want your input shift to go backwards
            input_shift=-input_shift 
        shift_dict={} #initializing dictionaries and empty lists 
        lower_case_letters=[]
        upper_case_letters=[]
        numbers=[]
        for letter in string.ascii_lowercase: #for the lowercase letters
            lower_case_letters.append(letter) #add each letter to a list of lowercase letters
            lower_case_copy=lower_case_letters[:] #make a copy of that list 
        for index in range(len(lower_case_letters)):       
            lower_case_copy[index]=lower_case_letters[(index+input_shift)%26] #mutate the copied list by changing it's letters to the new index after the input shift has been applied. The %26 takes care of looping around the alphabet. 
        for letter in string.ascii_uppercase: #do the same thing for uppercase letters as we did for lowercase letters
            upper_case_letters.append(letter)
            upper_case_copy=upper_case_letters[:]
        for index in range(len(upper_case_letters)):      
            upper_case_copy[index]=upper_case_letters[(index+input_shift)%26]
        for number in string.digits: #make a list of numbers and make a copy of that list 
            numbers.append(number)
            numbers_copy=numbers[:]
        for index in range(len(numbers)): #mutate the copied list by changing the index in the copy to the new index in the original list after the input shift has been applied. The %10 takes care of looping around the digits like from 9 to 0 for example.
            numbers_copy[index]=numbers[(index+input_shift)%10]
        for index in range(len(lower_case_letters)): #add all the lowercase letters into the dictionary as keys with their associated values being their shift values from the mutated list
            shift_dict[lower_case_letters[index]]=lower_case_copy[index]
        for index in range(len(upper_case_letters)): #add all the uppercase letters into the dictionary as keys with their associated values being their shift values from the mutated list
            shift_dict[upper_case_letters[index]]=upper_case_copy[index]
        for index in range(len(numbers)):#add all the numbers into the dictionary as keys with their associated values being their shift values from the mutated list
            shift_dict[numbers[index]]=numbers_copy[index]
        return shift_dict #return the shifted dictionary

    def apply_shift(self, shift_dict):
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
        self.get_message_text() #gets the string of the message_text
        X=[]
        for element in self.message_text: #for every character in the string
            if element not in shift_dict: #if the character is not in the dictionary, like spaces or punctuation, append the character to a list 
                X.append(element)
            else: #if the character is in the shifted dictionary, append the shift value associated with that element in the dictionary into a list. This will tell you what the shifted character of the original element should be. 
                X.append(shift_dict[element])
        message_text=''.join(X) #turn the list into a string 
        return message_text #return the encrypted string 
class PlaintextMessage(Message):
    def __init__(self, input_text, input_shift):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        input_shift: the shift associated with this message

        A PlaintextMessage object inherits from Message. It has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using the shift)
            self.encrypted_message_text (string, encrypted using self.encryption_dict)

        '''
        Message.__init__(self, input_text) #calling on data attributes of parent function
        self.shift=input_shift
        self.encryption_dict={} #initialized as an empty dictionary
        self.encrypted_message_text='' #initialized as an empty string 
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy of self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        self.encryption_dict=self.make_shift_dict(self.shift) #returns the dictionary given from making a specific shift
        return self.encryption_dict.copy() #returns a copy of the dictionary 

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        self.encrypted_message_text=self.apply_shift(self.get_encryption_dict()) #gets the encrypted text by calling the apply shift function for your specific shifted dictionary
        return self.encrypted_message_text #returns the encrypted text 

    def modify_shift(self, input_shift):
        '''
        Changes self.shift of the PlaintextMessage, and updates any other
        attributes that are determined by the shift.

        input_shift: an integer, the new shift that should be associated with this message.
        [0 <= shift < 26]

        Returns: nothing
        '''
        self.shift=input_shift #sets your shift equal to your input shift 


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the message's text

        an EncryptedMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, input_text) #initializes from the parent class 

    def decrypt_message(self):
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
        
        L={} #initialize an empty dictionary and list 
        Y=[]
        for input_shift in range(27): #for every possible input shift
            x=0
            Total_valid_words=0
            decryption_dict=self.make_shift_dict(input_shift, True) #find the dictionary by calling on make_shift_dict where decryption is True
            decrypted_message=self.apply_shift(decryption_dict) #find the string of the decrypted message by calling the apply shift function using your decryption dictionary
            word_string=decrypted_message.split(' ') #split the decrypted message along spaces so that each word is it's own string, not each character
            for word in word_string: #for every word in the decrypted message text 
                if is_word(self.get_valid_words(),word): #use a counter for every word that is a valid word 
                    x+=1
            Total_valid_words=x #essentially finds the total number of words that are valid words
            L[input_shift]=Total_valid_words #creates a dictionary mapping the decryption input shift to the total number of valid words
        max_valid_words=max(L.values()) #finds the max value of valid words in the decryption message
        for key in L: #if the value in the dictionary is equal to the max value, append the input shift key to a list. Finds the input shifts that give the highest number of valid words. 
            if L[key]==max_valid_words: 
                Y.append(key)
        for i in Y: #find the decrypted message from the input shift that gave the most number of valid words
            decrypted_message=self.apply_shift(self.make_shift_dict(i,True))
            break
        Y.append(decrypted_message) #adds the final decrypted message to a list 
        Tuple_answer=tuple(Y) #turns the list into a tuple
        return Tuple_answer #returns the tuple 

def test_plaintext_message():
    '''
    Write two test cases for the PlaintextMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (PlaintextMessage) #####

#    # This test is checking encoding a lowercase string with punctuation in it.
#    plaintext = PlaintextMessage('hello!', 2)
#    print('Expected Output: jgnnq!')
#    print('Actual Output:', plaintext.get_encrypted_message_text())

    #Ex. 1
    #This test is checking a string of uppercase and lowercase letters with punctuation
    plaintext = PlaintextMessage('I ScREam FOr IcE CReaM!!!!!!!!$$$$',4)
    print('Expected Output:', 'M WgVIeq JSv MgI GVieQ!!!!!!!!$$$$')
    print('Actual Output:', plaintext.get_encrypted_message_text())
    print('------------------')
    #Ex.2
    #This is testing a string of only numbers and punctuation
    plaintext = PlaintextMessage('789 2020202 &&&*** ###))))))',7)
    print('Expected Output:', '456 9797979 &&&*** ###))))))')
    print('Actual Output:', plaintext.get_encrypted_message_text())
    print('---------------')
def test_encrypted_message():
    '''
    Write two test cases for the EncryptedMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

    # Ex.1 test case
    #This test case is checking decoding a string with both upper and lowercase in it
    encrypted=EncryptedMessage('Khoor Zruog')
    print('Expected Output:', (3, "Hello World"))
    print("Actual Output:", encrypted.decrypt_message())
    print('----------------')
    #Ex. 2 test case
    #This test case is checking decoding a string with only puncutation, numbers, and letters in it
    encrypted=EncryptedMessage('Agnnqy, 940')
    print('Expected Output:', (2, "Yellow, 728"))
    print("Actual Output:", encrypted.decrypt_message())
    print('-------------------')
def decode_story():
    '''
    Write your code here to decode the story contained in the file story.txt.
    Hint: use the helper function get_story_string and your EncryptedMessage class.

    Returns: a tuple containing (best_shift, decoded_story)

    '''
    secret_story=EncryptedMessage(get_story_string()) #says that secret_story belongs to the EncryptedMessage class
    return secret_story.decrypt_message() #calls on the decryption function to decrypt secret story 




if __name__ == '__main__':

    # Uncomment these lines to try running your test cases
    test_plaintext_message()
    test_encrypted_message()

    # Uncomment these lines to try running decode_story_string()
    best_shift, story = decode_story()
    print("Best shift:", best_shift)
    print("Decoded story: ", story)
    

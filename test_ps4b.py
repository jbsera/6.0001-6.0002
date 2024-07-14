# for running unit tests on 6.00/6.0001/6.0002 student code

import os
import string
import sys
import unittest
from contextlib import redirect_stdout

import ps4b as student


# A class that inherits from unittest.TestCase, where each function
# is a test you want to run on the student's code. For a full description
# plus a list of all the possible assert methods you can use, see the
# documentation: https://docs.python.org/3/library/unittest.html#unittest.TestCase
class TestPS4B(unittest.TestCase):

    def setUp(self):
        self.text1 = 'testing message'
        self.text2 = 'A message with punctuation in it... Fun!'
        self.text3 = 'zzzzz....'
        self.text4 = 'he,llo'
        self.text5 = 'My PIN is 12345 so secure!'
        self.text6 = 'H3LL0 W0RLD'

        self.encrypt1 = 'whvwlqj phvvdjh'
        self.encrypt2 = 'B nfttbhf xjui qvoduvbujpo jo ju... Gvo!'
        self.encrypt3 = 'bbbbb....'
        self.encrypt4 = 'he,llo'
        self.encrypt5 = 'Xj ATY td 23456 dz dpnfcp!'
        self.encrypt6 = 'K6OO3 Z3UOG'

        # do this so "loading words" doesn't print out every time
        with redirect_stdout(open(os.devnull, "w")):
            self.msg1 = student.Message(self.text1)
            self.msg2 = student.Message(self.text2)
            self.msg3 = student.Message(self.text3)
            self.msg4 = student.Message(self.text4)
            self.msg5 = student.Message(self.text5)
            self.msg6 = student.Message(self.text6)

            self.ptmsg1 = student.PlaintextMessage(self.text1, 3) #1
            self.ptmsg2 = student.PlaintextMessage(self.text2, 1) #2
            self.ptmsg3 = student.PlaintextMessage(self.text3, 2)
            self.ptmsg4 = student.PlaintextMessage(self.text4, 0)
            self.ptmsg5 = student.PlaintextMessage(self.text5, 11)
            self.ptmsg6 = student.PlaintextMessage(self.text6, 3)

            self.ctmsg1 = student.EncryptedMessage(self.encrypt1)
            self.ctmsg2 = student.EncryptedMessage(self.encrypt2)
            self.ctmsg3 = student.EncryptedMessage(self.encrypt3)
            self.ctmsg4 = student.EncryptedMessage(self.encrypt4)
            self.ctmsg5 = student.EncryptedMessage(self.encrypt5)
            self.ctmsg6 = student.EncryptedMessage(self.encrypt6)

    def test_message_get_message_text(self):
        response = self.msg1.get_message_text()
        self.assertEqual(response, self.text1,
            "get_message_text returned %s, but %s was expected" % (response, self.text1))

    def test_message_get_valid_words(self):
        with redirect_stdout(open(os.devnull, "w")):
            expected_word_list = student.load_words(student.WORDLIST_FILENAME)
        student_list = self.msg1.get_valid_words()
        self.assertEqual(expected_word_list, student_list,
            "get_valid_words does not return expected word list")

        student_list.remove('a')
        new_student_list = self.msg1.get_valid_words()
        self.assertEqual(len(expected_word_list), len(new_student_list),
            "get_valid_words should return a *copy* of self.valid_words, but your code returns the original list.")

    def test_message_make_shift_dict(self):
        sd1 = self.msg1.make_shift_dict(0)
        self.assertTrue(len(sd1) >= 52, "The shift dictionary should contain 26 lower case and 26 upper case, and maybe 10 numbers")

        error_msg = "With a shift of %s, %s should map to %s, but instead maps to %s"

        for ll in string.ascii_lowercase:
            actual = sd1[ll]
            self.assertEqual(ll, actual, error_msg % (0, ll, ll, actual))

        for ul in string.ascii_uppercase:
            actual = sd1[ul]
            self.assertEqual(ul, actual, error_msg % (0, ul, ul, actual))

        sd2 = self.msg1.make_shift_dict(4)
        expected = {'V': 'Z', 'l': 'p', 'U': 'Y', 'm': 'q', 'C': 'G', 'h': 'l', 'd': 'h', 'n': 'r', 'b': 'f', 'H': 'L', 'a': 'e', 'W': 'A', 'P': 'T', 'B': 'F', 'F': 'J', 'i': 'm', 'G': 'K', 'S': 'W', 'N': 'R', 'k': 'o', 'e': 'i', 'o': 's', 'L': 'P', 'O': 'S', 'D': 'H', 'I': 'M', 'J': 'N', 'Y': 'C', 'K': 'O', 'R': 'V', 'E': 'I', 'p': 't', 'r': 'v', 'g': 'k', 'X': 'B', 'y': 'c', 'c': 'g', 'v': 'z', 'u': 'y', 't': 'x', 'f': 'j', 'w': 'a', 'Q': 'U', 'q': 'u', 'z': 'd', 'j': 'n', 's': 'w', 'x': 'b', 'M': 'Q', 'Z': 'D', 'T': 'X', 'A': 'E'}

        for ll in string.ascii_lowercase:
            actual = sd2[ll]
            self.assertEqual(expected[ll], actual, error_msg % (4, ll, expected[ll], actual))

        for ul in string.ascii_uppercase:
            actual = sd2[ul]
            self.assertEqual(expected[ul], actual, error_msg % (4, ul, expected[ul], actual))

    def test_message_make_shift_dict_with_numbers(self):
        sd1 = self.msg1.make_shift_dict(0)
        self.assertEqual(62, len(sd1), "The shift dictionary should contain 62 keys, one for each uppercase and lowercase letter and each string digit.")

        error_msg = "With a shift of %s, %s should map to %s, but instead maps to %s"

        for ll in string.ascii_lowercase:
            actual = sd1[ll]
            self.assertEqual(ll, actual, error_msg % (0, ll, ll, actual))

        for ul in string.ascii_uppercase:
            actual = sd1[ul]
            self.assertEqual(ul, actual, error_msg % (0, ul, ul, actual))

        for num in string.digits:
            actual = sd1[num]
            self.assertEqual(num, actual, error_msg % (0, num, num, actual))

        sd2 = self.msg1.make_shift_dict(4)
        expected = {'V': 'Z', 'l': 'p', 'U': 'Y', 'm': 'q', 'C': 'G', 'h': 'l', 'd': 'h', 'n': 'r', 'b': 'f', 'H': 'L', 'a': 'e', 'W': 'A', 'P': 'T', 'B': 'F', 'F': 'J', 'i': 'm', 'G': 'K', 'S': 'W', 'N': 'R', 'k': 'o', 'e': 'i', 'o': 's', 'L': 'P', 'O': 'S', 'D': 'H', 'I': 'M', 'J': 'N', 'Y': 'C', 'K': 'O', 'R': 'V', 'E': 'I', 'p': 't', 'r': 'v', 'g': 'k', 'X': 'B', 'y': 'c', 'c': 'g', 'v': 'z', 'u': 'y', 't': 'x', 'f': 'j', 'w': 'a', 'Q': 'U', 'q': 'u', 'z': 'd', 'j': 'n', 's': 'w', 'x': 'b', 'M': 'Q', 'Z': 'D', 'T': 'X', 'A': 'E', '0': '4', '1': '5', '2': '6', '3': '7', '4': '8', '5': '9', '6': '0', '7': '1', '8': '2', '9': '3'}

        for ll in string.ascii_lowercase:
            actual = sd2[ll]
            self.assertEqual(expected[ll], actual, error_msg % (4, ll, expected[ll], actual))

        for ul in string.ascii_uppercase:
            actual = sd2[ul]
            self.assertEqual(expected[ul], actual, error_msg % (4, ul, expected[ul], actual))

        for num in string.digits:
            actual = sd2[num]
            self.assertEqual(expected[num], actual, error_msg % (4, num, expected[num], actual))

    def test_message_apply_shift(self):
        error_msg = "Encoding message '%s' with shift of %s failed. Expected %s, got %s"

        sd1 = self.msg1.make_shift_dict(3)
        sd2 = self.msg2.make_shift_dict(1)
        sd3 = self.msg3.make_shift_dict(2)
        sd4 = self.msg4.make_shift_dict(0)

        msg1_encoded = self.msg1.apply_shift(sd1)
        msg2_encoded = self.msg2.apply_shift(sd2)
        msg3_encoded = self.msg3.apply_shift(sd3)
        msg4_encoded = self.msg4.apply_shift(sd4)

        self.assertEqual(msg1_encoded, self.encrypt1, error_msg % (self.text1, 3, self.encrypt1, msg1_encoded))
        self.assertEqual(msg2_encoded, self.encrypt2, error_msg % (self.text2, 1, self.encrypt2, msg2_encoded))
        self.assertEqual(msg3_encoded, self.encrypt3, error_msg % (self.text3, 2, self.encrypt3, msg3_encoded))
        self.assertEqual(msg4_encoded, self.encrypt4, error_msg % (self.text4, 0, self.encrypt4, msg4_encoded))

    def test_message_apply_shift_with_numbers(self):
        error_msg = "Encoding message '%s' with shift of %s failed. Expected %s, got %s"

        sd5 = self.msg5.make_shift_dict(11)
        sd6 = self.msg6.make_shift_dict(3)

        msg5_encoded = self.msg5.apply_shift(sd5)
        msg6_encoded = self.msg6.apply_shift(sd6)

        self.assertEqual(msg5_encoded, self.encrypt5, error_msg % (self.text5, 0, self.encrypt5, msg5_encoded))
        self.assertEqual(msg6_encoded, self.encrypt6, error_msg % (self.text6, 0, self.encrypt6, msg6_encoded))

    def test_plaintext_message_attributes(self):
        s1 = self.ptmsg1.get_shift()
        s2 = self.ptmsg2.get_shift()
        s3 = self.ptmsg3.get_shift()
        s4 = self.ptmsg4.get_shift()
        s5 = self.ptmsg5.get_shift()
        s6 = self.ptmsg6.get_shift()

        error_msg_1 = "Expected get_shift to return %s, but returned %s"

        self.assertEqual(s1, 3, error_msg_1 % (3, s1))
        self.assertEqual(s2, 1, error_msg_1 % (1, s2))
        self.assertEqual(s3, 2, error_msg_1 % (2, s3))
        self.assertEqual(s4, 0, error_msg_1 % (0, s4))
        self.assertEqual(s5, 11, error_msg_1 % (11, s5))
        self.assertEqual(s6, 3, error_msg_1 % (3, s6))

        expected_ed1 = {'V': 'Y', 'l': 'o', 'U': 'X', 'm': 'p', 'C': 'F', 'h': 'k', 'd': 'g', 'n': 'q', 'b': 'e', 'H': 'K', 'a': 'd', 'W': 'Z', 'P': 'S', 'B': 'E', 'F': 'I', 'i': 'l', 'G': 'J', 'S': 'V', 'N': 'Q', 'k': 'n', 'e': 'h', 'o': 'r', 'L': 'O', 'O': 'R', 'D': 'G', 'I': 'L', 'J': 'M', 'Y': 'B', 'K': 'N', 'R': 'U', 'E': 'H', 'p': 's', 'r': 'u', 'g': 'j', 'X': 'A', 'y': 'b', 'c': 'f', 'v': 'y', 'u': 'x', 't': 'w', 'f': 'i', 'w': 'z', 'Q': 'T', 'q': 't', 'z': 'c', 'j': 'm', 's': 'v', 'x': 'a', 'M': 'P', 'Z': 'C', 'T': 'W', 'A': 'D', '0': '3', '1': '4', '2': '5', '3': '6', '4': '7', '5': '8', '6': '9', '7': '0', '8': '1', '9': '2'}
        expected_ed2 = {'V': 'X', 'l': 'n', 'W': 'Y', 'Z': 'B', 'w': 'y', 'E': 'G', 'C': 'E', 'D': 'F', 'p': 'r', 'U': 'W', 'o': 'q', 'M': 'O', 'a': 'c', 'O': 'Q', 'd': 'f', 'A': 'C', 'Y': 'A', 'z': 'b', 'N': 'P', 'K': 'M', 'r': 't', 'B': 'D', 'm': 'o', 'b': 'd', 'R': 'T', 's': 'u', 'q': 's', 'j': 'l', 'u': 'w', 'P': 'R', 'c': 'e', 'Q': 'S', 'f': 'h', 'h': 'j', 'H': 'J', 'F': 'H', 'e': 'g', 'i': 'k', 'G': 'I', 'y': 'a', 'X': 'Z', 'g': 'i', 'x': 'z', 't': 'v', 'J': 'L', 'I': 'K', 'S': 'U', 'T': 'V', 'L': 'N', 'k': 'm', 'v': 'x', 'n': 'p', '0': '2', '1': '3', '2': '4', '3': '5', '4': '6', '5': '7', '6': '8', '7': '9', '8': '0', '9': '1'}
        ed1 = self.ptmsg1.get_encryption_dict()
        ed2 = self.ptmsg3.get_encryption_dict()
        # Add asserts for other two dictionaries
        self.assertEqual(expected_ed1, ed1, "The encryption dictionary returned by get_encryption_dict() does not match the message's shift.")
        self.assertEqual(expected_ed2, ed2, "The encryption dictionary returned by get_encryption_dict() does not match the message's shift.")
        ed1['test_key'] = 'test_value'

        new_eds = self.ptmsg1.get_encryption_dict()
        self.assertEqual(62, len(new_eds), "get_encryption_dict() should return a copy of the encryption_dict attribute, but your code returns the original.")

        expected_encrypted = 'whvwlqj phvvdjh'
        actual_encrypted = self.ptmsg1.get_encrypted_message_text()
        self.assertEqual(expected_encrypted, actual_encrypted, "get_encrypted_message_text() did not return the correct result; expected %s, got %s" % (expected_encrypted, actual_encrypted))

    def test_plaintext_message_modify_shift(self):
        self.ptmsg1.modify_shift(0)

        actual_shift = self.ptmsg1.get_shift()
        self.assertEqual(0, actual_shift, "After calling modify_shift(), the value of self.shift was not updated correctly: expected %s, got %s" % (0, actual_shift))

        actual_ed = self.ptmsg1.get_encryption_dict()
        expected_ed = {'V': 'V', 'l': 'l', 'U': 'U', 'm': 'm', 'C': 'C', 'h': 'h', 'd': 'd', 'n': 'n', 'b': 'b', 'H': 'H', 'a': 'a', 'W': 'W', 'P': 'P', 'B': 'B', 'F': 'F', 'i': 'i', 'G': 'G', 'S': 'S', 'N': 'N', 'k': 'k', 'e': 'e', 'o': 'o', 'L': 'L', 'O': 'O', 'D': 'D', 'I': 'I', 'J': 'J', 'Y': 'Y', 'K': 'K', 'R': 'R', 'E': 'E', 'p': 'p', 'r': 'r', 'g': 'g', 'X': 'X', 'y': 'y', 'c': 'c', 'v': 'v', 'u': 'u', 't': 't', 'f': 'f', 'w': 'w', 'Q': 'Q', 'q': 'q', 'z': 'z', 'j': 'j', 's': 's', 'x': 'x', 'M': 'M', 'Z': 'Z', 'T': 'T', 'A': 'A', '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
        self.assertEqual(expected_ed, actual_ed, 'After calling modify_shift(), the encryption_dict attribute was not updated correctly.')

        actual_message = self.ptmsg1.get_encrypted_message_text()
        expected_message = self.text1
        self.assertEqual(expected_message, actual_message, 'After calling modify_shift(), the encrypted_message_text attribute was not updated correctly. Expected %s, got %s' % (expected_message, actual_message))

    # This test may take a couple seconds to run
    def test_encrypted_decrypt_message(self):

        error_msg_1 = "Expected a best shift of %s for decoding '%s', but got %s"
        error_msg_2 = "Failed to properly decrypt the encrypted message '%s'; expected %s, got %s"

        dc1 = self.ctmsg1.decrypt_message()
        self.assertIsInstance(dc1, tuple, "decrypt_message() should return a tuple, but you return a " + str(type(dc1)))
        self.assertEqual(dc1[0], 3,  error_msg_1 % (3, self.encrypt1, dc1[0]))
        self.assertEqual(dc1[1], self.text1, error_msg_2 % (self.encrypt1, self.text1, dc1))

        dc2 = self.ctmsg2.decrypt_message()
        self.assertEqual(dc2[0], 1, error_msg_1 % (1, self.encrypt2, dc2[0]))
        self.assertEqual(dc2[1], self.text2, error_msg_2 % (self.encrypt2, self.text2, dc2))

        dc5 = self.ctmsg5.decrypt_message()
        self.assertEqual(dc5[0], 11, error_msg_1 % (11, self.encrypt5, dc5[0]))
        self.assertEqual(dc5[1], self.text5, error_msg_2 % (self.encrypt5, self.text5, dc5))

    def test_valid_word_checking(self):

        error_msg = "Expected best shift to be %s and best decryption to be %s for encrypted message '%s', but got shift of %s and message '%s'. Are you sure you're checking for valid words correctly?"
        encrypted = 'qoghzsg, qoh,'
        expected_decrypt = 'castles, cat,'
        with redirect_stdout(open(os.devnull, "w")):
            c = student.EncryptedMessage(encrypted)
        shift, actual = c.decrypt_message()
        self.assertEqual(actual, expected_decrypt, error_msg % (14, expected_decrypt, encrypted, shift, actual))


# Dictionary mapping function names from the above TestCase class to
# messages you'd like the student to see if the test fails.
failure_messages = {
    'test_message_get_message_text' : 'Message.get_message_text() does not return the expected messages.',
    'test_message_get_valid_words' : 'Message.get_valid_words() does not behave correctly. Either you do not return the correct list, or you return the original list rather than a copy of it.',
    'test_message_make_shift_dict' : 'Message.make_shift_dict() does not correctly build a shift dictionary.',
    'test_message_apply_shift' : 'Message.apply_shift() does not correctly encrypt messages.',
    'test_plaintext_message_attributes' : 'The attributes of your PlaintextMessage class and/or their getter functions are incorrectly implemented ',
    'test_plaintext_message_modify_shift' : 'PlaintextMessage.modify_shifts() does not properly update object attributes',
    'test_encrypted_decrypt_message' : 'EncryptedMessage.decrypt_message() does not correctly decrypt messages.',
    'test_valid_word_checking' : 'Your code does not correctly check if possible decrypted words are valid.'
}


# Dictionary mapping function names from the above TestCase class to
# the point value each test is worth.
point_values = {
    'test_message_get_message_text' : 0.25,
    'test_message_get_valid_words' : 0.25,
    'test_message_make_shift_dict' : 0.3,
    'test_message_make_shift_dict_with_numbers' : 0.2,
    'test_message_apply_shift' : 0.3,
    'test_message_apply_shift_with_numbers' : 0.2,
    'test_plaintext_message_attributes' : 0.25,
    'test_plaintext_message_modify_shift' : 0.5,
    'test_encrypted_decrypt_message' : 0.5,
    'test_valid_word_checking' : 0.25,
}

# Subclass to track a point score and appropriate
# grade comment for a suit of unit tests
class Results_600(unittest.TextTestResult):

    # We override the init method so that the Result object
    # can store the score and appropriate test output.
    def __init__(self, *args, **kwargs):
        super(Results_600, self).__init__(*args, **kwargs)
        self.output = []
        self.points = 3

    def addFailure(self, test, err):
        test_name = test._testMethodName
        msg = str(err[1])
        self.handleDeduction(test_name, msg)
        super(Results_600, self).addFailure(test, err)

    def addError(self, test, err):
        test_name = test._testMethodName
        self.handleDeduction(test_name, None)
        super(Results_600, self).addError(test, err)

    def handleDeduction(self, test_name, message):
        point_value = point_values[test_name]
        if message is None:
            message = 'Your code produced an error on test %s.' % test_name
        self.output.append('[-%s]: %s' % (point_value, message))
        self.points -= point_value

    def getOutput(self):
        if len(self.output) == 0:
            return "All correct!"
        return '\n'.join(self.output)

    def getPoints(self):
        return self.points

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPS4B))
    result = unittest.TextTestRunner(verbosity=2, resultclass=Results_600).run(suite)

    output = result.getOutput()
    points = result.getPoints()

    if points < .1:
        points = 0

    print("\nProblem Set 4B Unit Test Results:")
    print(output)
    print("Points: %s/3\n" % points)

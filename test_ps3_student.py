import os
import document_distance as ds
import unittest
import string

#Constants
a1 = ['from', 'time', 'to', 'time', 'this',
      'submerged', 'or', 'latent', 'theater',
      'in', 'becomes', 'almost', 'overt', 'it',
      'is', 'close', 'to', 'the', 'surface', 'in',
      'hamlets', 'pretense', 'of', 'madness', 'the',
      'antic', 'disposition', 'he', 'puts', 'on',
      'to', 'protect', 'himself', 'and', 'prevent',
      'his', 'antagonists', 'from', 'plucking', 'out',
      'the', 'heart', 'of', 'his', 'mystery', 'it',
      'is', 'even', 'closer', 'to', 'the', 'surface',
      'when', 'hamlet', 'enters', 'his', 'mothers',
      'room', 'and', 'holds', 'up', 'side', 'by',
      'side', 'the', 'pictures', 'of', 'the', 'two',
      'kings', 'old', 'hamlet', 'and', 'claudius',
      'and', 'proceeds', 'to', 'describe', 'for', 'her',
      'the', 'true', 'nature', 'of', 'the', 'choice',
      'she', 'has', 'made', 'presenting', 'truth', 'by',
      'means', 'of', 'a', 'show', 'similarly', 'when',
      'he', 'leaps', 'into', 'the', 'open', 'grave', 'at',
      'ophelias', 'funeral', 'ranting', 'in', 'high', 'heroic',
      'terms', 'he', 'is', 'acting', 'out', 'for', 'laertes',
      'and', 'perhaps', 'for', 'himself', 'as', 'well', 'the',
      'folly', 'of', 'excessive', 'melodramatic', 'expressions',
      'of', 'grief']
a1_freq = {'from': 2, 'time': 2, 'to': 5, 'this': 1, 'submerged': 1,
        'or': 1, 'latent': 1, 'theater': 1, 'in': 3, 'becomes': 1,
        'almost': 1, 'overt': 1, 'it': 2, 'is': 3, 'close': 1,
        'the': 10, 'surface': 2, 'hamlets': 1, 'pretense': 1, 'of': 7,
        'madness': 1, 'antic': 1, 'disposition': 1, 'he': 3, 'puts': 1,
        'on': 1, 'protect': 1, 'himself': 2, 'and': 5, 'prevent': 1,
        'his': 3, 'antagonists': 1, 'plucking': 1, 'out': 2, 'heart': 1,
        'mystery': 1, 'even': 1, 'closer': 1, 'when': 2, 'hamlet': 2,
        'enters': 1, 'mothers': 1, 'room': 1, 'holds': 1, 'up': 1,
        'side': 2, 'by': 2, 'pictures': 1, 'two': 1, 'kings': 1, 'old': 1,
        'claudius': 1, 'proceeds': 1, 'describe': 1, 'for': 3, 'her': 1,
        'true': 1, 'nature': 1, 'choice': 1, 'she': 1, 'has': 1, 'made': 1,
        'presenting': 1, 'truth': 1, 'means': 1, 'a': 1, 'show': 1,
        'similarly': 1, 'leaps': 1, 'into': 1, 'open': 1, 'grave': 1,
        'at': 1, 'ophelias': 1, 'funeral': 1, 'ranting': 1, 'high': 1,
        'heroic': 1, 'terms': 1, 'acting': 1, 'laertes': 1, 'perhaps': 1,
        'as': 1, 'well': 1, 'folly': 1, 'excessive': 1, 'melodramatic': 1,
        'expressions': 1, 'grief': 1}

b1 = ['almost', 'all', 'of', 'shakespeares', 'hamlet', 'can', 'be',
        'understood', 'as', 'a', 'play', 'about', 'acting', 'and', 'the',
        'theater', 'for', 'example', 'there', 'is', 'hamlets', 'pretense',
        'of', 'madness', 'the', 'antic', 'disposition', 'that', 'he',
        'puts', 'on', 'to', 'protect', 'himself', 'and', 'prevent', 'his',
        'antagonists', 'from', 'plucking', 'out', 'the', 'heart', 'of',
        'his', 'mystery', 'when', 'hamlet', 'enters', 'his', 'mothers',
        'room', 'he', 'holds', 'up', 'side', 'by', 'side', 'the', 'pictures',
        'of', 'the', 'two', 'kings', 'old', 'hamlet', 'and', 'claudius',
        'and', 'proceeds', 'to', 'describe', 'for', 'her', 'the', 'true',
        'nature', 'of', 'the', 'choice', 'she', 'has', 'made', 'presenting',
        'truth', 'by', 'means', 'of', 'a', 'show', 'similarly', 'when', 'he',
        'leaps', 'into', 'the', 'open', 'grave', 'at', 'ophelias', 'funeral',
        'ranting', 'in', 'high', 'heroic', 'terms', 'he', 'is', 'acting',
        'out', 'for', 'laertes', 'and', 'perhaps', 'for', 'himself', 'as',
        'well', 'the', 'folly', 'of', 'excessive', 'melodramatic',
        'expressions', 'of', 'grief']
b1_freq = {'almost': 1, 'all': 1, 'of': 8, 'shakespeares': 1, 'hamlet': 3,
        'can': 1, 'be': 1, 'understood': 1, 'as': 2, 'a': 2, 'play': 1,
        'about': 1, 'acting': 2, 'and': 5, 'the': 9, 'theater': 1, 'for': 4,
        'example': 1, 'there': 1, 'is': 2, 'hamlets': 1, 'pretense': 1,
        'madness': 1, 'antic': 1, 'disposition': 1, 'that': 1, 'he': 4,
        'puts': 1, 'on': 1, 'to': 2, 'protect': 1, 'himself': 2, 'prevent': 1,
        'his': 3, 'antagonists': 1, 'from': 1, 'plucking': 1, 'out': 2,
        'heart': 1, 'mystery': 1, 'when': 2, 'enters': 1, 'mothers': 1,
        'room': 1, 'holds': 1, 'up': 1, 'side': 2, 'by': 2, 'pictures': 1,
        'two': 1, 'kings': 1, 'old': 1, 'claudius': 1, 'proceeds': 1,
        'describe': 1, 'her': 1, 'true': 1, 'nature': 1, 'choice': 1,
        'she': 1, 'has': 1, 'made': 1, 'presenting': 1, 'truth': 1,
        'means': 1, 'show': 1, 'similarly': 1, 'leaps': 1, 'into': 1,
        'open': 1, 'grave': 1, 'at': 1, 'ophelias': 1, 'funeral': 1,
        'ranting': 1, 'in': 1, 'high': 1, 'heroic': 1, 'terms': 1,
        'laertes': 1, 'perhaps': 1, 'well': 1, 'folly': 1, 'excessive': 1,
        'melodramatic': 1, 'expressions': 1, 'grief': 1}

# Helper function to retrieve filepaths; ripped from https://stackoverflow.com/questions/9816816/get-absolute-paths-of-all-files-in-a-directory
def absolute_file_paths(directory):
    filepaths=[]
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            filepaths.append(os.path.abspath(os.path.join(dirpath, f)))

    return filepaths

# Test shell
class TestLoadFile(unittest.TestCase):
    def test_prep_hello_world(self):
        expected = ["hello", "world", "hello"]
        result = ds.load_file("tests/student_tests/hello_world.txt")
        self.assertEqual(result, expected)

    def test_prep_1a(self):
        expected = a1
        result = ds.load_file("tests/student_tests/test1a.txt")
        self.assertEqual(result, expected)

    def test_prep_all_whitespace(self):
        expected = ["hello", "it", "is", "me", "mario"]
        result = ds.load_file("tests/student_tests/test1c.txt")
        self.assertEqual(result, expected)

class TestComputeFrequencies(unittest.TestCase):
    def test_frequency_hello_world(self):
         data = ["hello", "world", "hello"]
         result = ds.compute_frequencies(data)
         expected = {"hello":2, "world":1}
         self.assertDictEqual(result, expected)

    def test_frequency_1a(self):
         data = a1
         result = ds.compute_frequencies(data)
         expected = a1_freq
         self.assertDictEqual(result, expected)

    def test_frequency_1b(self):
         data = b1
         result = ds.compute_frequencies(data)
         expected = b1_freq
         self.assertDictEqual(result, expected)

class TestNgrams(unittest.TestCase):
    def test_ngrams_empty(self):
         result = ds.find_ngrams([""], 2)
         expected = []
         self.assertListEqual(result, expected)

    def test_ngrams_zero(self):
         result = ds.find_ngrams(["hello", "world", "hello",
                                  "friends", "hello"], 0)
         expected = []
         self.assertListEqual(result, expected)

    def test_ngrams_hello(self):
         result = ds.find_ngrams(["hello", "world", "hello",
                                  "friends", "hello"], 2)
         expected = ['hello world', 'world hello', 'hello friends', 'friends hello']
         self.assertListEqual(result, expected)

    def test_ngrams_aeiou(self):
         result = ds.find_ngrams(['a', 'e', 'i', 'o', 'u', 'a', 'b', 'c'], 5)
         expected = ['a e i o u', 'e i o u a', 'i o u a b', 'o u a b c']
         self.assertListEqual(result, expected)


class TestSimilarity(unittest.TestCase):
     def test_similarity1(self):
         f1 = {"hello":2, "world":1}
         f2 = {"hello":2, "world":1}
         result = ds.get_similarity_score(f1, f2)
         expected = 100
         self.assertEqual(result, expected)

     def test_similarity2(self):
         f1 = {}
         f2 = {"hello":1}
         result = ds.get_similarity_score(f1, f2)
         expected = 0
         self.assertEqual(result, expected)

     def test_similarity3(self):
         f1 = {"hello":2, "world":1}
         f2 = {"hello":2, "friends":1}
         result = ds.get_similarity_score(f1, f2)
         expected = 67
         self.assertEqual(result, expected)

     def test_similarity4(self):
         f1 = {"hello":2, "world":1}
         f2 = {"hello":1, "friends":1}
         result = ds.get_similarity_score(f1, f2)
         expected = 40
         self.assertEqual(result, expected)

     def test_difference1(self):
         f1 = {"hello":2, "world":1}
         f2 = {"hello":1, "friends":1}
         result = ds.get_similarity_score(f1, f2, True)
         expected = 60
         self.assertEqual(result,expected)

     def test_difference2(self):
         f1 = {}
         f2 = {"hello":1}
         result = ds.get_similarity_score(f1, f2, True)
         expected = 100
         self.assertEqual(result,expected)


class TestMostFrequent(unittest.TestCase):
    def test_words1(self):
        f1 = {"hello":1, "world":2}
        f2 = {"hello":1, "world":5}
        result = ds.compute_most_frequent(f1, f2)
        expected = ['world']
        self.assertListEqual(result, expected)

    def test_words2(self):
        f1 = {"hello":5, "world":1}
        f2 = {"hello":1, "world":5}
        result = ds.compute_most_frequent(f1, f2)
        expected = ['hello', 'world']
        self.assertListEqual(result, expected)

class TestClosestArtist(unittest.TestCase):
    def test_closest_nomatch(self):
        artists = ["artist_1", "artist_2"]
        prefix = "tests/student_tests"
        artist_to_songfiles_map = {}
        query = ds.load_file(prefix + "/mystery_lyrics/mystery_3.txt")
        result = ds.find_closest_artist(artist_to_songfiles_map, query)
        expected = []
        self.assertListEqual(result, expected)

    def test_closest_none(self):
        artists = ["artist_1", "artist_2"]
        prefix = "tests/student_tests"
        artist_to_songfiles_map = {}
        query = ds.load_file(prefix + "/mystery_lyrics/mystery_1.txt")
        result = ds.find_closest_artist(artist_to_songfiles_map, query)
        expected = []
        self.assertListEqual(result, expected)

    def test_closest_3(self):
        artists = ["artist_1", "artist_2"]
        prefix = "tests/student_tests"
        artist_to_songfiles_map = {
            artist: absolute_file_paths(os.path.join(prefix, artist)) for artist in artists
        }
        query = ds.load_file(prefix + "/mystery_lyrics/mystery_1.txt")
        result = ds.find_closest_artist(artist_to_songfiles_map, query, ngrams=1)
        expected = ["artist_1"]
        self.assertListEqual(result, expected)

    def test_closest_tie_with_ngrams(self):
        artists = ["artist_1", "artist_2"]
        prefix = "tests/student_tests"
        artist_to_songfiles_map = {
            artist: absolute_file_paths(os.path.join(prefix, artist)) for artist in artists
        }
        query = ds.load_file(prefix + "/mystery_lyrics/mystery_4.txt")
        result = ds.find_closest_artist(artist_to_songfiles_map, query, ngrams=2)
        expected = ["artist_1", "artist_2"]
        self.assertListEqual(result, expected)

    def test_closest_ngrams(self):
        artists = ["artist_1", "artist_2"]
        prefix = "tests/student_tests"
        artist_to_songfiles_map = {
            artist: absolute_file_paths(os.path.join(prefix, artist)) for artist in artists
        }
        query = ds.load_file(prefix + "/mystery_lyrics/mystery_5.txt")
        result_with_ngrams = ds.find_closest_artist(artist_to_songfiles_map, query, ngrams=3)
        expected_with_ngrams = []
        result_without_ngrams = ds.find_closest_artist(artist_to_songfiles_map, query, ngrams=1)
        expected_without_ngrams = ["artist_2"]
        self.assertListEqual(result_without_ngrams, expected_without_ngrams)
        self.assertListEqual(result_with_ngrams, expected_with_ngrams)

#Dictionary mapping function names from the above TestCase class to
# the point value each test is worth. Make sure these add up to 5!
point_values = {
        'test_prep_hello_world': .05,
        'test_prep_all_whitespace': .05,
        'test_prep_1a': .10,
        'test_frequency_hello_world' : .40,
        'test_frequency_1a' : .30,
        'test_frequency_1b': .30,
        'test_ngrams_empty': .10,
        'test_ngrams_zero': .10,
        'test_ngrams_hello': .10,
        'test_ngrams_aeiou': .10,
        'test_similarity1': .10,
        'test_similarity2': .10,
        'test_similarity3': .20,
        'test_similarity4': .20,
        'test_difference1': .10,
        'test_difference2': .10,
        'test_words1': .30,
        'test_words2': .30,
        'test_closest_3': .50,
        'test_closest_none': .25,
        'test_closest_nomatch': .25,
        'test_closest_tie_with_ngrams': .50,
        'test_closest_ngrams': .50
    }

failure_messages = {
    'test_prep_hello_world': 'Your function generated an incorrect list to represent hello_world.txt',
    'test_prep_all_whitespace': 'Your function generated an incorrect list that strips all whitespace.',
    'test_prep_1a': 'Your function generated an incorrect list to represent test1a.txt',
    'test_frequency_hello_world' : 'Your function generated the incorrect frequency dictionary for hello_world.txt',
    'test_frequency_1a' : 'Your function generated the incorrect frequency dictionary for test1a',
    'test_frequency_1b':  'Your function generated the incorrect frequency dictionary for test1b',
    'test_ngrams_empty': 'Your function fails to generate an empty ngram list for the empty string',
    'test_ngrams_hello': 'Your function generates the incorrect ngrams for a sentence with repeated words',
    'test_ngrams_zero': 'Your function fails to return [] for an invalid n',
    'test_ngrams_aeiou': 'Your function generates the incorrect ngrams for larger values of n',
    'test_similarity1': 'Your function generated an incorrect similarity for identical frequency dictionaries',
    'test_similarity2': 'Your function generated an incorrect similarity for an empty frequency dictionary',
    'test_similarity3': 'Your function generated an incorrect similarity for similar word frequency dictionaries',
    'test_similarity4': 'Your function generated an incorrect similarity for dissimilar word frequency dictionaries',
    'test_difference1':'Your function generated an incorrect dissimilarity (difference = True) for similar word frequency dictionaries',
    'test_difference2':'Your function generated an incorrect dissimilarity (difference = True) for an empty frequency dictionary',
    'test_words1': 'You did not find the most frequent word from a frequency dictionary',
    'test_words2': 'You did not find the most frequent words in the case of a tie',
    'test_closest_3': 'Your function find_closest_match returned an incorrect answer when comparing against a query of three words.',
    'test_closest_none': 'Your function find_closest_match returned an incorrect answer in the empty set, i.e. there are no files to compare.',
    'test_closest_nomatch': 'Your function find_closest_match returned an incorrect answer in the case of no match.',
    'test_closest_tie_with_ngrams': 'Your function find_closest_match returned an incorrect answer in the case of a tie.',
    'test_closest_ngrams': 'Your function find_closest_match does not correctly use n-grams.'
}

error_messages = {
    'test_prep_hello_world': 'Your function generated an error while preparing hello_world.txt',
    'test_prep_all_whitespace': 'Your function generated an error while preparing a string with multiple types of whitespace.',
    'test_prep_1a': 'Your function generated an error while preparing test1a.txt',
    'test_frequency_hello_world' : 'Your function produced an error while generating a frequency dictionary for hello_world.txt',
    'test_frequency_1a' : 'Your function produced an error while generating a frequency dictionary for 1a',
    'test_frequency_1b':  'Your function produced an error while generating a frequency dictionary for 1b',
    'test_ngrams_empty': 'Your n-gram function produces an error for the empty string',
    'test_ngrams_hello': 'Your n-gram function produces an error for a sentence with repeated words',
    'test_ngrams_aeiou':  'Your n-gram function produces an error for a larger value of n',
    'test_ngrams_zero': 'Your n-gram function produces an error for n = 0',
    'test_similarity1': 'Your similarity function produces an error for identical frequency dictionaries',
    'test_similarity2': 'Your similarity function produces an error for an empty frequency dictionary.',
    'test_similarity3': 'Your similarity function produces an error for similar word frequency dictionaries',
    'test_similarity4': 'Your similarity function produces an error for dissimilar word frequency dictionaries',
    'test_difference1': 'Your compute_similarity_score function produces an error for similar word frequency dictionaries when returning the difference score (difference=True)',
    'test_difference2': 'Your compute_similarity_score function produces an error for an empty frequency dictionary when returning the difference score (difference=True)',
    'test_words1': 'Your function produced an error when finding the most frequent word from a frequency dictionary',
    'test_words2': 'Your function produced an error in the case of a tie',
    'test_words3': 'Your function produced an error when finding the most frequent word in a loaded text',
    'test_closest_3': 'Your function find_closest_match produced an error when comparing against a query of three words.',
    'test_closest_none': 'Your function find_closest_match produced an error in the empty set, i.e. there are no files to compare.',
    'test_closest_nomatch': 'Your function find_closest_match produced an error in the case of no match.',
    'test_closest_tie_with_ngrams': 'Your function find_closest_match produced an error in the case of a tie.',
    'test_closest_ngrams': 'Your function find_closest_match produced an error.'
}

# Subclass to track a point score and appropriate
# grade comment for a suit of unit tests
class Results_600(unittest.TextTestResult):
    # We override the init method so that the Result object
    # can store the score and appropriate test output.
    def __init__(self, *args, **kwargs):
        super(Results_600, self).__init__(*args, **kwargs)
        self.output = []
        self.points = 5

    def addFailure(self, test, err):
        test_name = test._testMethodName
        self.handleDeduction(test_name, failure_messages[test_name])
        super(Results_600, self).addFailure(test, err)

    def addError(self, test, err):
        test_name = test._testMethodName
        self.handleDeduction(test_name, error_messages[test_name])
        super(Results_600, self).addError(test, err)

    def handleDeduction(self, test_name, messages):
        point_value = point_values[test_name]
        self.output.append('[-%s]: %s' % (point_value, messages))
        self.points -= point_value
    def getOutput(self):
        if len(self.output) == 0:
            return "All correct!"
        return '\n'.join(self.output)

    def getPoints(self):
        return round(self.points, 3)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLoadFile))
    suite.addTest(unittest.makeSuite(TestNgrams))
    suite.addTest(unittest.makeSuite(TestComputeFrequencies))
    suite.addTest(unittest.makeSuite(TestSimilarity))
    suite.addTest(unittest.makeSuite(TestMostFrequent))
    suite.addTest(unittest.makeSuite(TestClosestArtist))
    result = unittest.TextTestRunner(verbosity=4, resultclass=Results_600).run(suite)

    output = result.getOutput()
    points = result.getPoints()
    #sys.stdout=store
    print("\n\nProblem Set 3 Unit Test Results:")
    print(output)
    print("Points: %s/5\n" % points)

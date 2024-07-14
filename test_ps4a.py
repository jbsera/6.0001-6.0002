# for running unit tests on 6.00/6.0001/6.0002 student code

import unittest
import ps4a as student

# A class that inherits from unittest.TestCase, where each function
# is a test you want to run on the student's code. For a full description
# plus a list of all the possible assert methods you can use, see the
# documentation: https://docs.python.org/3/library/unittest.html#unittest.TestCase
class TestPS4A(unittest.TestCase):

    ### test representation
    def test_data_representation(self):

        student_tA = student.treeA
        student_tB = student.treeB
        student_tC = student.treeC

        # # check lengths
        tree_length_msg = "Your list for %s has length %s, but should be length %s."
        self.assertEqual(len(student_tA), 2, tree_length_msg % ('treeA', len(student.treeA), 2))
        self.assertEqual(len(student_tB), 2, tree_length_msg % ('treeB', len(student.treeB), 2))
        self.assertEqual(len(student_tC), 3, tree_length_msg % ('treeC', len(student.treeC), 3))

        # check children
        self.assertEqual(student_tA[0], [14,19], "The left subtree of tree1 is incorrect.")
        self.assertEqual(student_tA[1], [[3,5],0], "The right subtree of tree1 is incorrect.")
        self.assertEqual(student_tB[0], [9,3], "The left subtree of tree2 is incorrect.")
        self.assertEqual(student_tB[1], 6, "The right subtree of tree2 is incorrect.")
        self.assertEqual(student_tC[0], [7], "The leftmost subtree of tree3 is incorrect.")
        self.assertEqual(student_tC[1], [16,4,2], "The middle subtree of tree3 is incorrect.")
        self.assertEqual(student_tC[2], [8], "The rightmost subtree of tree3 is incorrect.")

    ### tests for add_tree
    def test_add_example_trees(self):
        expected_1 = 41
        expected_2 = 18
        expected_3 = 37

        actual_1 = student.add_tree(student.treeA)
        actual_2 = student.add_tree(student.treeB)
        actual_3 = student.add_tree(student.treeC)

        self.assertEqual(actual_1, expected_1, "Expected add(treeA) to be 41, but got %s" % actual_1)
        self.assertEqual(actual_2, expected_2, "Expected add(treeB) to be 18, but got %s" % actual_2)
        self.assertEqual(actual_3, expected_3, "Expected add(treeC) to be 37, but got %s" % actual_3)

    ### tests for op_tree
    def test_op_sum_example_trees(self):

        def sumem(a,b):
            """
            Example operator function.
            Takes in two integers, returns their sum.
            """
            return a + b

        expected_1 = 41
        expected_2 = 18
        expected_3 = 37

        actual_1 = student.op_tree(student.treeA, sumem, 0)
        actual_2 = student.op_tree(student.treeB, sumem, 0)
        actual_3 = student.op_tree(student.treeC, sumem, 0)

        self.assertEqual(actual_1, expected_1, "Expected op_tree(treeA, sumem, 0) to be 41, but got %s" % actual_1)
        self.assertEqual(actual_2, expected_2, "Expected op_tree(treeB, sumem, 0) to be 21, but got %s" % actual_2)
        self.assertEqual(actual_3, expected_3, "Expected op_tree(treeC, sumem, 0) to be 37, but got %s" % actual_3)

    def test_op_prod_example_trees(self):

        def prod(a,b):
            """
            Example operator function.
            Takes in two integers, returns their product.
            """
            return a * b

        expected_1 = 0
        expected_2 = 162
        expected_3 = 7168

        actual_1 = student.op_tree(student.treeA, prod, 1)
        actual_2 = student.op_tree(student.treeB, prod, 1)
        actual_3 = student.op_tree(student.treeC, prod, 1)

        self.assertEqual(actual_1, expected_1, "Expected op_tree(treeA, prod, 1) to be 0, but got %s" % actual_1)
        self.assertEqual(actual_2, expected_2, "Expected op_tree(treeB, prod, 1) to be 162, but got %s" % actual_2)
        self.assertEqual(actual_3, expected_3, "Expected op_tree(treeC, prod, 1) to be 7168, but got %s" % actual_3)


    def test_op_search_greater_ten_example_trees(self):

        expected_1 = True
        expected_2 = False
        expected_3 = True

        actual_1 = student.op_tree(student.treeA, student.search_greater_ten, False)
        actual_2 = student.op_tree(student.treeB, student.search_greater_ten, False)
        actual_3 = student.op_tree(student.treeC, student.search_greater_ten, False)

        self.assertEqual(actual_1, expected_1, "Expected op_tree(treeA, search_greater_ten, False) to be True, but got %s" % actual_1)
        self.assertEqual(actual_2, expected_2, "Expected op_tree(treeB, search_greater_ten, False) to be False, but got %s" % actual_2)
        self.assertEqual(actual_3, expected_3, "Expected op_tree(treeC, search_greater_ten, False) to be True, but got %s" % actual_3)


# Dictionary mapping function names from the above TestCase class to
# the point value each test is worth.
point_values = {
	'test_data_representation' : 0.3,
    'test_add_example_trees' : 0.5,
	'test_op_sum_example_trees' : 0.4,
	'test_op_prod_example_trees' : 0.4,
	'test_op_search_greater_ten_example_trees': 0.5
}

# Subclass to track a point score and appropriate
# grade comment for a suit of unit tests
class Results_600(unittest.TextTestResult):

    # We override the init method so that the Result object
    # can store the score and appropriate test output.
    def __init__(self, *args, **kwargs):
        super(Results_600, self).__init__(*args, **kwargs)
        self.output = []
        self.points = 2

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
	suite.addTest(unittest.makeSuite(TestPS4A))
	result = unittest.TextTestRunner(verbosity=2, resultclass=Results_600).run(suite)

	output = result.getOutput()
	points = result.getPoints()

	# weird bug with rounding
	if points < .1:
		points = 0

	print("\nProblem Set 4A Unit Test Results:")
	print(output)
	print("Points: %s/2\n" % points)

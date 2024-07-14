# Problem Set 4A
# Name: Joy Bhattacharya
# Collaborators: Sang(Jess) Eun Han 
# Time Spent: 2 hours
# Late Days Used: x

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
treeA = [[14,19],[[3,5],0]]
treeB = [[9,3],6]
treeC = [[7],[16,4,2],[8]]

# Part A1: Multiplication on tree leaves

def add_tree(tree):
    """
    Recursively computes the sum of all tree leaves.
    Returns an integer representing the product.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
    Outputs
       total: An int equal to the sum of all the leaves of the tree.

    """
  

    total_sum=0
    if not isinstance(tree,list):#if the tree isn't a list, meaning it's just a number, then the total_sum is just equal to that number
        total_sum=tree
    else: #if the tree is a list 
        for subtree in tree: #iterate over the subtrees ofyour list
            total_sum+=add_tree(subtree) #increment your total sum by the sum of each subtree. This recursion will continue into each subtree until it reaches a point where the subtree isn't a list and then it will go into the if block.
    return total_sum
            
        


# Part A2: Arbitrary operations on tree leaves

def sumem(a, b):
    """
    Example operator function.
    Takes in two integers, returns their sum.
    """
    return a + b


def prod(a, b):
    """
    Example operator function.
    Takes in two integers, returns their product.
    """
    return a * b


def op_tree(tree, op, base_case):
    """
    Recursively runs a given operation on tree leaves.
    Return type depends on the specific operation.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
       op: A function that takes in two inputs and returns the
       result of a specific operation on them.
       base_case: What the operation should return as a result
       in the base case (i.e. when the tree is empty).
    """
    if len(tree)==0: #if we have an empty list, simply return the value of the base case
        return base_case
    else:
        if isinstance(tree[0], list): #if the first element in the tree is a list, perform the operation recursively on the first emelent and all other elements
            return op(op_tree(tree[0], op, base_case),op_tree(tree[1:], op, base_case))
        else:
            a=tree[0] #if the first element is not a list, peform the operation between that first element and every other element in tree
            return op(a,op_tree(tree[1:],op, base_case))        
            
        
        


# Part A3: Searching a tree

def search_greater_ten(a, b):
    """
    Operator function that searches for greater-than-10 values within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or > 10, and False otherwise
    """
    
    if a==True or b==True or a>10 or b>10: #checks is either A or B is true or if they're over the number 10
        return True
    else:
        return False


# Part A4: Find the maximum element of a tree using op_tree and max() in the
# main function below (remembering to pass the function in without parenthesis)
if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below.
    tree = [[14,19],[[3,5],0]] #initialize a specific tree
    op_tree(tree, max, base_case=0) #call your op_tree with the max as your op funciton. The base_case should equal zero to ensure that the base case can never be the maximum if tree has positive integers. 
    pass
    

################################################################################
# 6.0002 Fall 2020
# Problem Set 1
# Name: Joy Bhattacharya 
# Collaborators:
# Time: 10 hours 

from state import *

##########################################################################################################
## Problem 1
##########################################################################################################

def generate_election(filename):
    """
    Reads the contents of a file, with data given in the following tab-delimited format,
    State   Democrat_votes    Republican_votes    EC_votes 
 
    Please ignore the first line of the file, which are the column headers.
    
    Parameters:
    filename - the name of the data file as a string

    Returns:
    a list of State instances
    """
    file=open(filename, 'r') #creates a file object 
    L=[] #initializes an empty list 
    line=file.readlines() #reads the lines in the files 
    for row in line[1:]: #iterates over every line excluding the 1st one 
        row_copy=row.split() #creates a copy of the list created by splitting the row on spaces
        name=row_copy[0] #initializes variables
        dem=row_copy[1]
        gop=row_copy[2]
        ec=row_copy[3]
        new_state_instance=State(name,dem,gop,ec) #creates a state instance with these variables for the specific row 
        L.append(new_state_instance) #appends the state instance to a list 
    file.close() #closes the file 
    return L #returns the list 
##########################################################################################################
## Problem 2: Helper functions 
##########################################################################################################

def election_result(election):
    """
    Finds the winner of the election based on who has the most amount of EC votes.
    Note: In this simplified representation, all of EC votes from a state go
    to the party with the majority vote.

    Parameters:
    election - a list of State instances 

    Returns:
    a tuple, (winner, loser) of the election i.e. ('dem', 'gop') if Democrats won, else ('gop', 'dem')
    """
    Dem_votes=0
    Gop_votes=0
    for state in election: #iterates over state
        if state.get_winner()=="dem": #if the winner of the state is the democrat then get the number of electoral votes won from that state
            Dem_votes+=state.get_ecvotes() #find the total number of democratic votes by incrementing by the number of votes the dem won from each state
        else: #else get the electoral votes won by the GOP from that state
            Gop_votes+=state.get_ecvotes() #find the total number of gop votes by incrementing by the number of votes the gop won from each state
    if Dem_votes>Gop_votes: #if the democrat won more electoral college votes than the gop, make a tuple that shows the dem won
        final_result=('dem','gop')
    else: #else make a tuple that shows the gop won 
        final_result=('gop','dem')
    return final_result #return the tuple of the winner 


def winner_states(election):
    """
    Finds the list of States that were won by the winning candidate (lost by the losing candidate).

    Parameters:
    election - a list of State instances 

    Returns:
    A list of State instances won by the winning candidate
    """
    Dem_votes=0 #initialized empty variables and lists 
    Gop_votes=0
    Dem_list=[]
    Gop_list=[]
    for state in election: #iterates over state
        if state.get_winner()=="dem": #if the winner of the state is the democrat:
            Dem_votes+=state.get_ecvotes() #increment the dem's total number of electoral college votes by the votes they get from a state they won
            Dem_list.append(state) #add the state instance to the dem list 
        else: #else get the electoral votes won by the GOP from that state
            Gop_votes+=state.get_ecvotes() #increment GOP total ec votes by the votes they won from the state they won   
            Gop_list.append(state) #add the state instance to the GOP list 
    if Dem_votes>Gop_votes: #if the democrat won more electoral college votes than the gop, return the dem list 
        return Dem_list
    else: #otherwise if the Gop won, return the Gop list 
        return Gop_list 



def ec_votes_needed(election, total=538):
    """
    Finds the number of additional EC votes required by the loser to change election outcome.
    Note: A party wins when they earn half the total number of EC votes plus 1.

    Parameters:
    election - a list of State instances 
    total - total possible number of EC votes

    Returns:
    int, number of additional EC votes required by the loser to change the election outcome
    """
    winner_ec_votes=0
    for state in winner_states(election): #finds the total number of ec votes won by the winner 
        winner_ec_votes+=state.get_ecvotes()
    loser_ec_votes=total-winner_ec_votes #loser ec votes would be the total number of votes minus the winner ec votes 
    votes_needed=(total//2+1)-loser_ec_votes #votes needed to flip the election for the loser would be the majority required to win minus how many the loser originally won 
    return votes_needed
    

##########################################################################################################
## Problem 3: Brute Force approach
##########################################################################################################

def get_binary_representation(n, num_digits):
    """
    Helper function to get a binary representation of items to add to a subset,
    which combinations() uses to construct and append another item to the powerset.
    
    Parameters:
    n and num_digits are non-negative ints
    
    Returns: 
        a num_digits str that is a binary representation of n
    """
    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n//2
    if len(result) > num_digits:
        raise ValueError('not enough digits')
    for i in range(num_digits - len(result)):
        result = '0' + result
    return result

def combinations(L):
    """
    Helper function to generate powerset of all possible combinations
    of items in input list L. E.g., if
    L is [1, 2] it will return a list with elements
    [], [1], [2], and [1,2].

    Parameters:
    L - list of items

    Returns:
    a list of lists that contains all possible
    combinations of the elements of L
    """
    powerset = []
    for i in range(0, 2**len(L)):
        binStr = get_binary_representation(i, len(L))
        subset = []
        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset

def brute_force_swing_states(winner_states, ec_votes):
    """
    Finds a subset of winner_states that would change an election outcome if
    voters moved into those states, these are our swing states. Iterate over
    all possible move combinations using the helper function combinations(L).
    Return the move combination that minimises the number of voters moved. If
    there exists more than one combination that minimises this, return any one of them.

    Parameters:
    winner_states - a list of State instances that were won by the winner 
    ec_votes - int, number of EC votes needed to change the election outcome

    Returns:
    A list of State instances such that the election outcome would change if additional
    voters relocated to those states 
    The empty list, if no possible swing states
    """
    
    L=[] #initialize empty lists and variables 
    min_so_far=0
    final_list=[]
    for possible_combination in combinations(winner_states): #iterate over every possible combination
        voters_moved=0 #initialize variables 
        x=0
        for state in possible_combination: #iterate over every state in the given combination
            x+=state.get_ecvotes() #finds the total number of ec votes 
            voters_moved+=state.get_margin()+1 #finds the total number of voters moved 
        if x>=ec_votes and voters_moved>0: #if the combination gives you enough ec votes to win and your voters moved is above 0 (so this will exclude the combination of an empty list)
            L.append(voters_moved) #append your voters moved to a list 
            min_so_far=min(L) #find the minimum number of voters moved throughout all the combinations
            if voters_moved==min_so_far: #if your voters moved is equal to the min set that combination as your final combination
                final_list=possible_combination
    return final_list #return the final combination 
    
##########################################################################################################
## Problem 4: Dynamic Programming
## In this section we will define two functions, max_voters_move and min_voters_move, that
## together will provide a dynamic programming approach to find swing states. This problem
## is analagous to the complementary knapsack problem, you might find Lecture 1 of 6.0002 useful 
## for this section of the pset. 
##########################################################################################################
def memo_helper(winner_states, ec_votes, memo=None):
    if memo == None:
        memo = {}
    if (len(winner_states), ec_votes) in memo: #finds the combination if it is already stored in memo
        result = memo[(len(winner_states), ec_votes)]
    elif winner_states == [] or ec_votes == 0: #if we have an empty list or no ec_votes, return an empty list 
        result = (0, [])
    elif winner_states[0].get_ecvotes() > ec_votes: #if the ec_votes of the state is greater than our ec_votes, exclude the state and only analyze the right part of the branch
        #Explore right branch only
        result = memo_helper(winner_states[1:], ec_votes, memo) #recursively call the function on a list of states excluding the left one 
    else:
        nextItem = winner_states[0] #if we want to include the left state 
        #Explore left branch
        withVal, withToTake =\
                 memo_helper(winner_states[1:],
                            ec_votes - nextItem.get_ecvotes(), memo) #recursively explore the left side of the branch, adjusting the ec votes we have left by the ec votes the state we started from took
        withVal += nextItem.get_margin()+1 #increment the value by the number of voters needed to be moved 
        #Explore right branch
        withoutVal, withoutToTake = memo_helper(winner_states[1:], #explore what happens if we don't take the left state recursively
                                                ec_votes, memo)
        #Choose better branch
        if withVal > withoutVal: #if withVal is better 
            result = (withVal, withToTake + [nextItem]) #your result is a tuple with that state decided
        else:
            result = (withoutVal, withoutToTake) #otherwise your result does not include that state
    memo[(len(winner_states), ec_votes)] = result #stores the result in memo
    return result



def max_voters_move(winner_states, ec_votes, memo=None):
    """
    Finds the largest number of voters needed to relocate to get at most ec_votes
    for the election loser. 

    Analogy to the knapsack problem:
    Given a list of states each with a weight(#ec_votes) and value(#margin+1),
    determine the states to include in a collection so the total weight(#ec_votes)
    is less than or equal to the given limit(ec_votes) and the total value(#voters displaced)
    is as large as possible.

    Hint: If using a top-down implementation, it may be helpful to create a helper function

    Parameters:
    winner_states - a list of State instances that were won by the winner 
    ec_votes - int, the maximum number of EC votes 
    memo - dictionary, an OPTIONAL parameter for memoization (don't delete!).
    Note: If you decide to use the memo make sure to override the default value when it's first called.

    Returns:
    A list of State instances such that the maximum number of voters need to be relocated
    to these states in order to get at most ec_votes 
    The empty list, if every state has a # EC votes greater than ec_votes
    """
    if memo == None:
        memo = {}
    return memo_helper(winner_states,ec_votes,memo)[1] #returns the second element in the list from memo_helper, which is the states
    
def min_voters_move(winner_states, ec_votes_needed):
    """
    Finds a subset of winner_states that would change an election outcome if
    voters moved into those states. Should minimize the number of voters being relocated. 
    Only return states that were originally won by the winner (lost by the loser)
    of the election.

    Hint: This problem is simply the complement of max_voters_move. You should call 
    max_voters_move with ec_votes set to (#ec votes won by original winner - ec_votes_needed)

    Parameters:
    winner_states - a list of State instances that were won by the winner 
    ec_votes_needed - int, number of EC votes needed to change the election outcome

    Returns:
    A list of State instances such that the election outcome would change if additional
    voters relocated to those states (also can be referred to as our swing states)
    The empty list, if no possible swing states
    """
    L=[]
    winner_ec_votes=0
    for state in winner_states: #iterates over state to find total number of ec votes won by winner 
        winner_ec_votes+=state.get_ecvotes()
    non_swing_states=max_voters_move(winner_states,winner_ec_votes-ec_votes_needed,memo=None) #calls max voters function to find the non-swing states, ec votes would be the winner ec votes-votes needed
    for state in winner_states: #finds all the swing states from the non-swing states
        if state not in non_swing_states:
            L.append(state)
    return L 
##########################################################################################################
## Problem 5
##########################################################################################################

def relocate_voters(election, swing_states):
    """
    Finds a way to shuffle voters in order to flip an election outcome. Moves voters 
    from states that were won by the losing candidate (states not in winner_states), to 
    each of the states in swing_states. To win a swing state, you must move (margin + 1) 
    new voters into that state. Any state that voters are moved from should still be won 
    by the loser even after voters are moved. Also finds the number of EC votes gained by 
    this rearrangement, as well as the minimum number of voters that need to be moved.
    Note: You cannot move voters out of New York, Washington, Massachusetts, or California. 

    Parameters:
    election - a list of State instances representing the election 
    swing_states - a list of State instances where people need to move to flip the election outcome 
                   (result of min_voters_move or greedy_swing_states)

    Return:
    A tuple that has 3 elements in the following order:
        - a dictionary with the following (key, value) mapping: 
            - Key: a 2 element tuple of str, (from_state, to_state), the 2 letter State names
            - Value: int, number of people that are being moved 
        - an int, the total number of EC votes gained by moving the voters 
        - an int, the total number of voters moved 
    None, if it is not possible to sway the election
    """
    L=['NY','WA','MA','CA'] #list of states you can't move voters from 
    Loser_states=[] #initialize empty list 
    states_winner=winner_states(election) #finds the winner states 
    ec_votes_loser_needs=ec_votes_needed(election, total=538) #finds the number of votes needed to flip the election 
    Loser_dict={} #initialize empty dictionaries and variables 
    Winner_dict={}
    Final_dict={}
    Winner_EC_votes={}
    new_ec_votes=0
    total_voters_moved=0
    ###Creates list of loser states
    for state in election: #iterate over every winner state 
        if state not in states_winner and state.get_name() not in L:
            Loser_states.append(state) #create a list of losing states that only includes states you can move voters from 
    ###Creates dictionary of swing state: voters needed to flip and another dictionary for swing state: ec votes 
    for state in swing_states: #iterates over all winner states 
        Winner_dict[state.get_name()]=(state.get_margin()+1) #creates dictionary with the swing state and the number of voters needed to flip the result of the swing state 
        Winner_EC_votes[state.get_name()]=(state.get_ecvotes()) #create dictionary that keeps track of the number of electoral college votes for each swing state 
    ###Dictionary for losing state: possible voters to move 
    for losing_state in Loser_states:
        Loser_dict[losing_state.get_name()]=losing_state.get_margin()-1 #creates a dictionary that finds the number of voters that could be moved from a state while still preserving the winner of that state 
    ### Process for flipping states 
    for winner_swing_state in Winner_dict.keys(): #iterate over all swing states
        for losing_loser_state in Loser_dict.keys(): #iterate over all the losing states 
            if Winner_dict[winner_swing_state]<=Loser_dict[losing_loser_state]: #if the voters you would need to move to the swing state to win is less than or equal to the max number of voters you could move from a losing state 
                new_ec_votes+=Winner_EC_votes[winner_swing_state] #increment your new ec votes by the votes won from the flipped swing state 
                Loser_dict[losing_loser_state]=Loser_dict[losing_loser_state]-Winner_dict[winner_swing_state] #change the possible voter remaining for relocation by the amount that the loser state moved to the swing state 
                Final_dict[(losing_loser_state, winner_swing_state)]=Winner_dict[winner_swing_state] #create a dictionary of from state: to state with the number of voters moved 
                break #break from the loop in order to try another swing state since you've already won this one
            else:  #if the voters you need to flip the state is more than the voters you can take from the loser's state 
                Winner_dict[winner_swing_state]=Winner_dict[winner_swing_state]-Loser_dict[losing_loser_state] #change the margin of voters you need to win the swing state by the amount you took from the losing state 
                Final_dict[(losing_loser_state, winner_swing_state)]=Loser_dict[losing_loser_state] #the number of voters transfered equals the number of voters in the losing state 
                Loser_dict[losing_loser_state]=0 #Set the remaining voters you can take from the loser state to 0 since you've taken them all. 
    ### finds total voters moved 
    for voters_moved in Final_dict.values():
        total_voters_moved+=voters_moved
    ### finds final result 
    if new_ec_votes>=ec_votes_loser_needs: #if you have successfully flipped the election 
        return (Final_dict, new_ec_votes, total_voters_moved)
    else: #if you can't return the election, return None 
        return None
    
if __name__ == "__main__":
    pass
    # Uncomment the following lines to test each of the problems

    # #tests Problem 1
    year = 2012
    election = generate_election("%s_results.txt" % year)
    # print(len(election))
    # print(election[0])

    # # # tests Problem 2
    winner, loser = election_result(election)
    won_states = winner_states(election)
    names_won_states = [state.get_name() for state in won_states]
    reqd_ec_votes = ec_votes_needed(election)
    # print("Winner:", winner, "\nLoser:", loser)
    # print("States won by the winner: ", names_won_states)
    # print("EC votes needed:",reqd_ec_votes, "\n")

    #tests Problem 3
    brute_election = generate_election("60002_results.txt")
    brute_won_states = winner_states(brute_election)
    brute_ec_votes_needed = ec_votes_needed(brute_election, total=14)
    brute_swing = brute_force_swing_states(brute_won_states, brute_ec_votes_needed)
    names_brute_swing = [state.get_name() for state in brute_swing]
    voters_brute = sum([state.get_margin()+1 for state in brute_swing])
    ecvotes_brute = sum([state.get_ecvotes() for state in brute_swing])
    # print("Brute force swing states results:", names_brute_swing)
    # print("Brute force voters displaced:", voters_brute, "for a total of", ecvotes_brute, "Electoral College votes.\n")

    # tests Problem 4: max_voters_move
    print("max_voters_move")
    total_lost = sum(state.get_ecvotes() for state in won_states)
    non_swing_states = max_voters_move(won_states, total_lost-reqd_ec_votes)
    non_swing_states_names = [state.get_name() for state in non_swing_states]
    max_voters_displaced = sum([state.get_margin()+1 for state in non_swing_states])
    max_ec_votes = sum([state.get_ecvotes() for state in non_swing_states])
    print("States with the largest margins (non-swing states):", non_swing_states_names)
    print("Max voters displaced:", max_voters_displaced, "for a total of", max_ec_votes, "Electoral College votes.", "\n")

    # tests Problem 4: min_voters_move
    # print("min_voters_move")
    swing_states = min_voters_move(won_states, reqd_ec_votes)
    swing_state_names = [state.get_name() for state in swing_states]
    min_voters_displaced = sum([state.get_margin()+1 for state in swing_states])
    swing_ec_votes = sum([state.get_ecvotes() for state in swing_states])
    # print("Complementary knapsack swing states results:", swing_state_names)
    # print("Min voters displaced:", min_voters_displaced, "for a total of", swing_ec_votes, "Electoral College votes. \n")

    # tests Problem 5: relocate_voters
    print("relocate_voters")
    flipped_election = relocate_voters(election, swing_states)
    print("Flip election mapping:", flipped_election)
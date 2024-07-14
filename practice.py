# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:27:08 2020

@author: joyse
"""

L=['NY','WA','MA','CA']
    Loser_states=[]
    states_winner=winner_states(election)
    ec_votes_loser_needs=ec_votes_needed(election, total=538)
    Loser_dict={}
    Winner_dict={}
    Final_dict={}
    Winner_EC_votes={}
    new_ec_votes=0
    total_voters_moved=0
    for state in election: #iterate over every winner state 
        if state not in states_winner and state.get_name() not in L:
            Loser_states.append(state)
    print('------------------------')
    print('THESE ARE THE SWING STATES', swing_states)
    print('THESE ARE THE LOSER STATES', Loser_states)
    print("EC votes needed", ec_votes_loser_needs)
    for state in swing_states: #iterates over all winner states 
        Winner_dict[state.get_name()]=(state.get_margin()+1) #finds number of voters needed to flip the result of the swing state 
        Winner_EC_votes[state.get_name()]=(state.get_ecvotes()) #keeps track of the number of electoral college votes for each swing state 
    for losing_state in Loser_states:
        Loser_dict[losing_state.get_name()]=losing_state.get_margin()-1 #finds the number of voters that could be moved from a state while still preserving the winner of that state 
    print('THIS IS THE LOSING STATE DICTIONARY', Loser_dict)
    print('THESE ARE WINNER STATES', Winner_dict)
    for winner_swing_state in Winner_dict.keys():
        print("state", winner_swing_state, 'ec votes', Winner_EC_votes[winner_swing_state], "margin of voters", Winner_dict[winner_swing_state])
        for losing_loser_state in Loser_dict.keys(): #for all the losing states 
            print('losing state', losing_loser_state, 'losing state voters', Loser_dict[losing_loser_state])
            if Loser_dict[losing_loser_state]==0: #if the loser state has no more voters to give, break and try another state 
                del Loser_dict[losing_loser_state]
                print("Loser state votes=0")
                break
            elif Winner_dict[winner_swing_state]==0: #if the swing state is already won
                print("Swing state already won")
                break
            elif Winner_dict[winner_swing_state]<Loser_dict[losing_loser_state]: #if the voters you would need to move to the swing state to win is less than or equal to the max number of voters you could move from a losing state 
                print('WIN state')
                new_ec_votes+=Winner_EC_votes[winner_swing_state] #increment your new ec votes by the votes won from the flipped swing state 
                Loser_dict[losing_loser_state]=Loser_dict[losing_loser_state]-Winner_dict[winner_swing_state] #change the possible voter remaining for relocation by the amount that the loser state moved to the swing state 
                Final_dict[(losing_loser_state, winner_swing_state)]=Winner_dict[winner_swing_state] #create a dictionary of from state: to state with the number of voters moved 
                Winner_dict[winner_swing_state]=0 #now set the value of voters needed to win the swing state to 0
                print('new ec votes', new_ec_votes)
                break
            elif Winner_dict[winner_swing_state]==Loser_dict[losing_loser_state]:
                new_ec_votes+=Winner_EC_votes[winner_swing_state]
                Final_dict[(losing_loser_state, winner_swing_state)]=Winner_dict[winner_swing_state]
                Loser_dict[losing_loser_state]=0
                Winner_dict[winner_swing_state]=0
                del Loser_dict[losing_loser_state]
            elif Winner_dict[winner_swing_state]>Loser_dict[losing_loser_state]: #if the voters you need to flip the state is more than the voters you can take from the loser's state 
                print('LOSE state')
                Winner_dict[winner_swing_state]=Winner_dict[winner_swing_state]-Loser_dict[losing_loser_state] #change the margin of voters you need to win the swing state by the amount you took from the losing state 
                Final_dict[(losing_loser_state, winner_swing_state)]=Loser_dict[losing_loser_state] #the nuber of voters transfered equals the number of voters in the losing state 
                Loser_dict[losing_loser_state]=0 #Set the remaining voters you can take from the loser state to 0 since you've taken them all 
                del Loser_dict[losing_loser_state]
                break
        print('final dict', Final_dict)
    for voters_moved in Final_dict.values():
        total_voters_moved+=voters_moved
    if new_ec_votes>=ec_votes_loser_needs: #if you have successfully flipped the election 
        print('FINAL ANSWER', (Final_dict, new_ec_votes, total_voters_moved))
        return (Final_dict, new_ec_votes, total_voters_moved)
    else:
        print('COULD NOT FIND ANSWER')
        return None
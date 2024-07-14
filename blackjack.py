# Problem Set 4
# Name: Joy Bhattacharya
# Collaborators: <insert collaborators>
# Time Spent: 12 hours
# Late Days Used: (only if you are using any)

import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import random
from ps4_classes import BlackJackCard, CardDecks, Busted


#############
# PROBLEM 1 #
#############
class BlackJackHand:
    """
    A class representing a game of Blackjack.   
    """

    # Do not modify these three lines, they provide an interface for the tester!
    HIT = 'hit'
    STAND = 'stand'
    DS = 'double-stand'
    #########################

    def __init__(self, deck, init_bet=1.0):
        """
        Parameters:
        deck - An instance of CardDeck that represents the starting shuffled
               card deck (this deck itself contains one or more standard card decks)
        init_bet - float, represents the init bet/wager of the hand

        Attributes:
        self.deck - CardDeck, represents the shuffled card deck for this game of BlackJack
        self.current_bet - float, represents the current bet/wager of the hand
        self.player - list, initialized with the first 2 cards dealt to the player
                      and updated as the player is dealt more cards from the deck
        self.dealer - list, initialized with the first 2 cards dealt to the dealer
                      and updated as the dealer is dealt more cards from the deck

        Important: You MUST deal out the first four cards in the following order:
            player, dealer, player, dealer
            
            You may find the deal_card function (and others) in ps4_classes.py helpful.
        """
        self.deck=deck
        self.current_bet=init_bet
        self.player=[]
        self.dealer=[]
        self.player.append(deck.deal_card())
        self.dealer.append(deck.deal_card())
        self.player.append(deck.deal_card())
        self.dealer.append(deck.deal_card())

    # Do not modify!
    def set_bet(self, new_bet):
        """
        Sets the player's current wager in the game.

        Parameters:
        new_bet - the floating point number representing the new wager for the game.

        Do not modify!
        """
        self.current_bet = new_bet

    # Do not modify!
    def get_bet(self):
        """
        Returns the player's current wager in the game.

        Returns:
        self.current_bet, the floating point number representing the current wager for the game

        Do not modify!
        """
        return self.current_bet
        
    # Do not modify this function!
    def set_initial_cards(self, player_cards, dealer_cards):
        """
        Sets the initial cards of the game.
        player_cards - list, containing the inital player cards
        dealer_cards - list, containing the inital dealer cards

        used for testing, DO NOT MODIFY
        """
        self.player = player_cards[:]
        self.dealer = dealer_cards[:]

    # You can call the method below like this:
    #   BlackJackHand.best_value(cards)
    @staticmethod
    def best_value(cards):
        """
        Finds the total value of the cards. All cards must contribute to the
        best sum; however, an Ace may contribute a value of 1 or 11.

        The best sum is the highest point total not exceeding 21 if possible.
        If it is not possible to keep the total value from exceeding 21, then
        the best sum is the lowest total value of the cards.

        Hint: If you have one Ace, give it a value of 11 by default. If the sum
        point total exceeds 21, then give it a value of 1. What should you do
        if cards has more than one Ace?

        Parameters:
        cards - a list of BlackJackCard instances.

        Returns:
        int, best sum of point values of the cards  
        """
        total_value=0
        number_of_aces=0
        for card in cards:
            total_value+=card.get_val() #Keeps track of the total card value 
            if card.get_rank()=='A':
                number_of_aces+=1 #Keeps track of the total number of aces 
        if total_value<=21: #if the total value on your cards is less than or equal to 21, then return that value
            return total_value
        elif number_of_aces>0: #if you exceed your point total, we'll initially convert all aces to a value of 1 and recalculate the total value
            for ace in range(number_of_aces):
                total_value-=10 #decreasing the total_value by 10 for every ace
            while (21-total_value)>=10: #while the difference between 21 and your total value is greater than or equal to 10, add an ace of full value (11) back
                total_value+=10
            return total_value
        else: #if you don't have any aces but youre best value is still over 21
            return total_value
        

    def get_player_cards(self):
        """
        Returns:
        list, a copy of the player's cards 
        """
        return self.player.copy()

    def get_dealer_cards(self):
        """
        Returns:
        list, a copy of the dealer's cards 
        """
        return self.dealer.copy()

    def get_dealer_upcard(self):
        """
        Returns the dealer's face up card. We define the dealer's face up card
        as the first card in their hand.

        Returns:
        BlackJackCard instance, the dealer's face-up card 
        """
        face_up_card=self.dealer[0] #gets the dealer's first card
        return face_up_card

    # Strategy 1
    def copy_dealer_strategy(self):
        """
        A playing strategy in which the player uses the same metric as the
        dealer to determine their next move.

        The player will:
            - hit if the best value of their cards is less than 17
            - stand otherwise

        Returns:
        str, "hit" or "stand" representing the player's decision  
        """
        cards=self.get_player_cards()
        if self.best_value(cards)<17: #hit is best value is below 17, stand if otherwise 
            return self.HIT
        else:
            return self.STAND
    # Strategy 2
    def cheating_strategy(self):
        """
        A playing strategy in which the player knows the best value of the
        dealer's cards.

        The player will:
            - hit if the best value of their hand is less than that of the dealer's
            - stand otherwise

        Returns:
        str, "hit" or "stand" representing the player's decision
        """
        dealer_cards=self.get_dealer_cards()
        player_cards=self.get_player_cards()
        if self.best_value(player_cards)<self.best_value(dealer_cards): #hit if player cards has less value than dealer cards
            return self.HIT
        else:
            return self.STAND

    # Strategy 3
    def basic_strategy(self):
        """
        A playing strategy in which the player will
            - stand if one of the following is true:
                - the best value of player's hand is greater than or equal to 17
                - the best value of player's hand is between 12 and 16 (inclusive)
                  AND the dealer's up card is between 2 and 6 (inclusive)  
            - hit otherwise

        Returns:
        str, "hit" or "stand" representing the player's decision 
        """
        player_sweet_spot=[12,13,14,15,16]
        dealer_sweet_spot=[2,3,4,5,6]
        up_card=self.get_dealer_upcard().get_val()
        player_cards=self.get_player_cards()
        if self.best_value(player_cards)>=17: #stand if greater than or equal to 17
            return self.STAND
        elif self.best_value(player_cards) in player_sweet_spot and up_card in dealer_sweet_spot: #stand if both are in the range
            return self.STAND
        else: #else hit 
            return self.HIT

    # Strategy 4
    def double_stand_strategy(self):
        """
        A playing strategy in which the player will
            - double-stand (DS) if the following is true:
                - the best value of the player's cards is 11
            - else they will fall back to using basic_strategy

        In our game, we allow "doubling stand" (DS) on any turn, rather than just the first turn.

        The double stand action indicates a special, somewhat risky, but possibly rewarding player
        action. It means the player wishes to double the current bet of the hand, hit one more time,
        and then immediately stand, ending their turn with whatever cards result. 

        This strategy simply consists of signaling to that the calling function with the action
        BlackJackHand.DS when the sum of the players cards is 11, which is a very good
        position in which to try to double one's bet while getting only one more card. Otherwise,
        the strategy falls back to using the basic_strategy to play normally.
        
        NOTE: This function should not double your bet.

        Returns:
        str, "double-stand" if player_best_score == 11,
             otherwise the return value of calling basic_strategy to play in the default way
        """
        player_cards=self.get_player_cards()
        if self.best_value(player_cards)==11:  #double stand if equal to 11
            return self.DS
        else:
            return self.basic_strategy() #else, revert to the basic strategy
    # Strategy 5
    def random_strategy(self):
        """
        A playing strategy in which the player will
            - stand if the following is true:
                - the best value of player's hand is greater than or equal to 16
            - hit if the following is true:
                - the best value of player's hand is less than or equal to 12
            - otherwise:
                - toss a coin and hit if the result of the coin toss is a head, stand otherwise
                  (the 'random' library is already imported for you - think of ways to mimic a coin toss through it).

        Returns:
        str, "hit" or "stand" representing the player's decision
        """
        coin_toss=['Heads', 'Tails']
        player_cards=self.get_player_cards()
        if self.best_value(player_cards)>=16: #stand if greater than or equal to 16
            return self.STAND
        elif self.best_value(player_cards)<=12: #hit if less than or equal to 12
            return self.HIT
        else:
            choice=random.choice(coin_toss) #randomly choose whether to hit or stand
            if choice=='Heads':
                return self.HIT
            else:
                return self.STAND
            

    def play_player_turn(self, strategy):
        """
        Plays a full round of the player's turn and updates the player's hand
        to include new cards that have been dealt to the player (a hit). The player
        will be dealt a new card until they stand, bust, or double-stand.

        With double-stand, the player doubles their bet, receive one final hit, and
        then they stand. The hit with double-stand strategy (like any hit) can cause the player to
        go bust.

        The following will guide you through some design requirements for this function. 

        This function must _repeatedly_ query the strategy for the next action, until the action
        is to stand, or until their hand's best value is over 21, which should then raise a Busted
        exception (imported from ps4_classes.py) to signal this sad outcome to the caller.

        Remember, receiving the double-stand action from a strategy indicates:
            - the player wishes to double their current bet,
            - the player receives one last hit,
            - the player then immediately stands, ending their turn

        Remember, 
            - Whenever hitting, always signal to the caller if the best value of the 
              player's hand becomes greater than 21 (because the player has busted).

        Parameter:
        strategy - function, one of the the 4 playing strategies defined in BlackJackHand
                   (e.g. BlackJackHand.copy_dealer_strategy, BlackJackHand.double_stand_strategy)

        Returns:          
        This function does not return anything.

        """
        player_cards=self.get_player_cards() #initialize the list of player cards
        while self.best_value(player_cards)<21: #continue while the value of the cards is under 21
            if strategy(self)==self.STAND: #if standing, break from the loop
                break
            ###They want to draw a card
            elif strategy(self)==self.HIT: #if hitting, deal a new card and update their list of player cards
                self.player.append(self.deck.deal_card())
                player_cards=self.get_player_cards()
            elif strategy(self)==self.DS: #if double standing, double their bet and update the player's card list 
                self.current_bet=2*self.current_bet
                self.player.append(self.deck.deal_card())
                player_cards=self.get_player_cards()
                break #the player stands 
            if self.best_value(player_cards)>21: #if you've gone bust, raise a Busted exception 
                raise Busted(Exception)
                break
               
                
        

    def play_dealer_turn(self):
        """
        Plays a full round of the dealer's turn and updates the dealer's hand
        to include new cards that have been dealt to the dealer. The dealer
        will get a new card as long as the best value of their hand is less
        than 17. If they go over 21, they bust.

        This function does not return anything. Instead, it:
            - Adds a new card to self.dealer each time the dealer hits.
            - Raises Busted exception (imported from ps4_classes.py) if the
              best value of the dealer's hand is greater than 21.
        """
        dealer_cards=self.get_dealer_cards() #initialize the list of player cards
        while self.best_value(dealer_cards)<17: #continue while the value of the cards is under 17
           self.dealer.append(self.deck.deal_card())
           dealer_cards=self.get_dealer_cards()
           if self.best_value(dealer_cards)>21: #if you've gone bust, raise a Busted exception 
                raise Busted(Exception)
                break

    def __str__(self):
        """
        Returns:
        str, representation of the player and dealer and dealer hands.

        Useful for debugging. DO NOT MODIFY. 
        """
        result = 'Player: '
        for c in self.player:
            result += str(c) + ','
        result = result[:-1] + '    '
        result += '\n   Dealer '
        for c in self.dealer:
            result += str(c) + ','
        return result[:-1]

#############
# PROBLEM 2 #
#############


def play_hand(deck, strategy, init_bet=1.0):
    """
    Plays a hand of Blackjack and determines the amount of money the player
    gets back based on the bet/wager of the hand.

    The player will get:

        - 2.5 times the bet of the hand if the player's first two cards equal 21,
          and the dealer's first two cards do not equal 21. YES

        - 2 times the bet of the hand if the player wins by having a higher best value than 
          the dealer after the dealer's turn concludes YES

        - 2 times the bet of the hand if the dealer busts YES

        - the exact bet amount of the hand if the game ends in a tie. 
          If the player and dealer both get blackjack from their first two cards, 
          this is also a tie.

        - 0 if the dealer wins with a higher best value, or the player busts.

        Remember, the double-stand strategy doubles the current bet under certain conditions.
        You do not have to worry about doubling the bet here for any double-stand if
        your double-stand strategy properly signals to alter the bet of the hand during the
        player's turn.

        Reminder of how the game flow works:

        1. Deal cards to player, then dealer, then player, then dealer.

        2. Check for initial blackjacks from either player. If at least one person has 
           blackjack, the game is over. Calculate how much the player receives.

        3. If no one has blackjack, then deal the player until they stand or bust 
           (use your play_player_turn function).

           If you catch a Busted exception from the player playing their turn,
           the player busted, and the game is over. Calculate how much the player receives.

        4. If the player has not bust, then deal the dealer until they stand or bust.
           (use your play_dealer_turn function).
           If the dealer busts, the game is over. Calculate how much the player receives.

        5. If no one has bust, determine the outcome of the game based on the
            best value of the player's cards and the dealer's cards.

    Parameters:
        deck - an instance of CardDeck
        strategy - function, one of the the four playing strategies defined in BlackJackHand
                   (e.g. BlackJackHand.copy_dealer_strategy)
        init_bet - float, the amount that the player initially bets (default=1.0)

    Returns:
        tuple (float, float): (amount_wagered, amount_won)
               amount_wagered, the current bet of the hand. Should use hand.get_bet().
               amount_won, the amount of money the player gets back. Should be 0 if they busted and lost.
    """
    game=BlackJackHand(deck, init_bet)
    p2_card_value=game.best_value(game.player) #gets the value of the player's first two cards 
    d2_card_value=game.best_value(game.dealer)#gets the value of the dealer's first two cards 
    if p2_card_value==21 and d2_card_value==21: #if both the player's and the dealer's first cards add to 21, they tie
        winnings=game.get_bet()
        final_tuple=(game.get_bet(), winnings)
        return final_tuple
    elif p2_card_value==21: #gets 2.5 times bet if the player's first two cards equal 21 and the dealer's don't
        winnings=2.5*game.get_bet()
        final_tuple=(game.get_bet(), winnings)
        return final_tuple
    elif d2_card_value==21: #dealer wins immediately
        winnings=0
        final_tuple=(game.get_bet(), winnings)
        return final_tuple
    ###Start playing beyond first two cards
    else:
        try: #Proceed with this if the player doesn't bust
            game.play_player_turn(strategy)
            pfinal_value=game.best_value(game.player)
        except: #if the player busted
            winnings=0
            final_tuple=(game.get_bet(), winnings)
            return final_tuple
        try:
            game.play_dealer_turn()
            dfinal_value=game.best_value(game.dealer)
        except: #if the dealer busts
            winnings=2*game.get_bet()
            final_tuple=(game.get_bet(), winnings)
            return final_tuple
        if pfinal_value>dfinal_value: #if the player has a higher final value then the dealer
            winnings=2*game.get_bet()
        elif pfinal_value<dfinal_value: #if the dealer has a higher final value than the player
            winnings=0
        else: #if they tie 
            winnings=game.get_bet()
        final_tuple=(game.get_bet(), winnings)
        return final_tuple

#############
# PROBLEM 3 #
#############


def run_simulation(strategy, init_bet=2.0, num_decks=8, num_hands=20, num_trials=4000, show_plot=False):
    """
    Runs a simulation and generates a normal distribution reflecting 
    the distribution of player's rates of return across all trials.

    The normal distribution is based on the mean and standard deviation of 
    the player's rates of return across all trials. 
    You should also plot the histogram of player's rates of return that 
    underlies the normal distribution. 
    For hints on how to do this, consider looking at 
        matplotlib.pyplot
        scipy.stats.norm.pdf

    For each trial:

        - instantiate a new CardDeck with the num_decks and type BlackJackCard
        - for each hand in the trial, call play_hand and keep track of how
          much money the player receives across all the hands in the trial
        - calculate the player's rate of return, which is
            100*(total money received-total money bet)/(total money bet)

    Parameters:

        strategy - function, one of the the four playing strategies defined in BlackJackHand
                   (e.g. BlackJackHand.copy_dealer_strategy)
        init_bet - float, the amount that the player initially bets each hand. (default=2)
        num_decks - int, the number of standard card decks in the CardDeck. (default=8)
        num_hands - int, the number of hands the player plays in each trial. (default=20)
        num_trials - int, the total number of trials in the simulation. (default=100)
        show_plot - bool, True if the plot should be displayed, False otherwise. (default=False)

    Returns:

        tuple, containing the following 3 elements:
            - list of the player's rate of return for each trial
            - float, the average rate of return across all the trials
            - float, the standard deviation of rates of return across all trials


    MORE PLOTTING HINTS:

    y_values = stats.norm.pdf(x_values, avg, std), This function returns the y-values of the normal distribution
    make sure x_values passed in are sorted. avg and std can be calculated using some numpy functions. 


    """
    Rates=[]
    for trial in range(num_trials):
        total_bets=0
        total_winnings=0
        deck=CardDecks(num_decks,BlackJackCard)
        #deck=Card_deck.create_deck(BlackJackCard)
        for turn in range(num_hands):
            tuple_answer=play_hand(deck, strategy, init_bet)
            total_bets+=tuple_answer[0]
            total_winnings+=tuple_answer[1]
        rate_of_return=100*(total_winnings-total_bets)/(total_bets)
        Rates.append(rate_of_return)
    avg_rate=np.mean(Rates)
    std_rate=np.std(Rates)
    final_tuple=(Rates,avg_rate,std_rate)
    #print('THIS IS THE FINAL TUPLE', final_tuple)
    if show_plot:
        plt.hist(Rates, density=True, histtype='stepfilled', alpha=0.3)
        x=np.linspace(avg_rate-4*std_rate, avg_rate+4*std_rate, 100)
        plt.plot(x, stats.norm.pdf(x, avg_rate, std_rate))
        plt.xlabel('% return')
        plt.title('Player ROI on playing ' + str(num_hands)+ ' Hands (' + strategy.__name__ + ').' +'\n' + '(Mean=' + str(avg_rate) + '%, STD=' + str(std_rate) + '%)')
        plt.show()
    return final_tuple
        


def run_all_simulations(strategies):
    """
    Runs a simulation for each strategy in strategies and generates a single graph with normal 
    distribution plot for each strategy. No need to graph the underlying histogram. Each guassian 
    (another name for normal) distribution should reflect the distribution of rates of return 
    for each strategy.

    You might find scipy.stats (imported as stats) helpful.

    You might find matplotlib.pyplot (imported as plt) helpful.

    Make sure to label each plot with the name of the strategy and the x axis label.

    Parameters:

        strategies - list of strategies to simulate
    """
    for strategy in strategies:
        answer_tuple=run_simulation(strategy, init_bet=2.0, num_decks=8, num_hands=20, num_trials=100, show_plot=False)
        avg_rate=answer_tuple[1]
        std_rate=answer_tuple[2]
        x=np.linspace(avg_rate-4*std_rate, avg_rate+4*std_rate, 100)
        plt.plot(x, stats.norm.pdf(x, avg_rate, std_rate), label=strategy.__name__)
        plt.xlabel('% return')
        plt.title('Player ROI for Different Strategies')
    plt.legend(loc='upper left')
    plt.show()
if __name__ == '__main__':
    #
    # You can uncomment pieces of the following to test each strategy separately.
    #
    # Default plots:
    #
   #run_simulation(BlackJackHand.copy_dealer_strategy, show_plot=True)
    #run_simulation(BlackJackHand.cheating_strategy, show_plot=True)
#    run_simulation(BlackJackHand.basic_strategy, show_plot=True)
#    run_simulation(BlackJackHand.double_stand_strategy, show_plot=True)
#
    # Uncomment to run all simulations:
#
    run_all_simulations([BlackJackHand.copy_dealer_strategy,
                        BlackJackHand.cheating_strategy,
                        BlackJackHand.basic_strategy,
                        BlackJackHand.double_stand_strategy])
  
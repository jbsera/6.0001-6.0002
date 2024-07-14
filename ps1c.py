## 6.0001 Pset 1: Part c
## Name: Joy Bhattacharya
## Time Spent: 2 hours
## Collaborators:Hermon Kaysha (pset buddy)

#############################################
## Get user input for starting_amount below ##
#############################################
starting_amount=float(input("What is the initial amount in your savings account:"))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
house_cost=750000
down_payment_percent=0.25
down_payment=house_cost*down_payment_percent
years=3
number_months=years*12
low=0
high=1
epislon=100
r=(high + low)/2.0
steps = 0
########################################################################################################
## Determine the lowest return on investment needed to get the down payment for your dream home below ##
########################################################################################################
if down_payment>starting_amount*((1+(1/12))**36): #If r is maximized to a value of 1 so that savings are maximized and the total savings are still less than the down payment, then it's impossible to reach the down payment in 3 years and r=None
    r=None
    steps = 0
elif down_payment-starting_amount<=100: #If the initial starting amount is within $100 less (inclusive) than the down_payment, then your initial r is 0
    r=0.0
    steps = 0
elif starting_amount>=down_payment: #If the intial starting amount is greater than or equal to the down_payment, then your r=0
    r=0.0
    steps = 0
else: 
    while abs((down_payment-starting_amount*((1+r/12)**number_months))) >= epislon: #While the difference in our down_payment and savings is greater than 100, our epsilon
        if starting_amount*((1+r/12)**number_months )< down_payment: #If our savings are less than our downpayment by more than epsilon, then we reset our interval so that our low bound=r 
            low = r
        else: #If our savings exceed our downpayment by more than epsilon, then we reset our interval so that our high bound=r 
            high = r
        r = (high + low)/2.0   #Redefine r as the average of our new low and high bounds
        steps +=1 #Increment the steps each time the program goes through the loop
             
        
    
##########################################################
## Print out the best savings rate and steps taken here ##
##########################################################
print('Best savings rate: ',r)
print('Steps in bisection search: ',steps)

## 6.0001 Pset 1: Part b
## Name:Joy Bhattacharya
## Time Spent: 10 minutes
## Collaborators:Hermon Kaysha (pset buddy)

#######################################################################################
## Get user input for salary, savings_percent, total_cost and raise_percentage below ##
#######################################################################################
salary=float(input("What is your starting yearly salary:"))
savings_percent=float(input("What percent of your salary will you save?"))
total_cost=float(input("What is the cost of your dream home?"))
raise_percentage=float(input("What is your semi-annual salary raise?"))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
percent_down_payment=0.15
down_payment=float(percent_down_payment*total_cost)
amount_saved=0
months=0
r=0.05
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
while amount_saved<=down_payment: #Perform this loop until your amount saved is less than or equal to the cost of the down payment
    final_amount_saved=((savings_percent)*(salary/12))+((r/12)*amount_saved) #Find the compounded interest from the amount saved at the beginning of the month and add that total to your monthly interest 
    total_amount_saved=final_amount_saved+amount_saved #Take the value calculated in line 25 and add that to your amount saved
    amount_saved=total_amount_saved #Redefine your total amount saved as the value calculated in line 26 so that when the loop continues, it continues with amount saved redefined as this new value 
    months+=1 #Everytime the loop runs, increment months by +1
    if months%6==0: #Every 6 months, increase salary by raise percentage
        salary=salary+(salary*raise_percentage)
    else:#When the month is not the month where you receive a raise, keep your salary as salary without a raise percentage
        salary=salary

#######################################################
## Print out the number of months it would take here ##
#######################################################
print(months)

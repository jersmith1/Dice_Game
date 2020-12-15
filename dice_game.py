#Jeremy Smith - ID# 260948914
import random
#allows me access to any function within the random module

def can_play(money_available, desired_bet):
    """(float, float) -> bool
    Returns true if the desired bet is non-negative and doesnt exceed the available money
    >>>can_play(55.50, 80.90)
    False
    >>>can_play(100.00, 75.45)
    True
    >>>can_play(70.90, -64.90)
    False
    """
    #the two inputs are defined in the play() fcn
    if (money_available>=desired_bet) and (desired_bet>0.0):
        #allows all non negative bets that dont exceed the amount of money that the user has to be true
        return True
    else:
        #takes into account both negative bets and bets of a greater amount than the available money to a user
        return False

def dice_roll():
    """no input but returns an integer between 2 and 12
    Rolls two dice and returns the sum of the faces that each di landed on
    >>>random.seed(78)
    >>>dice_roll()
    3
    >>>dice_roll()
    9
    >>>dice_roll()
    9
    >>>random.seed(0)
    >>>dice_roll()
    8
    >>>dice_roll()
    4
    >>>dice_roll()
    9
    >>>random.seed(-1)
    >>>dice_roll()
    7
    >>>dice_roll()
    4
    >>>dice_roll()
    5
    """
    first_roll = random.randint(1,6)
    #takes a random integer from 1 to 6 both included as the result of the first roll
    second_roll = random.randint(1,6)
    #see last comment but for the second di
    point = first_roll + second_roll
    #adds the two rolls will be between 2 and 12 as the lowest possible results are 1 and 1 and the highest are 12 and 12
    #the sum of the two rolls 'point' is what is returned by the dice roll function
    return point

def second_stage(point):
    """
    (int)->int (point) or int (7)
    Re-rolls the dice until the result is either a 7 or the point from the initial roll
    >>>r = second_stage(9)
    8 7
    >>>r
    7
    >>>r = second_stage(4)
    2 6 8 8 11 7
    >>>r
    7
    >>>r = second_stage(5)
    4 5
    >>>r
    5
    """
    while(True):
        #essentially an infinite loop so that the dice will be rolled over and over again until the while loop is broken
        x = dice_roll()
        #saves the result of that dice roll
        print(x, end = ' ')
        #keeps printing the dice roll and ensures that it will all be printed on the same line
        if (x == 7 or x == point):
            #ends the while loop when the result of the roll is either the point from the come out roll or is a 7
            break
    if (x == 7):
        #the second stage function will return the value of the final roll that determines whether or not the user won the game either a 7 or the initial point will be returned
        return 7
    if (x == point):
        return point
        
def pass_line_bet(money_available, desired_bet):
    """(float, float) -> float
    Takes 2 floats 1st being the amount of money the user has available to them and the 2nd being their desired bet.
    The dice are rolled and depending on the result the user will win, lose or move on.
    The amount of money remaining after the result is determined is returned as a float
    >>>random.seed(7)
    >>>m = pass_line_bet(100.67, 20.55)
    A  5  was rolled. Moving on to next stage
    10 2 6 8 6 3 5 
    A  5  was rolled again. You win!
    >>>m
    121.22
    >>>random.seed(14)
    >>>m = pass_line_bet(3, 1)
    A  6  was rolled. Moving on to next stage
    12 7 
    A 7 was rolled. You lose.
    >>>m
    2
    >>>random.seed(1)
    >>>m = pass_line_bet(34,22)
    A 7 was rolled. You win!
    >>>m
    56
    """
    point = dice_roll()
    #saves the result of the first roll as 'point'
    if (point == 7 or point == 11):
        #when winning scenarios are rolled
        print("A ",point," was rolled. You win!")
        m = money_available + desired_bet
        round(m,2)
        #had an error when inputs were 67.89 and 43.4 that returned an m with more than 2 decimal point so I am rounding the reult as well as the inputs
        #calculates how much money the user has after winning the same is done under the following scenario for a loss
    elif (point == 2 or point == 3 or point == 12):
        print("A ",point," was rolled. You lose.")
        m = money_available - desired_bet
        round(m,2)
    else:
        print("A ",point," was rolled. Roll again")
        r = second_stage(point)
        #saves the result from the second stage as r and calls on the second stage to run using the point as input
        if (r == 7):
            #shows what happens when the second stage spits out a 7 and what happens to the amount of money remaining for the user the following statement shows what happens when the second dtage returns the point
            print ("\nA 7 was rolled. You lose.")
            m = money_available - desired_bet
            round(m,2)
        elif (r == point):
            print ("\nA ", point," was rolled again. You win!")
            m = money_available + desired_bet
            round(m,2)
    return m
        
def play():
    #the main function that is being run to play the dice game
    money_available=round(float(input("Please enter the amount of money you have here: ")),2)
    #takes input from the user converts it into a float that is rounded to 2 decimal points
    desired_bet=round(float(input("How much would you like to bet?: ")),2)
    #takes input from the user converts it into a float that is rounded to 2 decimal points
    c = can_play(money_available, desired_bet)
    #calls on the can_play function to verify that the user's bet is non-negative and does not exceed the amount of money available to the user
    if (c == True):
        m = pass_line_bet(money_available, desired_bet)
        print("You now have $",m," available")
    else:
        #in order to make sure the game doesnt run when the user cant play
        print("Insufficient funds. You cannot play.")

play()
#calls on the play function may have to remove this when uploading to code post or just throw a # in front of play()
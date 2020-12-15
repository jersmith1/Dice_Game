# Dice_Game
McGill Comp202 Assignment 2

Question 1: Craps (40 points)
Craps is a dice game where each player bets on the outcome of the dice rolls. The goal of this question is to write several functions in order to create a program that simulates the outcome of a Pass Line Bet (see below) in a game of Craps. All the code for this question must be placed in a file named dice game.py.
The Pass Line Bet
Craps is a game of rounds. The first dice roll of a round is called the Come-out Roll. When a player is making a Pass Line Bet, they will place a bet before the Come-Out Roll. Depending on the result of the roll, the player might win, lose, or go to the “next stage” of the game:
• If a 7 or an 11 is rolled, then the player wins.
• If a 2, 3, or 12 is rolled, then the player loses.
• If any other number is rolled, the player must go to the next stage.
For the next stage, it is important to remember which number was rolled in the Come-Out Roll, this number is called the point. In the second stage, the player will keep rolling the dice unless one of the following happens:
• A 7 is rolled, and the player loses the bet
• The point is rolled again, and the player wins the bet
 Page 4
The payout is 1:1: the players win as much as they bet. Thus, if the player bets $5 and wins they receive an additional $5. If they lose, they lose the entire bet.
Let’s see a couple of examples:
• The result of the Come-Out Roll is a 3. → The player loses!
• The result of the Come-Out Roll is a 5 → The dice are rolled again until either a 7 or a 5 is rolled. Supposed that the results of the rolls are the following: 10, 11, 4, 7. → The player loses!
• The result of the Come-Out Roll is a 9 → The dice are rolled again until either a 7 or a 9 is rolled. Let the results of the rolls be as follow: 3, 5, 9. → The player wins!
Now that we now how the game works, let’s see which functions we need to simulate the result of a Pass Line bet in a game of Craps. Because this program simulates a game of dice, you will need to generate random numbers. To achieve this, make sure to import random at the top of your file.
For full marks, all the following functions must be part of your program:
• dice_roll: In a game of Craps, players are betting on the outcome of a roll of two six-sided dice. Write a function called dice_roll that simulates the roll of two six-sided dice. Such function takes no input and returns an integer between 2 and 12 (included), which is the sum of the result of rolling two six-sided dice. Notice, that to simulate the roll of two six-sided dice, you will have to generate two random numbers between 1 and 6 (both included) and sum the results together. If you have any doubts on how to achieve this, review the slide from lecture 7. To be able to test the correctness of your function, we suggest you to fix a seed while testing the function. Do NOT use random.seed from within the function dice roll. Once you have created the function, if you test if from the shell you should see the following:
    >>> random.seed(5)
    >>> dice_roll()
    8
    >>> dice_roll()
    9
    >>> random.seed(2)
    >>> dice_roll()
    2
    >>> dice_roll()
    4
• second_stage: This function simulates the second stage of the Pass Line Bet. It takes as input one integer value that corresponds to the point, the number rolled in the Come-Out Roll (either 4, 5, 6, 8, 9, or 10), and returns an integer which will either be a 7 or the point itself depending on which one gets rolled first. The function should also print (on the same line!) the result of all the dice rolls carried out before either a 7 or the point is rolled. For example,
    >>> random.seed(5)
    >>> r = second_stage(6)
    8 9 12 11 5 8 3 4 6
    >>> r
    6
    >>> random.seed(789)
    >>> r = second_stage(8)
    10 7
    >>> r
    7
Make sure to use dice roll to obtain the value of each roll.
  Page 5

• can_play: This function takes two floats as input and returns a boolean value. The first input value corresponds to the money the player has, the second corresponds to how much money the player would like to bet. A player is allowed to play only if they bet more than $ 0.0, but not more than what they own. If the player is allowed to play, the function returns True, otherwise it returns False. For example,
  >>> can_play(5.25, 5.0)
  True
  >>> can_play(0.0, 2.0)
  False
  >>> can_play(5.0, -3.0)
  False
• pass_line_bet: This function simulates what happens when a Pass Line Bet is placed. It takes two floats as input: the first one corresponds the total amount of money the player has, the second correspond to how much money the player decides to bet. You can assume that the given values are such that the player can play (see previous function). The function returns a float which corresponds to the amount of money the player has left after one round of Craps.
The function should display the result of the Come-Out Roll (the first roll in a round of Craps) as well as what will happen next. Recall that the player wins with a 7 or 11, loses with a 2, 3, or 12, and moves to the second stage with any other number. Here are three possible statements that the function might display after the Come-Out Roll:
  A 7 has been rolled. You win!
  A 12 has been rolled. You lose!
  A 5 has been rolled. Roll again!
If necessary, the function should simulate the second stage in order to determine whether the player wins or loses. If at the end of the second stage a 7 was rolled the function displays a statement informing the player they lost, if instead the point was rolled the function displays a statement informing the player they won.
For full marks, you should use second stage, and dice roll in order to implement the simulation of a Pass Line Bet. Remember to return the amount of money the player has left depending on whether they won or lost the bet. For example,
  >>> random.seed(5)
  >>> m = pass_line_bet(12.5, 3.5)
  A 8 has been rolled. Roll again!
  9 12 11 5 8
  You win!
  >>> m
  16.0
  >>> random.seed(789)
  >>> m = pass_line_bet(12.5, 3.5)
  A 10 has been rolled. Roll again!
  7
  You lose
  >>> m
  9.0
  >>> random.seed(3)
  >>> m = pass_line_bet(5.0, 5.0)
  A 7 has been rolled. You win!
  >>> m
  10.0
  Page 6

• play: This function takes no input and returns no value. The function retrieves two inputs from the user. The first input corresponds to the money the player has, the second to the money they would like to bet. If the user does not have enough money to play, the function displays a message informing the user about it and terminates. Otherwise, the function calls pass line bet with the appropriate inputs in order to place the bet. At the end, make sure to display a statement informing the player about how much money they have left after their bet. The number representing the money left should not have more than 2 decimals.
For example,
  >>> play()
  Please enter your money here: 3.0
  How much would you like to bet? 5.0
  Insufficient funds. You cannot play.
  >>> random.seed(5)
  >>> play()
  Please enter your money here: 12.5
  How much would you like to bet? 3.5
  A 8 has been rolled. Roll again!
  9 12 11 5 8
  You win!
  You now have $16.0
  >>> random.seed(789)
  >>> play()
  Please enter your money here: 12.5
  How much would you like to bet? 3.5
  A 10 has been rolled. Roll again!
  7
  You lose
  You now have $9.0
  >>> random.seed(3)
  >>> play()
  Please enter your money here: 12.5
  How much would you like to bet? 3.5
  A 7 has been rolled. You win!
  You now have $16.0
  Page 7

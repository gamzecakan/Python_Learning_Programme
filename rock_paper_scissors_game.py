#Collect all the components of your program to run it in a while loop
#Import the random library
import random

#Add the code to create a list containing the three actions of the game.
actions=["rock", "paper", "scissors"]

#Add the code to set the scores of players to 0
player1_score=0
player2_score=0
#Add a round_counter that is 0 at the beginning
round_counter=0

#Add the code to ask the user how many rounds they want to play
round=int(input("How many rounds do you want to play? "))

#Write a while loop and put the game inside
while round_counter < round:

  #increase round_counter by 1 and print it
    round_counter += 1

  #Add the code to select a random action for each player
    player1=random.choice(actions)
    player2=random.choice(actions)

  #Add the code to print the players choices
    print("Player 1 chose: ",player1)
    print("Player 2 chose: ",player2)

  #Add the tie condition
    if player1==player2:
      print("Tie! Both players chose the same action.")

  #Add the remaining condition
    elif    (player1 == 'rock' and player2 == 'scissors') or \
            (player1 == 'paper' and player2 == 'rock') or \
            (player1 == 'scissors' and player2 == 'paper'):
            print("Player 1 wins this round!")
            player1_score += 1
    else:
        print("Player 2 wins this round!")
        player2_score += 1


  #print the score
    print("\nScore:")
    print("Player 1:", player1_score)
    print("Player 2:", player2_score)


  #stop the while loop if the round_counter equals the number of total rounds
    if round_counter==round:
      break
#Print the outcome of the game by using conditional statements
print("\nFinal Score")
if player1_score > player2_score:
    print("Player 1 wins the game!")
elif player1_score < player2_score:
    print("Player 2 wins the game!")
else:
    print("The game ended in a tie!")

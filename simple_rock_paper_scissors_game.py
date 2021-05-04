# generate a rock, paper scissors game

#rules 2 player game where rock > scissors; scissors > paper; paper > rock

player1 = (input("Welcome to the game of Rock, Paper and Scissors. Player 1 please enter your choice: "))
player2 = (input("Play 2 please enter your choice: "))


if player1 == "rock" and player2 == "scissors":
    print("Player one wins")
elif player1 == "scissors" and player2 == "paper":
    print("player one wins")
elif player1 == "paper" and player2 == "rock":
    print("player one wins")
elif player1 == "scissors" and player2 == "rock":
    print("Player two wins")
elif player1 == "paper" and player2 == "scissors":
    print("Player two wins")
elif player1 == "rock" and player2 == "paper":
    print("Player two wins")
else:
    print("Invalid option")
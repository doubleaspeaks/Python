# A rock, paper and scissors game!
import random
while True:
    user_action = input("Enter a choice rock, paper or scissors: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_actions = random.choice(possible_actions)

    print(f"You chose {user_action} , computer chose {computer_actions} .\n")

    #Tie
    if user_action == computer_actions:
        print(f"Both players selected {user_action} . Its a tie")

    elif user_action == "rock":
        if computer_actions == "scissors":
            print("Rock smashed scissors! You Win :) !!")
        else:
            print("Paper covers rock...You Lose...:( ")
    #user selects paper
    elif user_action == "Paper":
        if computer_actions == "scissors":
            print("Paper covers rock! You Win :) !!")
        else:
            print("Scissors cuts paper...You Lose...:( ")

    # user selects paper
    elif user_action == "scissors":
     if computer_actions == "paper":
        print("Scissors cut paper! You Win :) !!")
    else:
        print("Rock smashes scissors...You Lose...:( ")

    play_again = input("Play again (y/n) : ")
    if play_again.lower() != "y":
        exit()

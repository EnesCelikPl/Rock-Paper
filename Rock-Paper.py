import random

def get_choice():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]

    if player_choice not in options:
        print("Invalid choice, please choose rock, paper, or scissors.")
        return get_choice()  # Ask again if input is incorrect

    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    if player == computer:
        return "It's a tie!"

    elif player == "rock":
        if computer == "scissors":
            return "You win!"
        else:
            return "You lose!"
    elif player == "paper":
        if computer == "rock":
            return "You win!"
        else:
            return "You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "You win!"
        else:
            return("You lose!")



#Play Again
while True:
    choices = get_choice()
    print(f"You chose {choices['player']}, computer chose {choices['computer']}.")
    result = check_win(choices["player"], choices["computer"])
    print(result)

    next_game = input("Do you want to play again? (yes/no): ").lower()
    if next_game != "yes":
        print("Goodbye!")
        break





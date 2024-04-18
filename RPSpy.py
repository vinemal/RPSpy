import random
def play():
    # List containing the options

    choices= ['rock','papar','seissors']

    # Keeps running till the user doesnt want to play again

    while True:
        print("\nRock, Paper, Seissors")
        print("Enter your choice: (rock, paper, scissors)");
        player_choice = input().lower()

        if player_choice not in choices:
            print("Invalid choice! Please choose again.")
            continue

        # Use random to päck for the computer
        computer_choice = random.choice(choices)
        print(f"\nyou : {player_choice}.")
        print(f"Computer : {computer_choice}.\n")

        #Print the winner
        print(winner(player_choice, computer_choice))

        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != "y":
            print ("Thanks for playing!\n")
            break

# Function to determine the winner
def winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "Its a tie"
    # Checks all the possible combinations for the user winning
    elif (user_choice == 'rock' and computer_choice== 'scissors' or
         user_choice == 'paper' and computer_choice == 'rock' or
         user_choice == 'scissors' and computer_choice == 'paper'):
         return "You win!!!"
    else:
        return "Computer win!!!"


if __name__ == "__main__":
    play()

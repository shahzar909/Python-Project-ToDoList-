import random

def play_game():
    user_choice = int(input("Enter your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
    if user_choice < 0 or user_choice > 2:
        print("Invalid Choice, You Lose... Try Again!!")
    else:
        computer_choice = random.randint(0, 2)
        print("Computer Chose:", computer_choice)
        
        if computer_choice == user_choice:
            print("It's a Draw.")
        elif computer_choice == 0 and user_choice == 2:
            print("You Lose.")
        elif user_choice == 0 and computer_choice == 2:
            print("You Win.")
        elif computer_choice > user_choice:
            print("You Lose.")
        elif user_choice > computer_choice:
            print("You Win.")

if __name__ == "__main__":
    while True:
        play_game()
        continue_choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            print("Goodbye!")
            break




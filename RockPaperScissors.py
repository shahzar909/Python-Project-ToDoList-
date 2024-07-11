import random

user_score = 0
computer_score = 0

while True:
    user_choice = int(input("Enter your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
    
    if user_choice < 0 or user_choice >= 3:
        print("Invalid Choice, You Lose... Try Again!!")
    else:
        computer_choice = random.randint(0, 2)
        print(f"Computer Chose: {computer_choice}")

        if computer_choice == user_choice:
            print("It's a Draw.")
        elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
            print("You Lose.")
            computer_score += 1
        else:
            print("You Win.")
            user_score += 1

        print(f"Current Scores - You: {user_score}, Computer: {computer_score}")

    continue_choice = input("\nDo you want to play another round? (yes/no): ").strip().lower()
    if continue_choice != "yes":
        print("Final Scores - You: {user_score}, Computer: {computer_score}")
        print("Goodbye!")
        break

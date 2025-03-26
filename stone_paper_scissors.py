import random

choice_list = ['stone', 'paper', 'scissors']

while True:
    user_choice = input("Enter 'stone', 'paper' or 'scissors': (Enter 'q' to exit): ").lower()
    if user_choice == 'q':
        break
    
    random_number = random.randint(0, 2)
    computer_choice = choice_list[random_number]
    print(f"You chose: {user_choice}.")
    print(f"Computer chose: {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie.")

    elif user_choice == 'stone' and computer_choice == 'scissors':
        print("You win.")

    elif user_choice == 'paper' and computer_choice == 'stone':
        print("You win.")

    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You win.")

    else:
        print("You lose.")

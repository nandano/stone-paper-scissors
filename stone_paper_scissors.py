import random

stone = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice_list = [stone, paper, scissors]
user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter 0 for 'stone', 1 for 'paper' or 2 for 'scissors' (Enter 'q' to exit): ")
    if user_choice == 'q':
        print(f"Your Score: {user_score}.")
        print(f"Computer Score: {computer_score}.")
        print("Have a nice day!")
        break
    
    user_choice = int(user_choice)
    computer_choice = random.randint(0, 2)
    print(f"You chose:\n{choice_list[user_choice]}.")
    print(f"Computer chose:\n{choice_list[computer_choice]}.")

    if user_choice == computer_choice:
        print("It's a tie.")

    elif user_choice == 0 and computer_choice == 2:
        print("You win.")
        user_score += 1

    elif user_choice == 1 and computer_choice == 0:
        print("You win.")
        user_score += 1

    elif user_choice == 2 and computer_choice == 1:
        print("You win.")
        user_score += 1

    else:
        print("You lose.")
        computer_score += 1

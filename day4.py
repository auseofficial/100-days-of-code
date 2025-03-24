# import random
#
# # random_integer=random.randint(1,10)
# # print(random_integer)
#
# # random_float=random.uniform(1,10)
# # print(random_float)
#
# friends=["Eshan","Hasan","Maruf","Arpita","Esrat"]
# print(random.choice(friends))


# rock_paper_scissor

import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of images
game_images = [rock, paper, scissors]

# User Input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Ensure valid input
if user_choice >= 3 or user_choice < 0:
    print("Invalid choice! You lose.")
else:
    print("You chose:")
    print(game_images[user_choice])

    # Computer Choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Game Logic
    if user_choice == computer_choice:
        print("It's a draw! 🤝")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (
            user_choice == 2 and computer_choice == 1):
        print("You win! 🎉")
    else:
        print("You lose! 😢")

import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissor]

user_choice = int(input("Write what you choose? O for Rock, 1 for Paper and 2 for Scissor"))

if user_choice >=3 or user_choice <0:
    print("Invalid choice! You lose. ")
else:
    print("Choose please:")
    print(game_images[user_choice])

    computer_choice=random.randint(0,2)
    print("Computer chose: ")


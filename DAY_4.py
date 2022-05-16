# DAY 4

# Head and tails

import random

head_tails = random.randint(1,2)

if head_tails == 1:
  print("Its head")
else:
  print("Its Tail")
  
# Spliting Bills

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

pay_bills = random.randint(0,len(names) -1)
print (f"{names[pay_bills]} is going to buy the meal today!" )


# Place your treasure

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vartical = int(position[1])

print(horizontal)
print(vartical)

#selected_row = map[vartical - 1]
#selected_row [horizontal -1] = "X"

map[vartical - 1][horizontal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# Rock, Paper, Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper,scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input > 2 or user_input < 0:
  print("You have enter wrong number. Game over!")
elif user_input >= 0 or user_input < 3:
  print(game_image[user_input])
  
  comp_random = random.randint(0,2)  
  print("Computer Choose:")
  print(game_image[comp_random])
  
  if user_input == 0 and comp_random == 2:
    print("You win!")
  elif comp_random == 0 and user_input == 2:
    print("You lose!")
  elif comp_random > user_input:
    print("You lose!")
  elif user_input > comp_random:
    print("You win!")
  elif user_input == comp_random:
    print("It's a draw!")
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

# Write your code below this line 👇
import random

rps = [rock, paper, scissors]
c_rps = len(rps)
r_rps = random.randint(0, c_rps - 1)

user = input("type: 'rock', 'paper' or 'scissors'\n")

if user == 'rock':
    print(rps[0])
    ai = print(f"{rps[r_rps]}")

    if r_rps == 0:
        print("It's a tie!")
    elif r_rps == 1:
        print("Paper wins!")
    elif r_rps == 0:
        print("Rock wins!")
elif user == 'paper':
    print(rps[1])
    ai = print(f"{rps[r_rps]}")

    if r_rps == 1:
        print("It's a tie!")
    elif r_rps == 2:
        print("Scissors wins!")
    elif r_rps == 0:
        print("Paper wins!")
elif user == 'scissors':
    print(rps[2])
    ai = print(f"{rps[r_rps]}")

    if r_rps == 2:
        print("It's a tie!")
    elif r_rps == 1:
        print("Scissors wins!")
    elif r_rps == 0:
        print("Rock wins!")
else:
    print("Did you type any of the following: 'rock', 'paper' or 'scissors'?")

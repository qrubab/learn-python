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
items=[rock, paper, scissors]
print("Welcome to the Rock paper scissors game.")
user_choice=int(input("Type 0 for Rock. 1 for Paper and 2 for Scissors."))
comp_choice=random.randint(0,2)

print(f"You chose{items[user_choice]}")
print(f"Computer chose {items[comp_choice]}")

if user_choice==comp_choice:
    print("Its a tie.")
elif user_choice==0 and comp_choice==2:
    print("You won.")
elif user_choice==1 and comp_choice==0:
    print("You won.")
elif user_choice==2 and comp_choice==1:
    print("You won.")
else:
    print("Computer won.")

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
game = [rock, paper, scissors]
user = int(input("Choose a number - 0,1,2"))
if user >=0 and user <= 2 :
    print(game[user])
computer = random.randint(0,2)
print(f"Computer chose {computer}")
print(game[computer])

if computer == user:
    print("Draw")
elif computer == 0 and user == 2:
    print("You Lose")
elif user == 0 and computer == 2:
    print("You Win")
elif computer > user:
    print("You Lose")
elif computer < user:
    print("You Win")
else:
    print("Please choose a valid number and Play again!")
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

winner = '''
             __   __         __      ___      
             \ \ / ___ _  _  \ \    / (_)_ _  
              \ V / _ | || |  \ \/\/ /| | ' \ 
               |_|\___/\_,_|   \_/\_/ |_|_||_|
 '''

loser = '''
             __   __          _               
             \ \ / ___ _  _  | |   ___ ______ 
              \ V / _ | || | | |__/ _ (_-/ -_)
               |_|\___/\_,_| |____\___/__\___|
 '''

draw = '''
                  ___                  
                 |   \ _ _ __ ___ __ __
                 | |) | '_/ _` \ V  V /
                 |___/|_| \__,_|\_/\_/ 
'''

choices = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(choices[player])

print("Computer chose:")

computer = random.randint(0, 2)
print(choices[computer])

if(player == computer):
    print(draw)
elif ((player - computer) != -1 and (player - computer) < 2):
    print(winner)
else:
    print(loser)

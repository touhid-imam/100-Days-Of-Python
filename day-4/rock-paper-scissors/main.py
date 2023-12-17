import random

rock = '''                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                             '''

paper = '''                             
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''

scissors = '''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
                                   
'''

game_images = [rock, paper, scissors]

user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n=> "))

if user_choice >= 3 or user_choice < 0:
    print("You types invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer Choice: ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif computer_choice == user_choice:
        print("It's a draw")

# create game for guess numbers .abs

import argparse
import sys
import random

# 1 : the command line arguments .
game_parser = argparse.ArgumentParser(
    description="guessing game ==> start playing ."
)

game_parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="Please Enter Your Name To Start."
)

args = game_parser.parse_args()
# 2 : input and While and condition with random and # 
# sys and printing the messages  .

count_game = 0
player_score = 0
computer_score = 0
limit_palying  = True

while limit_palying:
    count_game += 1
    guessing = input(f"\nhi {args.name} Guess The Star Number 1|2|3: ")

    int_guessing = int(guessing)
    rdm = random.choice("123")
    int_rdm = int(rdm)

    if int_guessing < 1 or int_guessing > 3:
       print(f"\n\n{args.name} Please Stay in 1|2|3\n")
       continue
    
    print(f"\n{args.name} You Chose "+ guessing)
    print(f"\n{args.name} I Was Thinking About "+ rdm)
    if int_guessing == int_rdm:
        print(f"\n{args.name} You Win !")
        player_score += 1
    else:
        print(f"\n{args.name} You Lose !")
        computer_score += 1
    
    print("\nGame Number :"+ str(count_game))
    print(f"\n{args.name} You Win "+ str(player_score)+" Time")
    print(f"\nAnd Computer Win "+ str(computer_score)+" Time")

    if player_score / count_game == 0:
        print(f"\n\nYou Lose {args.name}.")
        sys.exit(f"\n\nThe Game Its Over {args.name} .")
    else:
        print(f"\nPoint : {player_score/count_game:.2%} .")

    print(f"\nAre You Want To Play Again {args.name}? Enter Y If Note Enter Q !")
    end_game = input("\nY OR Q : ")

    if end_game.upper() == "Y":
        continue
    elif end_game.upper() == "Q":
        limit_palying = False
sys.exit(f"\n\nBy {args.name} !")


    





    

    



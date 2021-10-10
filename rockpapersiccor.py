import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cont = "y"

def play():
    users = input(" What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n ")
    computer = random.choice(['r','p','s'])

    if users == computer:
       return 'tie'

    # r > s, s > p, p < r
    if is_win(users, computer):
        return 'You won!'        

    return 'You lost!'

def is_win(player, opponent):
# return true if player wins
# r > s, s > p, p < r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())
# Import
import cmd
import time
import os
import sys
import textwrap
import random

screen_width = 100

class player():
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effect = []
        self.inventory = []

myPlayer = player()

# -------TITLE SCREEN---------
def title_screen_choose():
    Pcmd = input('>> ')
    if Pcmd.lower() == ('main'):
        start_game()
    elif Pcmd.lower() == ('tutorial'):
        help_game()
    elif Pcmd.lower() == ('keluar'):
        sys.exit()
    while Pcmd.lower() not in ['main','tutorial','keluar']:
        Print('Gunakan perintah yang benar! Coba lagi.')
        Pcmd = input('>> ')
        if Pcmd.lower() == ('main'):
            start_game()
        elif Pcmd.lower() == ('tutorial'):
            help_game()
        elif Pcmd.lower() == ('keluar'):
            sys.exit()







# while True:
#     get_Pname = str(input('Who are you? '))
#     if get_Pname.isdigit():
#         print('''Can't use number as a name! Try again.''')
#         continue
#     else:
#         break

# get_Pname = get_Pname.capitalize()
# player_data.update({'name': get_Pname})
# os.system('cls')
# print(f'''Welcome to game, {player_data['name']}!

# >> This game is set in a village called OldKeep. You live in peace and quiet. Until that night,
# Dreadsword's body was found in the middle of a farmer's field.Dreadsword is a cunning and-
# ferocious monster. Dreadswords are usually found along beaches and in the middle of forests.
# However, it seems that the explorers from the village informed that the monster came from a-
# dark and scary Dungeon. You are assigned by the OldKeeper Leader to eradicate the monsters in-
# The Dungoen so that they no longer disturb the peace of the villagers of OldKeep.
# ''')
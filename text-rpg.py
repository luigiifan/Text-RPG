import random
from os import system

player_health = 100
# Monster Database
commonEnemy_Type1 = [
    {
        'name': 'Ghoul',
        'level': 3,
        'hp': 82,
        'counter': 'Fast',
        'damage': random.randint(8,28),
        'is_Boss': False,
    },
]

player_data = {
        'name': 'Guest',
        'skill': None,
        'level': 1,
        'hp': 100,
        'weapon': 'Sword',
        'armor': None,
        'monster_kill': 0,
        'inventory': None,
        'is_Mastery': False,
        'is_Hardcore': False
}

while True:
    get_Pname = str(input('Who are you? '))
    if get_Pname.isdigit():
        print('''Can't use number as a name! Try again.''')
        continue
    else:
        break

get_Pname = get_Pname.capitalize()
player_data.update({'name': get_Pname})
welcome_text = f'''Welcome to the game, {player_data['name']}!'''
print(welcome_text)

# ghoul_damage = commonEnemy_Type1[0]['damage']
# print(f'Ghoul memberikan damage: -{ghoul_damage}')
# playerhealth_now = player_health - ghoul_damage
# print(f'Hp-mu sekarang: {playerhealth_now}')
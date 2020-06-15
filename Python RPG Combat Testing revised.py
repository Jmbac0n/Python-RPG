import random

player_health = 10
player_attack = 5

monster_health = 10
monster_attack = 2

def player_turn():
    global player_attack
    global monster_health

    print("""\

        Player action - what will you do?

        1. Attack

        """)

    player_input = input()

    if player_input == ("1"):
        p_atk = random.randint(1, player_attack)
        monster_health = monster_health - p_atk
        print("""\
        
        Attacking Monster - Hit for %s Damage
        Monster HP: %s
        ____________________________

        """ % (str(p_atk), (monster_health)))
        
    
    turn_check_monster()

def monster_turn():
    global monster_attack
    global player_health

    print("""\
        The Monster attacks you

        """)

    m_atk = random.randint(1, monster_attack)
    player_health = player_health - m_atk
    print("""\

        Monster Attacking - Hit for %s Damage
        Player HP: %s
        ___________________________

        """ % (str(m_atk), (player_health)))

    turn_check_player()

def turn_check_player():
    global player_health

    if player_health > 0:
        player_turn()
    elif player_health == 0:
        print("You have been defeated")

def turn_check_monster():
    global monster_health

    if monster_health > 0:
        monster_turn()
    elif monster_health < 1:
        print("You are victorious")
        Stop_input = input() # Only here to stop code for review in terminal

def start_combat():
    turn_check_player()
    
start_combat()   

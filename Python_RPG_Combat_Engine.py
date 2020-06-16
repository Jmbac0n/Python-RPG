import random
import Python_RPG_Combat_Text

player_health = 10
player_attack = 5

monster_health = 10
monster_attack = 2
monster_escape_rating = 50 # Bosses should have an unbeatable rating

# Monster exp - Earned if battle won and added to player total

def player_turn():
    global player_attack
    global monster_health
    global monster_escape_rating

    print(Python_RPG_Combat_Text.player_action_text)

    player_input = input()

    if player_input == ("1"):
        p_atk = random.randint(1, player_attack)
        monster_health = monster_health - p_atk
        print(Python_RPG_Combat_Text.player_attack_text % (str(p_atk), (monster_health)))
    elif player_input == ("2"):
        print(Python_RPG_Combat_Text.player_escape_text)
        escape_roll = random.randint(0, 1)
        if escape_roll > monster_escape_rating:
            print(Python_RPG_Combat_Text.player_escape_success_text)
            stop_input = input() # Escape condition needs to go here that ends combat immediately
        elif escape_roll < monster_escape_rating:
            print(Python_RPG_Combat_Text.player_escape_fail_text)
        
    
    turn_check_monster()

def monster_turn():
    global monster_attack
    global player_health

    print(Python_RPG_Combat_Text.monster_action_text)

    m_atk = random.randint(1, monster_attack)
    player_health = player_health - m_atk
    print(Python_RPG_Combat_Text.monster_attack_text % (str(m_atk), (player_health)))

    turn_check_player()

def turn_check_player():
    global player_health

    if player_health > 0:
        player_turn()
    elif player_health == 0:
        print(Python_RPG_Combat_Text.defeat_text)

def turn_check_monster():
    global monster_health

    if monster_health > 0:
        monster_turn()
    elif monster_health < 1:
        print(Python_RPG_Combat_Text.victory_text)
        Stop_input = input() # Only here to stop code for review in terminal

def start_combat():
    turn_check_player()
    
start_combat()   

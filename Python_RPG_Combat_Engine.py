import sys,time,random
import Python_RPG_Combat_Text
import Python_RPG_Monster_List
import Python_RPG_Combat_Engine

#Global variables
player_health = 10
player_attack = 5 

monster_health = 0

battle_result = False

# Monster exp - Earned if battle won and added to player total

def start_combat(m_name, m_attack, m_e_rating):
    
    def slow_type(t):
        typing_speed = 150 #wpm
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random()*10.0/typing_speed)
        print('')

    def player_turn():
        global player_attack
        global monster_health

        monster_escape_rating = m_e_rating
        monster_name = m_name

        slow_type(Python_RPG_Combat_Text.player_action_text)

        player_input = input()

        if player_input == ("1"):
            p_atk = random.randint(1, player_attack) 
            monster_health = monster_health - p_atk
            slow_type(Python_RPG_Combat_Text.player_attack_text % (str(monster_name), (p_atk), (monster_name), (monster_health))) # Got to here last night - finish changing combat text
        elif player_input == ("2"):
            slow_type(Python_RPG_Combat_Text.player_escape_text)
            escape_roll = random.randint(0, 100)
            if escape_roll > monster_escape_rating:
                slow_type(Python_RPG_Combat_Text.player_escape_success_text)
            elif escape_roll < monster_escape_rating:
                slow_type(Python_RPG_Combat_Text.player_escape_fail_text % (str(monster_name)))
        
        turn_check_monster()

    def monster_turn():
        monster_attack = m_attack
        monster_name = m_name
        global player_health

        slow_type(Python_RPG_Combat_Text.monster_action_text % (str(monster_name)))

        m_atk = random.randint(1, monster_attack)
        player_health = player_health - m_atk
        slow_type(Python_RPG_Combat_Text.monster_attack_text % (str(monster_name), (m_atk), (player_health)))

        turn_check_player()

    def turn_check_player():
        global player_health
        global battle_result
        #global battle_result

        if player_health > 0:
            player_turn()
        elif player_health < 1:
            slow_type(Python_RPG_Combat_Text.defeat_text)
            battle_result = False

    def turn_check_monster():
        global monster_health
        global battle_result

        if monster_health > 0:
            monster_turn()
        elif monster_health < 1:
            slow_type(Python_RPG_Combat_Text.victory_text)
            battle_result = True
            

    turn_check_player()

#TODO

#If player wins the battle, award exp/boost to atk + health plus item move to chapter 2
#If player loses, option to try again
# Escaping yields no rewards

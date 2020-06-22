import sys, time, random
import Python_RPG_Combat_Engine
import Python_RPG_Story_Text
import Python_RPG_Monster_List
import Python_RPG_Player_Sheet
import Python_RPG_Item_List

def slow_type(t, t_speed):
    typing_speed = t_speed
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)

def start_menu():

    slow_type(Python_RPG_Story_Text.title, 1000)

    slow_type(Python_RPG_Story_Text.start_menu, 1000)

    start_input = input()

    if start_input == ("1"):
        chapter_one()

def chapter_one():
    
    from Python_RPG_Monster_List import wolf

    slow_type(Python_RPG_Story_Text.text_block_one, 1000)
    Python_RPG_Combat_Engine.monster_health = wolf['health']
    Python_RPG_Combat_Engine.start_combat(wolf['name'], wolf['attack'], wolf['escape_rating'])
    chapter_two(Python_RPG_Combat_Engine.battle_result)

def chapter_two(b_result):

    from Python_RPG_Monster_List import goblin

    battle_result = b_result

    if battle_result == (True):
        slow_type(Python_RPG_Story_Text.text_block_two, 1000)
        Python_RPG_Player_Sheet.player['health'] = Python_RPG_Player_Sheet.player['health'] + Python_RPG_Item_List.shield['defense']
        Python_RPG_Player_Sheet.player['attack'] = Python_RPG_Player_Sheet.player['attack'] + Python_RPG_Item_List.sword['attack_power']
        Python_RPG_Player_Sheet.show_player_sheet()
        slow_type(Python_RPG_Story_Text.text_block_three, 1000)
        Python_RPG_Combat_Engine.monster_health = goblin['health']
        Python_RPG_Combat_Engine.start_combat(goblin['name'], goblin['attack'], goblin['escape_rating'])
    elif battle_result == (False):
        slow_type(Python_RPG_Story_Text.game_over, 1000)

    

start_menu()

#Known Bugs

#Sometimes - During the combat sequence the code will jump over the player input and allow
#the monster to keep attacking until player is dead.

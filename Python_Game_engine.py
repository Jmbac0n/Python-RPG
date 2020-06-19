import sys, time, random
import Python_RPG_Combat_Engine
import Python_RPG_Story_Text
import Python_RPG_Monster_List

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

def chapter_two():

    slow_type(Python_RPG_Story_Text.text_block_two, 1000)
    slow_type(Python_RPG_Story_Text.text_block_three, 1000)   
    

#start_menu()
chapter_two()

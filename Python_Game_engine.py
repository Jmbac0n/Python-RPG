import sys, time, random
import Python_RPG_Combat_Engine
import Python_RPG_Story_Text

def slow_type(t, t_speed):
    typing_speed = t_speed
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)

def start_menu():

    slow_type(Python_RPG_Story_Text.title, 300)

    slow_type(Python_RPG_Story_Text.start_menu, 100)

    start_input = input()

    if start_input == ("1"):
        chapter_one()

def chapter_one():
    
    slow_type(Python_RPG_Story_Text.text_block_one, 75)
    Python_RPG_Combat_Engine.start_combat()

chapter_one()
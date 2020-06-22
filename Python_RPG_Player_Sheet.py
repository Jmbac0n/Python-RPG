player = {
    'health': 10,
    'attack': 5,
}

def show_player_sheet():
    text = ("""\
        HP: %s
        ATK: %s
        """)

    print(text % (str(player['health']), (player['attack'])))


show_player_sheet()
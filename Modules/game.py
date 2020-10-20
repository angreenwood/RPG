from Modules.Player import player
from Modules.Data import Database
import sys
database = Database()
def prompt():
  if player.is_dead == 'False':
    action = input("> ")
    acceptable_actions = ['go', 'move', 'quit', 'inspect', 'examine', 'look', 'search','score']
  while action.lower() not in acceptable_actions:
    print("Unknown command")
    action = input("> ")
  if action.lower() == 'quit':
    confirmation = input("Are you sure you want to quit?(y or n)\n> ")
    if confirmation == 'yes' or confirmation == 'y':
      player_data = player.get_save_data()
      database.save_character(player_data)
      print("Returning to the real world.")  
      sys.exit()
  elif action.lower() in ['go', 'move']:
    player.move(action.lower())
  elif action.lower() == 'look':
    player.look()
  elif action.lower() == 'score':
    player.score()


def main_game_loop():
  while player.is_dead == 'False':
    prompt()
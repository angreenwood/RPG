from Modules.Player import player
import sys

def prompt():
  if player.is_dead == 'False':
    action = input("> ")
    acceptable_actions = ['go', 'move', 'quit', 'inspect', 'examine', 'look', 'search','score']
  while action.lower() not in acceptable_actions:
    print("Unknown command")
    action = input("> ")
  if action.lower() == 'quit':
    confirmation = input("Are you sure you want to quit?\n> ")
    if confirmation == 'yes' or confirmation == 'y':
      sys.exit()
  elif action.lower() in ['go', 'move']:
    player.move(action.lower())
  elif action.lower() in ['inspect', 'examine', 'look', 'search']:
    player.look()
  elif action.lower() == 'score':
    player.score()

def main_game_loop():
  while player.is_dead == 'False':
    prompt()
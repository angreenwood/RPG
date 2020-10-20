from Modules.Data import *
from Modules.Player import player
from Modules.game import main_game_loop
import os
import sys
os.system('cls')
database = Database()
print('#' * 45)
print('#           Welcome adventurer to           #')
print("#                  Vanheart                 #")

def landing_screen():
  print('#' * 45)
  print("#           .: 1.New Character :.           #")
  print("#              .: 2.Log in :.               #")
  print("#           .: 3.Create Table :.            #")
  print("#               .: 4.Quit :.                #")
  print('#' * 45)

  user_input = input(">:")
  if user_input.lower() == "new character" or user_input.lower() == "new" or user_input.lower() == "1":
    username = input("Username:")
    password = None
    database.create_user(username,password)
    landing_screen()

  elif user_input.lower() == "log in" or user_input.lower() == "log" or user_input.lower() == "2":
    database.validate_user()
    character_id = database.character_id
    player.get_stats(character_id)
    main_game_loop()

  elif user_input.lower() == "create table" or user_input.lower() == "3":
    database.create_table()

  elif user_input.lower == "quit" or user_input.lower() == "4":
    quit()
    
  else:
    print("please type:new,log in, help or quit.")


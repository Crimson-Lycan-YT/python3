"""
Program: nostalSys.py
Author:  Giovanni Arias
Date:    5-20-2021

Note: A custom module has to import this. This is just a base that contains dictionaries
and functions that work with only these dictionaries.
"""
import json, random

#Dictionary of a pet's basic stats that are key in every pet sim.
pet_info_base = {"name":"",
                 "age":0,
                 "mood":0,
                 "belly":0,
                 "secretIQStat":0,
                 "secretLuckStat":0,
                 "affinity":0,
                 "ID":"69-420-9000+",
                 "mainTimekeeper":0,
                 "moodTimekeeper":0,
                 "bellyTimekeeper":0
                }

#Dictionary of a player stats, the pet and the player will both grow.
player_info_base = {"name":"player",
                    "password":"",
                    "money":0,
                    "ID":"69-420-9000+",
                    "moneyTimekeeper":0,
                    "affinity":0,
                    "level":0,
                    "experience":0
                   }

#Initialize player data.
def initNewGamePlayer(player_info_base):
    player_info_base["money"] = 100
    return player_info_base

#Load player data.
def loadGamePlayer(player_info_base):
    print("Loading game...")
    with open('player.txt') as json_file:
        player_info_base = json.load(json_file)
    print("Game loaded.")
    return player_info_base

#Save player data.
def saveGamePlayer(player_info_base):
    print("Saving player data...")
    with open('player.txt', 'w') as outfile:
        json.dump(player_info_base, outfile)
    print("Player data saved.")

#Load basic pet data. A game using NostalSys needs to load expansion data in their own program for other key data.
def loadPetData(pet_info_base):
    print("Loading pet (1/2)...")
    with open('pet_base.txt') as json_file:
        pet_info_base = json.load(json_file)
    print("Pet file (base) loaded.")
    return pet_info_base

#Pet command
def petCommand(pet_info_base):
    print("You decided to pet your pet.")
    
    if(pet_info_base["mood"] < 10):
        pet_info_base["mood"] += 1
        pet_info_base["moodTimekeeper"] = 0
        
        if(pet_info_base["mood"] <= 3):
            print("Your pet's mood increased, but it looks sad.")
        elif(pet_info_base["mood"] <= 6):
            print("Your pet's mood increased, but it looks bored.")
        elif(pet_info_base["mood"] <= 9):
            print("Your pet's mood increased, it looks happy.")
        elif(pet_info_base["mood"] == 10):
            print("Your pet is now brimming with energy.")
        
    elif(pet_info_base["mood"] == 10):
        print("Your pet is brimming with energy.")
        
    return pet_info_base


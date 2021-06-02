"""
Program: petTerminalV2.py
Author:  Giovanni Arias
Date:    3-31-2021
"""
# Imported modules go here.
import json, random
#I'm using json for the easy loading and saving of files.
#I'm also gonna need to use pseudorandom numbers for stat and xp assignments.

# Create a dictionary that holds all of the pet's key information,
# perfect for functions and file loading/saving.
petInfo = {"name":"", "lifeStage":"", "age":0, "mood":0, "belly":0, "airStat":0,
           "airLevel":0, "airProgress":0, "armorStat":0, "armorLevel":0,
           "armorProgress":0, "landStat": 0, "landLevel":0, "landProgress":0,
           "powerStat":0, "powerLevel":0, "powerProgress":0, "seaStat":0,
           "seaLevel":0, "seaProgress":0, "staminaStat":0, "staminaLevel":0,
           "staminaProgress":0, "secretIQStat":0, "secretLuckStat":0,
           "affinity":0, "ID":"", "mainTimekeeper":0, "moodTimekeeper":0, 
           "bellyTimekeeper":0}

# Dictionary for player info.
playerInfo = {"name":"player", "password":"", "money":0, "ID":"", "moneyTimekeeper": 0}

# Functions for "New Game".
def initNewGamePlayer(playerInfo):
    playerInfo["money"] = 100
    return playerInfo

def initNewGamePet(petInfo):
    petInfo["lifeStage"] = "Egg"
    return petInfo

# Functions designed to load a game from file.
def loadGamePlayer(playerInfo):
    print("Loading game...")
    with open('player.txt') as json_file:
        playerInfo = json.load(json_file)
    print("Game loaded.")
    return playerInfo

def loadGamePet(playerInfo, petInfo):
    print("Loading pet...")
    with open('pet.txt') as json_file:
        petInfo = json.load(json_file)
    print("Pet file loaded.")
    return petInfo

# Functions designed to save a game to a file.
def saveGamePlayer(playerInfo):
    print("Saving game...")
    with open('player.txt', 'w') as outfile:
        json.dump(playerInfo, outfile)
    print("Game saved.")
    
def saveGamePet(playerInfo, petInfo):
    print("Saving pet...")
    with open('pet.txt', 'w') as outfile:
        json.dump(petInfo, outfile)
    print("Pet file saved.")
    
# Function to name the pet & reassign stats when an egg hatches. 
def eggHatch(petInfo):
    petInfo["mood"] = 5 # Set Mood & Belly to 5. (Sonic Advance Chao Garden research)
    petInfo["belly"] = 5
    petInfo["secretIQStat"] = random.randint(1,9999) # Set IQ & Luck to random numbers from 1 to 9999 (this happens once per hatch.).
    petInfo["secretLuckStat"] = random.randint(1,9999)
    petInfo["lifeStage"] = "Child"
    petInfo["name"] = input("Give your pet a name: ")
    print("Your pet's name is now:", petInfo["name"])
    return petInfo

# Rename command
def rename(petInfo):
    petInfo["name"] = input("Give your pet a new name: ")
    print("Your pet's name is now:", petInfo["name"])
    return petInfo

# Display stats
def displayStats(petInfo, playerInfo):
    print("Status:")
    print("Money:", playerInfo["money"])
    print("Name:", petInfo["name"])
    print("Stage:", petInfo["lifeStage"])
    print("Mood:", petInfo["mood"])
    print("Belly:", petInfo["belly"])
    print("Air Stat:", petInfo["airStat"], "Level:", petInfo["airLevel"])
    print("Progress:", petInfo["airProgress"])
    print("Armor Stat:", petInfo["armorStat"], "Level:", petInfo["armorLevel"])
    print("Progress:", petInfo["armorProgress"])
    print("Land Stat:", petInfo["landStat"], "Level:", petInfo["landLevel"])
    print("Progress:", petInfo["landProgress"])
    print("Power Stat:", petInfo["powerStat"], "Level:", petInfo["powerLevel"])
    print("Progress:", petInfo["powerProgress"])
    print("Sea Stat:", petInfo["seaStat"], "Level:", petInfo["seaLevel"])
    print("Progress:", petInfo["seaProgress"])
    print("Stamina Stat:", petInfo["staminaStat"], "Level:", petInfo["staminaLevel"])
    print("Progress:", petInfo["staminaProgress"])
    print("IQ:", petInfo["secretIQStat"]) # To be removed after final release.
    print("Luck:", petInfo["secretLuckStat"]) # This one too.

# Display possible commands.
def displayCommands():
    print("Command List:")
    print("\"Stats\" = Check your pet's stats.")
    print("\"Watch\" = Look at your pet and see what it does.")
    print("\"Feed\" = Feed your pet.")
    print("\"Pet\" = Pet your pet.")
    print("\"Save\" = Save your game progress.")
    print("\"Quit\" = Exit the program.")
    
    print("Special Commands:") # Special Command List
    
    if petInfo["lifeStage"] == "Egg":
        print("\"Hatch\" = Hatch the egg.")
    if petInfo["name"] != "" and petInfo["lifeStage"] != "Egg":
        print("\"Rename\" = Rename your pet.")
    else:
        print("No special commands available...")

    print("")

# Pet command
def petCommand(petInfo):
    print("You decided to pet your pet.")
    
    if petInfo["mood"] < 10:
        petInfo["mood"] += 1
        petInfo["moodTimekeeper"] = 0
        
        if petInfo["mood"] <= 3:
            print("Your pet's mood increased, but it looks sad.")
        elif petInfo["mood"] <= 6:
            print("Your pet's mood increased, but it looks bored.")
        elif petInfo["mood"] <= 9:
            print("Your pet's mood increased, it looks happy.")
        elif petInfo["mood"] == 10:
            print("Your pet is now brimming with energy.")
        
    elif petInfo["mood"] == 10:
        print("Your pet is brimming with energy.")
        
    return petInfo

# Feed command
def feedCommand(petInfo):
    airUnrounded = 0
    armorUnrounded = 0
    landUnrounded = 0
    powerUnrounded = 0
    seaUnrounded = 0
    staminaUnrounded = 0
    
    displayFoodList() # Function call in a function...
    foodType = input("What do you want to feed it? ")
    
    if foodType == "Nut" or foodType == "nut":
        print("You tried to feed your pet the nut.")
        
        if petInfo["belly"] < 10:
            petInfo["belly"] += 1
            petInfo["bellyTimekeeper"] = 0
        
            if petInfo["belly"] <= 3:
                print("Your pet ate the nut, but it still looks really hungry.")
            elif petInfo["belly"] <= 6:
                print("Your pet ate the nut, but it still looks hungry.")
            elif petInfo["belly"] <= 9:
                print("Your pet ate the nut, it looks satisfied.")
            elif petInfo["belly"] == 10:
                print("Your pet ate the nut, and it now has a full belly.")
        
            if petInfo["staminaLevel"] == 99 and petInfo["staminaProgress"] >= 100:
                petInfo["staminaProgress"] = 100
                print("Your pet's stamina stat cannot be improved any further.")
            else:
                staminaUnrounded += random.randint(5,25)
                if staminaUnrounded >= 5 and staminaUnrounded <= 14:
                    petInfo["staminaProgress"] += 10
                elif staminaUnrounded >= 15 and staminaUnrounded <= 24:
                    petInfo["staminaProgress"] += 20
                elif staminaUnrounded == 25:
                    petInfo["staminaProgress"] += 30
        
        elif petInfo["belly"] == 10:
            print("Your pet is too full to eat anything.")
    
    else:
        print("Invalid Input")
    return(petInfo)
    
# Display the food list.
def displayFoodList():
    print("")
    print("\"Nut\" = Basic nut. Increases stamina.")
    
# Stat distribution function.
def statDist(petInfo):
    if petInfo["airLevel"] == 99:
        pass
    elif petInfo["airLevel"] >= 0 and petInfo["airLevel"] <= 98:
        if petInfo["airProgress"] >= 100:
            petInfo["airProgress"] -= 100
            petInfo["airStat"] += random.randint(10,60)
            petInfo["airLevel"] += 1
            
    if petInfo["armorLevel"] == 99:
        pass
    elif petInfo["armorLevel"] >= 0 and petInfo["armorLevel"] <= 98:
        if petInfo["armorProgress"] >= 100:
            petInfo["armorProgress"] -= 100
            petInfo["armorStat"] += random.randint(10,60)
            petInfo["armorLevel"] += 1
            
    if petInfo["landLevel"] == 99:
        pass
    elif petInfo["landLevel"] >= 0 and petInfo["landLevel"] <= 98:
        if petInfo["landProgress"] >= 100:
            petInfo["landProgress"] -= 100
            petInfo["landStat"] += random.randint(10,60)
            petInfo["landLevel"] += 1
            
    if petInfo["powerLevel"] == 99:
        pass
    elif petInfo["powerLevel"] >= 0 and petInfo["powerLevel"] <= 98:
        if petInfo["powerProgress"] >= 100:
            petInfo["powerProgress"] -= 100
            petInfo["powerStat"] += random.randint(10,60)
            petInfo["powerLevel"] += 1
            
            if petInfo["powerStat"] > 9000:
                print("It's over 9000!!!")
            
    if petInfo["seaLevel"] == 99:
        pass
    elif petInfo["seaLevel"] >= 0 and petInfo["seaLevel"] <= 98:
        if petInfo["seaProgress"] >= 100:
            petInfo["seaProgress"] -= 100
            petInfo["seaStat"] += random.randint(10,60)
            petInfo["seaLevel"] += 1
            
    if petInfo["staminaLevel"] == 99:
        pass
    elif petInfo["staminaLevel"] >= 0 and petInfo["staminaLevel"] <= 98:
        if petInfo["staminaProgress"] >= 100:
            petInfo["staminaProgress"] -= 100
            petInfo["staminaStat"] += random.randint(10,60)
            petInfo["staminaLevel"] += 1
            
    return(petInfo)

# Watch command
def watchCommand(petInfo):
    print("You decided to observe your pet for a while.")
    while True:
        watchType = random.randint(1,4)
        if watchType == 1:
            print("Your pet sat down on the soft grass.")
            break
            
        elif watchType == 2:
            if petInfo["landStat"] <= 500:
                tripChance = random.randint(1,100)
                print("Your pet is walking around the garden.")
                if tripChance >= 51:
                    print("Your pet tripped and fell!")
                    petInfo["mood"] -= 3
                    while True:
                        tripOpt = input("Are you going to help it? ")
                        print("")
                        
                        if tripOpt == 'Y' or tripOpt == 'y':
                            print("You consoled your pet and it felt better about itself.")
                            petInfo["mood"] += random.randint(1,3)
                            petInfo["affinity"] += 1
                            break
                        elif tripOpt == 'N' or tripOpt == 'n':
                            print("Your pet just stood there crying, you monster...")
                            petInfo["affinity"] -= 1
                            break
                        else:
                            print("Invalid choice, press \"Y\" or \"N\".")
                        
                break
                
            elif petInfo["landStat"] <= 1000:
                tripChance = random.randint(1,100)
                print("Your pet is running around the garden.")
                if tripChance >= 26: # A pet's out of control running can lead to accidents.
                    print("Your pet tripped and fell!")
                    petInfo["mood"] -= 3
                    while True:
                        tripOpt = input("Are you going to help it? ")
                        
                        if tripOpt == 'Y' or tripOpt == 'y':
                            print("You consoled your pet and it felt better about itself.")
                            petInfo["mood"] += random.randint(1,3)
                            petInfo["affinity"] += 1
                            break
                        elif tripOpt == 'N' or tripOpt == 'n':
                            print("Your pet just stood there crying, you monster...")
                            petInfo["affinity"] -= 1
                            break
                        else:
                            print("Invalid choice, press \"Y\" or \"N\".")
                        
                break
                
            elif petInfo["landStat"] <= 1500:
                tripChance = random.randint(1,100)
                print("Your pet is running around the garden.")
                if tripChance >= 51:
                    print("Your pet tripped and fell!")
                    petInfo["mood"] -= 3
                    while True:
                        tripOpt = input("Are you going to help it? ")
                        
                        if tripOpt == 'Y' or tripOpt == 'y':
                            print("You consoled your pet and it felt better about itself.")
                            petInfo["mood"] += random.randint(1,3)
                            petInfo["affinity"] += 1
                            break
                        elif tripOpt == 'N' or tripOpt == 'n':
                            print("Your pet just stood there crying, you monster...")
                            petInfo["affinity"] -= 1
                            break
                        else:
                            print("Invalid choice, press \"Y\" or \"N\".")
                        
                break
                
            elif petInfo["landStat"] <= 2000:
                tripChance = random.randint(1,100)
                print("Your pet is running around the garden.")
                if tripChance >= 76:
                    print("Your pet tripped and fell!")
                    petInfo["mood"] -= 3
                    while True:
                        tripOpt = input("Are you going to help it? ")
                        
                        if tripOpt == 'Y' or tripOpt == 'y':
                            print("You consoled your pet and it felt better about itself.")
                            petInfo["mood"] += random.randint(1,3)
                            petInfo["affinity"] += 1
                            break
                        elif tripOpt == 'N' or tripOpt == 'n':
                            print("Your pet just stood there crying, you monster...")
                            petInfo["affinity"] -= 1
                            break
                        else:
                            print("Invalid choice, press \"Y\" or \"N\".")
                        
                break

        elif watchType == 3:
            print("Gross! Your pet farted out in the open...")
            print("It smells like it ate rotten eggs or spoiled beans...")
            break
        
        elif watchType == 4:
            print("Your pet drew some graffiti on the ground.")
            while True:
                graffitiOpt = input("Will you take a look? ")
                print("")
                graffitiType = random.randint(1,6)
                
                if graffitiOpt == 'Y' or graffitiOpt == 'y': # Get ready for some easter eggs...
                    if graffitiType == 1:
                        print("It appears to be blank, but it's actually a picture of a cow eating grass.")
                        print("The grass was eaten by the cow, and the cow went away to find more grass to eat.")
                        print("|----------|")
                        print("|          |")
                        print("|          |")
                        print("|          |")
                        print("|          |")
                        print("|          |")
                        print("|----------|")
                        if petInfo["secretIQStat"] < 9999:
                            petInfo["secretIQStat"] += 1
                    elif graffitiType == 2:
                        print("|--------------------|")
                        print("|                    |")
                        print("|  |--------------|  |")
                        print("|  |--------------|  |")
                        print("|         __         |")
                        print("|        /  \        |")
                        print("|       |    |       |")
                        print("|       |    |       |")
                        print("|        \__/        |")
                        print("|  |--------------|  |")
                        print("|  |--------------|  |")
                        print("|                    |")
                        print("|--------------------|")
                        print("An egg sandwich.")
                        if petInfo["secretIQStat"] < 9999:
                            petInfo["secretIQStat"] += 1
                    elif graffitiType == 3:
                        if petInfo["affinity"] > 0:
                            print("A picture of a blue hedgehog. Gotta go fast.")
                            petInfo["affinity"] += 1
                        elif petInfo["affinity"] < 0:
                            print("A picture of a black hedgehog armed with a gun.")
                            print("Where's that DAMN fourth chaos emerald!?")
                            petInfo["affinity"] -= 1
                        elif petInfo["affinity"] == 0:
                            print("A picture of 7 emeralds, each one having a different color.")
                            print("A ruby also appears in the picture.")
                    elif graffitiType == 4:
                        print("A picture of a dog working on a game.")
                        print("If you wait patiently, maybe he'll finish it.")
                    elif graffitiType == 5:
                        print("Cool! It's the mark of the Shibuya GG!")
                        print("Jet Set Radio!!!")
                    elif graffitiType == 6:
                        print("A picture of Pokemon #155: Cyndaquil. A Fire type.") # One of my favorite starters.
                    break
                elif graffitiOpt == 'N' or graffitiOpt == 'n':
                    print("You decided not to take a look.")
                    print("Your pet seems a bit disappointed.")
                    petInfo["mood"] -= 1
                    break
                else:
                    print("Invalid choice, press \"Y\" or \"N\".")
                    
            break
                    
    return(petInfo)
    
# Program loop to load game or start new game
print("Welcome to the main area!")

while True:
    print("\"Load\" = Load game from file.")
    print("\"New\" = Start a new game.")
    gameStart = input("What is your choice? ")
    
    if (gameStart == 'New' or gameStart == 'new'):
        initNewGamePlayer(playerInfo)
        initNewGamePet(petInfo)
        print("New game started.")
        break
    elif (gameStart == 'Load' or gameStart == 'load'):
        print("")
        playerInfo = loadGamePlayer(playerInfo)
        print("")
        petInfo = loadGamePet(playerInfo, petInfo)
        break
    else:
        print("Incorrect Input. Enter \"Load\" or \"New\".")
    
# Main game loop
while True:
    print("")
    displayCommands()
    commandInput = input("Input a command: ")
    
    if commandInput == "stats" or commandInput == "Stats":
        print("")
        displayStats(petInfo, playerInfo)
    elif commandInput == "watch" or commandInput == "Watch":
        if petInfo["lifeStage"] == "Egg":
            print("It's only an egg, go hatch it.")
        elif petInfo["lifeStage"] == "Child" or petInfo["lifeStage"] == "Adult":
            print("")
            watchCommand(petInfo)
            petInfo["bellyTimekeeper"] += 1
            petInfo["moodTimekeeper"] += 1
            petInfo["mainTimekeeper"] += 1
            playerInfo["moneyTimekeeper"] += 1
    elif commandInput == "feed" or commandInput == "Feed":
        if petInfo["lifeStage"] == "Egg":
            print("Hatch the egg first before you feed your pet.")
        elif petInfo["lifeStage"] == "Child" or petInfo["lifeStage"] == "Adult":
            feedCommand(petInfo)
            statDist(petInfo)
            petInfo["moodTimekeeper"] += 1
            petInfo["mainTimekeeper"] += 1
            playerInfo["moneyTimekeeper"] += 1
    elif commandInput == "pet" or commandInput == "Pet":
        if petInfo["lifeStage"] == "Egg":
            print("Hatch the egg first before you pet your pet.")
        elif petInfo["lifeStage"] == "Child" or petInfo["lifeStage"] == "Adult":
            print("")
            petCommand(petInfo)
            petInfo["bellyTimekeeper"] += 1
            petInfo["mainTimekeeper"] += 1
            playerInfo["moneyTimekeeper"] += 1
    elif commandInput == "save" or commandInput == "Save":
        print("")
        saveGamePlayer(playerInfo)
        print("")
        saveGamePet(playerInfo, petInfo)
    elif commandInput == "quit" or commandInput == "Quit":
        break
    
    # Special Commands
    elif commandInput == "hatch" or commandInput == "Hatch":
        if petInfo["lifeStage"] == "Egg":
            print("")
            eggHatch(petInfo)
        elif petInfo["lifeStage"] == "Child" or petInfo["lifeStage"] == "Adult":
            print("You can't use that command on a pet that has already hatched from it's egg.")
    elif commandInput == "rename" or commandInput == "Rename":
        if petInfo["lifeStage"] == "Egg":
            print("You can't name your pet until you hatch it first.")
        elif petInfo["lifeStage"] == "Child" or petInfo["lifeStage"] == "Adult":
            print("")
            rename(petInfo)
            
    # Invalid Input
    else:
        print("Invalid Command.")
    
    # Timekeeper code
    if petInfo["moodTimekeeper"] == 3:
        petInfo["mood"] -= 1
        petInfo["moodTimekeeper"] = 0
        
    if petInfo["bellyTimekeeper"] == 3:
        petInfo["belly"] -= 1
        petInfo["bellyTimekeeper"] = 0
        
    if petInfo["mainTimekeeper"] == 210: # 14 days = 1 "pet year", 15 actions per day, 210 actions.
        petInfo["age"] += 1
        petInfo["mainTimekeeper"] = 0
        
    if playerInfo["moneyTimekeeper"] == 15: # 10 units added to your account every day.
        playerInfo["money"] += 10
        playerInfo["moneyTimekeeper"] = 0
    
print("")
print("Good-Bye.")

"""
Program: petTerminalV3.py
Author:  Giovanni Arias
Date:    5-20-2021

Note: Requires the "nostalSys" base to work properly.
"""
import json, random, nostalSys

debug_mode = True

pet_info_xpan = {"ID":"69-420-9000+",
                 "lifeStage":"",
                 "airStat":0,
                 "airLevel":0,
                 "airProgress":0,
                 "armorStat":0,
                 "armorLevel":0,
                 "armorProgress":0,
                 "landStat": 0,
                 "landLevel":0,
                 "landProgress":0,
                 "powerStat":0,
                 "powerLevel":0,
                 "powerProgress":0,
                 "seaStat":0,
                 "seaLevel":0,
                 "seaProgress":0,
                 "staminaStat":0,
                 "staminaLevel":0,
                 "staminaProgress":0
                }

#Utilize code from nostalSys.
pet_base = nostalSys.pet_info_base
player_base = nostalSys.player_info_base

#Initialize pet data.
def initNewGamePet(pet_info_xpan):
    pet_info_xpan["lifeStage"] = "Egg"
    return pet_info_xpan

#Load pet data unique to game.
def loadPetExpansion(pet_info_xpan):
    print("Loading pet (2/2)...")
    with open('pet_xpan.txt') as json_file:
        pet_info_xpan = json.load(json_file)
    print("Pet file (game expansion) loaded.")
    return pet_info_xpan

#Verify player and pet data.
def verifyData(player_base, pet_base, pet_info_xpan):
    print("Verifying NostalSys IDs...")
    if(player_base["ID"] == pet_base["ID"] and
       pet_base["ID"] == pet_info_xpan["ID"] and
       pet_info_xpan["ID"] == player_base["ID"]):
        print("NostalSys IDs Verified.")
    elif(player_base["ID"] != pet_base["ID"] and
         pet_base["ID"] == pet_info_xpan["ID"] and
         pet_info_xpan["ID"] != player_base["ID"]):
        print("Is this your friend's pet? Take good care of it.")
    elif(player_base["ID"] == pet_base["ID"] and
         pet_base["ID"] != pet_info_xpan["ID"] and
         pet_info_xpan["ID"] != player_base["ID"]):
        print("Your pet's stats are modified!")
        print("If you keep this up, then...")
        print("You're gonna have a bad time.")
        exit()

#Save pet data.
def saveGamePet(player_base, pet_base, pet_info_xpan):
    print("Saving pet data (1/2)...")
    with open('pet_base.txt', 'w') as outfile:
        json.dump(pet_base, outfile)
    print("Saving pet data (2/2)...")
    with open('pet_xpan.txt', 'w') as outfile:
        json.dump(pet_info_xpan, outfile)
    print("Pet files saved.")

#Function to name the pet & reassign it's stats when an egg hatches. 
def eggHatch(pet_base, pet_info_xpan):
    pet_base["mood"] = 5 #Set Mood & Belly to 5. (Sonic Advance Chao Garden research)
    pet_base["belly"] = 5
    pet_base["secretIQStat"] = random.randint(1,9999) #Set IQ & Luck to random numbers from 1 to 9999 (happens once per hatch).
    pet_base["secretLuckStat"] = random.randint(1,9999)
    pet_info_xpan["lifeStage"] = "Child"
    pet_base["name"] = input("Give your pet a name: ")
    print("Your pet's name is now:", pet_base["name"])
    return pet_base, pet_info_xpan

#Rename command
def rename(pet_base):
    pet_base["name"] = input("Give your pet a new name: ")
    print("Your pet's name is now:", pet_base["name"])
    return pet_base

#Display stats
def displayStats(pet_base, player_base, pet_info_xpan):
    print("Status:")
    print("Money:", player_base["money"])
    print("Name:", pet_base["name"])
    print("Stage:", pet_info_xpan["lifeStage"])
    print("Mood:", pet_base["mood"])
    print("Belly:", pet_base["belly"])
    print("Air Stat:", pet_info_xpan["airStat"], "Level:", pet_info_xpan["airLevel"])
    print("Progress:", pet_info_xpan["airProgress"])
    print("Armor Stat:", pet_info_xpan["armorStat"], "Level:", pet_info_xpan["armorLevel"])
    print("Progress:", pet_info_xpan["armorProgress"])
    print("Land Stat:", pet_info_xpan["landStat"], "Level:", pet_info_xpan["landLevel"])
    print("Progress:", pet_info_xpan["landProgress"])
    print("Power Stat:", pet_info_xpan["powerStat"], "Level:", pet_info_xpan["powerLevel"])
    print("Progress:", pet_info_xpan["powerProgress"])
    print("Sea Stat:", pet_info_xpan["seaStat"], "Level:", pet_info_xpan["seaLevel"])
    print("Progress:", pet_info_xpan["seaProgress"])
    print("Stamina Stat:", pet_info_xpan["staminaStat"], "Level:", pet_info_xpan["staminaLevel"])
    print("Progress:", pet_info_xpan["staminaProgress"])
    
    if(debug_mode == True):
        print("IQ:", pet_base["secretIQStat"]) # For programmers only.
        print("Luck:", pet_base["secretLuckStat"])

#Display possible commands.
def displayCommands(pet_base, pet_info_xpan):
    specialCommands = False
    print("Command List:")
    print("\"Stats\" = Check your pet's stats.")
    print("\"Watch\" = Look at your pet and see what it does.")
    print("\"Feed\" = Feed your pet.")
    print("\"Pet\" = Pet your pet.")
    print("\"Save\" = Save your game progress.")
    print("\"Quit\" = Exit the program.\n")
    print("Special Commands:") # Special Command List
    
    if(pet_info_xpan["lifeStage"] == "Egg"):
        specialCommands = True
        print("\"Hatch\" = Hatch the egg.")
    
    if(pet_base["name"] != "" and pet_info_xpan["lifeStage"] != "Egg"):
        specialCommands = True
        print("\"Rename\" = Rename your pet.")
    
    if(specialCommands == False):
        print("No special commands available...")
    
    print("")

#Feed command
def feedCommand(player_base, pet_base, pet_info_xpan):
    airUnrounded = 0
    armorUnrounded = 0
    landUnrounded = 0
    powerUnrounded = 0
    seaUnrounded = 0
    staminaUnrounded = 0
    
    displayFoodList() # Function call in a function...
    foodType = input("What do you want to feed it? ")
    
    if(foodType == "Nut" or foodType == "nut"):
        print("You tried to feed your pet the nut.")
        
        if(pet_base["belly"] < 10):
            pet_base["belly"] += 1
            pet_base["bellyTimekeeper"] = 0
        
            if(pet_base["belly"] <= 3):
                print("Your pet ate the nut, but it still looks really hungry.")
            elif(pet_base["belly"] <= 6):
                print("Your pet ate the nut, but it still looks hungry.")
            elif(pet_base["belly"] <= 9):
                print("Your pet ate the nut, it looks satisfied.")
            elif(pet_base["belly"] == 10):
                print("Your pet ate the nut, and it now has a full belly.")
        
            if(pet_info_xpan["staminaLevel"] == 99 and pet_info_xpan["staminaProgress"] >= 100):
                pet_info_xpan["staminaProgress"] = 100
                print("Your pet's stamina stat cannot be improved any further.")
            else:
                staminaUnrounded += random.randint(5,25)
                if(staminaUnrounded >= 5 and staminaUnrounded <= 14):
                    pet_info_xpan["staminaProgress"] += 10
                elif(staminaUnrounded >= 15 and staminaUnrounded <= 24):
                    pet_info_xpan["staminaProgress"] += 20
                elif(staminaUnrounded == 25):
                    pet_info_xpan["staminaProgress"] += 30
        
        elif(pet_base["belly"] == 10):
            print("Your pet is too full to eat anything.")
    
    else:
        print("Invalid Input")
    
    return pet_base, pet_info_xpan, player_base

#Display the food list.
def displayFoodList():
    print("")
    print("\"Nut\" = Basic nut. Increases stamina.")

#Stat distribution function.
def statDist(pet_info_xpan):
    if(pet_info_xpan["airLevel"] == 99):
        pass
    elif(pet_info_xpan["airLevel"] >= 0 and pet_info_xpan["airLevel"] <= 98):
        if(pet_info_xpan["airProgress"] >= 100):
            pet_info_xpan["airProgress"] -= 100
            pet_info_xpan["airStat"] += random.randint(10,60)
            pet_info_xpan["airLevel"] += 1
            
    if(pet_info_xpan["armorLevel"] == 99):
        pass
    elif(pet_info_xpan["armorLevel"] >= 0 and pet_info_xpan["armorLevel"] <= 98):
        if(pet_info_xpan["armorProgress"] >= 100):
            pet_info_xpan["armorProgress"] -= 100
            pet_info_xpan["armorStat"] += random.randint(10,60)
            pet_info_xpan["armorLevel"] += 1
            
    if(pet_info_xpan["landLevel"] == 99):
        pass
    elif(pet_info_xpan["landLevel"] >= 0 and pet_info_xpan["landLevel"] <= 98):
        if(pet_info_xpan["landProgress"] >= 100):
            pet_info_xpan["landProgress"] -= 100
            pet_info_xpan["landStat"] += random.randint(10,60)
            pet_info_xpan["landLevel"] += 1
            
    if(pet_info_xpan["powerLevel"] == 99):
        pass
    elif(pet_info_xpan["powerLevel"] >= 0 and pet_info_xpan["powerLevel"] <= 98):
        if(pet_info_xpan["powerProgress"] >= 100):
            pet_info_xpan["powerProgress"] -= 100
            pet_info_xpan["powerStat"] += random.randint(10,60)
            pet_info_xpan["powerLevel"] += 1
            
            if(pet_info_xpan["powerStat"] > 9000):
                print("It's over 9000!!!")
            
    if(pet_info_xpan["seaLevel"] == 99):
        pass
    elif(pet_info_xpan["seaLevel"] >= 0 and pet_info_xpan["seaLevel"] <= 98):
        if(pet_info_xpan["seaProgress"] >= 100):
            pet_info_xpan["seaProgress"] -= 100
            pet_info_xpan["seaStat"] += random.randint(10,60)
            pet_info_xpan["seaLevel"] += 1
            
    if(pet_info_xpan["staminaLevel"] == 99):
        pass
    elif(pet_info_xpan["staminaLevel"] >= 0 and pet_info_xpan["staminaLevel"] <= 98):
        if(pet_info_xpan["staminaProgress"] >= 100):
            pet_info_xpan["staminaProgress"] -= 100
            pet_info_xpan["staminaStat"] += random.randint(10,60)
            pet_info_xpan["staminaLevel"] += 1
            
    return pet_info_xpan

#Watch command
def watchCommand(pet_base, pet_info_xpan):
    print("You decided to observe your pet for a while.")
    while True:
        watchType = random.randint(1,4)
        if(watchType == 1):
            print("Your pet sat down on the soft grass.")
            break
            
        elif(watchType == 2):
            if(pet_info_xpan["landStat"] <= 500):
                tripChance = random.randint(1,100)
                print("Your pet is walking around the garden.")
                if(tripChance >= 51):
                    petTripped(pet_base)  
                break
                
            elif(pet_info_xpan["landStat"] <= 1000):
                tripChance = random.randint(1,100)
                print("Your pet is running around the garden.")
                if(tripChance >= 26): # A pet's out of control running can lead to accidents.
                    petTripped(pet_base)
                break
                
            elif(pet_info_xpan["landStat"] <= 1500):
                tripChance = random.randint(1,100)
                print("Your pet is running around the garden.")
                if(tripChance >= 51):
                    petTripped(pet_base)
                break
                
            elif(pet_info_xpan["landStat"] <= 2000):
                tripChance = random.randint(1,100)
                print("Your pet is running around the garden.")
                if(tripChance >= 76):
                    petTripped(pet_base)
                break

        elif(watchType == 3):
            print("Gross! Your pet farted out in the open...")
            print("It smells like it ate rotten eggs or spoiled beans...")
            break
        
        elif(watchType == 4):
            print("Your pet drew some graffiti on the ground.")
            while True:
                graffitiOpt = input("Will you take a look? ")
                print("")
                graffitiType = random.randint(1,6)
                
                if(graffitiOpt == 'Y' or graffitiOpt == 'y'): # Get ready for some easter eggs...
                    if(graffitiType == 1):
                        print("It appears to be blank, but it's actually a picture of a cow eating grass.")
                        print("The grass was eaten by the cow, and the cow went away to find more grass to eat.")
                        print("|----------|")
                        print("|          |")
                        print("|          |")
                        print("|          |")
                        print("|          |")
                        print("|          |")
                        print("|----------|")
                        if(pet_base["secretIQStat"] < 9999):
                            pet_base["secretIQStat"] += 1
                    elif(graffitiType == 2):
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
                        if(pet_base["secretIQStat"] < 9999):
                            pet_base["secretIQStat"] += 1
                    elif(graffitiType == 3):
                        if(pet_base["affinity"] > 0):
                            print("A picture of a blue hedgehog. Gotta go fast.")
                            pet_base["affinity"] += 1
                        elif(pet_base["affinity"] < 0):
                            print("A picture of a black hedgehog armed with a gun.")
                            print("Where's that DAMN fourth chaos emerald!?")
                            pet_base["affinity"] -= 1
                        elif(pet_base["affinity"] == 0):
                            print("A picture of 7 emeralds, each one having a different color.")
                            print("A ruby also appears in the picture.")
                    elif(graffitiType == 4):
                        print("A picture of a dog working on a game.")
                        print("If you wait patiently, maybe he'll finish it.")
                    elif(graffitiType == 5):
                        print("Cool! It's the mark of the Shibuya GG!")
                        print("Jet Set Radio!!!")
                    elif(graffitiType == 6):
                        print("A picture of Pokemon #155: Cyndaquil. A Fire type.") # One of my favorite starters.
                    break
                elif(graffitiOpt == 'N' or graffitiOpt == 'n'):
                    print("You decided not to take a look.")
                    print("Your pet seems a bit disappointed.")
                    pet_base["mood"] -= 1
                    break
                else:
                    print("Invalid choice, press \"Y\" or \"N\".")
                    
            break
                    
    return pet_base, pet_info_xpan

#When a pet trips...
def petTripped(pet_base):
    print("Your pet tripped and fell!")
    pet_base["mood"] -= 3
    while True:
        tripOpt = input("Are you going to help it? ")
        print("")
                        
        if(tripOpt == 'Y' or tripOpt == 'y'):
            print("You consoled your pet and it felt better about itself.")
            pet_base["mood"] += random.randint(1,3)
            pet_base["affinity"] += 1
            break
            
        elif(tripOpt == 'N' or tripOpt == 'n'):
            print("Your pet just stood there crying, you monster...")
            pet_base["affinity"] -= 1
            break
            
        else:
            print("Invalid choice, press \"Y\" or \"N\".")
        
    return pet_base
    
#Game Setup
if(debug_mode == True):
    print("Debug mode enabled.")  
    
print("Welcome to the main area!")

while True:
    print("\"Load\" = Load game from file.")
    print("\"New\" = Start a new game.")
    gameStart = input("What is your choice? ")
    
    if (gameStart == 'New' or gameStart == 'new'):
        player_base = nostalSys.initNewGamePlayer(player_base)
        initNewGamePet(pet_info_xpan)
        print("New game started.")
        break
    
    elif (gameStart == 'Load' or gameStart == 'load'):
        print("")
        player_base = nostalSys.loadGamePlayer(player_base)
        print("")
        pet_base = nostalSys.loadPetData(pet_base)
        pet_info_xpan = loadPetExpansion(pet_info_xpan)
        print("")
        verifyData(player_base, pet_base, pet_info_xpan)
        break
    
    else:
        print("Incorrect Input. Enter \"Load\" or \"New\".")

#Main game loop
while True:
    print("")
    displayCommands(pet_base, pet_info_xpan)
    commandInput = input("Input a command: ")
    
    if(commandInput == "stats" or commandInput == "Stats"):
        print("")
        displayStats(pet_base, player_base, pet_info_xpan)
    elif(commandInput == "watch" or commandInput == "Watch"):
        if(pet_info_xpan["lifeStage"] == "Egg"):
            print("It's only an egg, go hatch it.")
        elif(pet_info_xpan["lifeStage"] == "Child" or pet_info_xpan["lifeStage"] == "Adult"):
            print("")
            watchCommand(pet_base, pet_info_xpan)
            pet_base["bellyTimekeeper"] += 1
            pet_base["moodTimekeeper"] += 1
            pet_base["mainTimekeeper"] += 1
            player_base["moneyTimekeeper"] += 1
    elif(commandInput == "feed" or commandInput == "Feed"):
        if(pet_info_xpan["lifeStage"] == "Egg"):
            print("Hatch the egg first before you feed your pet.")
        elif(pet_info_xpan["lifeStage"] == "Child" or pet_info_xpan["lifeStage"] == "Adult"):
            feedCommand(player_base, pet_base, pet_info_xpan)
            statDist(pet_info_xpan)
            pet_base["moodTimekeeper"] += 1
            pet_base["mainTimekeeper"] += 1
            player_base["moneyTimekeeper"] += 1
    elif(commandInput == "pet" or commandInput == "Pet"):
        if(pet_info_xpan["lifeStage"] == "Egg"):
            print("Hatch the egg first before you pet your pet.")
        elif(pet_info_xpan["lifeStage"] == "Child" or pet_info_xpan["lifeStage"] == "Adult"):
            print("")
            nostalSys.petCommand(pet_base)
            pet_base["bellyTimekeeper"] += 1
            pet_base["mainTimekeeper"] += 1
            player_base["moneyTimekeeper"] += 1
    elif(commandInput == "save" or commandInput == "Save"):
        print("")
        nostalSys.saveGamePlayer(player_base)
        print("")
        saveGamePet(player_base, pet_base, pet_info_xpan)
    elif(commandInput == "quit" or commandInput == "Quit"):
        break
    
    #Special Commands
    elif(commandInput == "hatch" or commandInput == "Hatch"):
        if(pet_info_xpan["lifeStage"] == "Egg"):
            print("")
            eggHatch(pet_base, pet_info_xpan)
        elif(pet_info_xpan["lifeStage"] == "Child" or pet_info_xpan["lifeStage"] == "Adult"):
            print("You can't use that command on a pet that has already hatched from it's egg.")
    elif(commandInput == "rename" or commandInput == "Rename"):
        if(pet_info_xpan["lifeStage"] == "Egg"):
            print("You can't name your pet until you hatch it first.")
        elif(pet_info_xpan["lifeStage"] == "Child" or pet_info_xpan["lifeStage"] == "Adult"):
            print("")
            rename(pet_base)
            
    #Invalid Input
    else:
        print("Invalid Command.")
    
    #Timekeeper code
    if(pet_base["moodTimekeeper"] == 3):
        pet_base["mood"] -= 1
        pet_base["moodTimekeeper"] = 0
        
    if(pet_base["bellyTimekeeper"] == 3):
        pet_base["belly"] -= 1
        pet_base["bellyTimekeeper"] = 0
        
    if(pet_base["mainTimekeeper"] == 210): #14 days = 1 "pet year", 15 actions per day, 210 actions.
        pet_base["age"] += 1
        pet_base["mainTimekeeper"] = 0
        
    if(player_base["moneyTimekeeper"] == 15): #10 units added to your account every day.
        player_base["money"] += 10
        player_base["moneyTimekeeper"] = 0
    
print("")
print("Good-Bye.")

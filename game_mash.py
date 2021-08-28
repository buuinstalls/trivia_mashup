# Importing

import os
import time
import colorama
import webbrowser as wb
import ctypes
import random

# Variables

normal = "\u001b[0m"

red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
purple = "\u001b[35m"
cyan = "\u001b[36m"

# Function

def cprint(string):
    print(yellow + ":: " + normal + string)
# ---------------------------------------------
def scprint(string):
    print(yellow + "    - " + normal + string)
# ---------------------------------------------
def cerror(string):
    print(red + "#: " + normal + string)
# ---------------------------------------------
def scerror(string):
    print(red + "    #- " + normal + string)
# ---------------------------------------------
def cinfo(string):
    print(blue + "?> " + normal + string)
# ---------------------------------------------
def scinfo(string):
    print(blue + "    ?> " + normal + string)
# ---------------------------------------------
def cnotice(string):
    print(green + "!> " + normal + string)
# ---------------------------------------------
def scnotice(string):
    print(green + "    !> " + normal + string)
# ---------------------------------------------
def cinput(string):
    input(yellow + ":: " + normal + string)
# ---------------------------------------------
def scinput(string):
    input(yellow + "    - " + normal + string)
# ---------------------------------------------
def cmdinput(string):
    input(green + ">> " + normal + string)
# ---------------------------------------------
def cls():
    os.system("cls")
# ---------------------------------------------
def wait(string): # lol just in case i get mixed up with lua
    time.sleep(string)


#- Game Descriptions sorted by order
games = ["ruddytrivia", "christrivia"]
gamedesc = ["ruddy's official trivia", "chris's official trivia"]
prefix = "" # Too lazy to fix this rn, delete this tmrw if u want
            # lol

# Function for the script & The title
print(red + '''
game project v1
''')

# Some back function for commands

# Games

def home():
    os.system("cls")
    print(red + '''
    game project v1
    '''
          + green +
          '''
    select your game
    type in ''' + prefix + '''games to view games
    massive bug fix
    ''')
    cinfo("this is a useless info bar")

home()

def rungameline():
    mainscript()

def mainscript():
    rungame = input(green + ">> " + normal + "")
    if rungame == prefix + "games":
        os.system("cls")
        print(red + '''
        game project v1
        ''')
        print("")
        cinfo("This is the list of commands! :)")
        print("--------------------------------")
        cinfo("Ruddy Trivia:")
        scinfo("Command is : " + games[0])
        scinfo(gamedesc[0])
        print("     #############")
        print("--------------------------------")
        cinfo("Chris Trivia:")
        scinfo("Command is : " + games[1])
        scinfo(gamedesc[1])
        print("     #############")
        scinfo("Click enter when your finished")
        print("")
        cnotice("Enter new command below")
        rungameline()
    elif rungame == games[0]:
        os.system("cls")
        # I kinda dislike this tbh
        def smoothloader():
            print("welcome to ruddy trivia")
            wait(.58)
            print("b")
            time.sleep(0.02)
            os.system("cls")
            print("bu")
            time.sleep(0.02)
            os.system("cls")
            print("but")
            time.sleep(0.02)
            os.system("cls")
            print("but i")
            time.sleep(0.02)
            os.system("cls")
            print("but it")
            time.sleep(0.02)
            os.system("cls")
            print("but its")
            time.sleep(0.02)
            os.system("cls")
            print("but its r")
            time.sleep(0.02)
            os.system("cls")
            print("but its re")
            time.sleep(0.02)
            os.system("cls")
            print("but its rem")
            time.sleep(0.02)
            os.system("cls")
            print("but its rema")
            time.sleep(0.02)
            os.system("cls")
            print("but its remas")
            time.sleep(0.02)
            os.system("cls")
            print("but its remast")
            time.sleep(0.02)
            os.system("cls")
            print("but its remaste")
            time.sleep(0.02)
            os.system("cls")
            print("but its remaster")
            time.sleep(0.02)
            os.system("cls")
            print("but its remastere")
            time.sleep(0.02)
            os.system("cls")
            print("but its remastered")
            time.sleep(.58)
            os.system("cls")
        # Actual Menu
        print(blue + '''
                         _     _         _        _       _       
  _ __ _   _  __| | __| |_   _  | |_ _ __(_)_   _(_) __ _ 
 | '__| | | |/ _` |/ _` | | | | | __| '__| \ \ / / |/ _` |
 | |  | |_| | (_| | (_| | |_| | | |_| |  | |\ V /| | (_| |
 |_|   \__,_|\__,_|\__,_|\__, |  \__|_|  |_| \_/ |_|\__,_|
                         |___/                             
        ''')
        cinfo("To answer questions type")
        scinfo("yes / no")
        scinfo("y / n")
        questions = ["Does ruddy like monkeys?",
                     "Does ruddy like transgenders?",
                     "Does ruddy have a crush?"]

        # The game
        cinfo(questions[0])
        q = input(green + ">> " + normal + "")
        if q == "yes" or q == "y":
            print(green + "Correct!")
            print("################")
        elif q == "no" or q == "n":
            print(red + "Incorrect.")
            print("################")
        cinfo(questions[1])
        q = input(green + ">> " + normal + "")
        if q == "yes" or q == "y":
            print(red + "Incorrect.")
            print("################")
        elif q == "no" or q == "n":
            print(green + "Correct!")
            print("################")
        cinfo(questions[2])
        q = input(green + ">> " + normal + "")
        if q == "yes" or q == "y":
            print(yellow + "idek")
            print("################")
        elif q == "no" or q == "n":
            print(yellow + "idek")
            print("################")

        # The end of the Game
        print(" ")
        print(normal + "well, looks like you've reached the end")
        time.sleep(1.5)
        os.system("cls")
        print(normal + "time to go back to menu")
        time.sleep(.7)
        home()
        rungameline()
    elif rungame == games[1]:
        os.system("cls")
        print(blue + '''
       _          _       _        _       _       
   ___| |__  _ __(_)___  | |_ _ __(_)_   _(_) __ _ 
  / __| '_ \| '__| / __| | __| '__| \ \ / / |/ _` |
 | (__| | | | |  | \__ \ | |_| |  | |\ V /| | (_| |
  \___|_| |_|_|  |_|___/  \__|_|  |_| \_/ |_|\__,_|
                                                   
             ''')
        questions = ["Is chris addicted to brawlhalla?",
                     "Does chris play apex?",
                     "Does chris has a crush?",
                     "Does chris secretly a crush on mathias?"]
        cinfo(questions[0])
        q = input(green + ">> " + normal + "")
        if q == "yes" or q == "y":
            print(green + "Correct!")
            print("################")
        elif q == "no" or q == "n":
            print(red + "Incorrect.")
            print("################")
        cinfo(questions[1])
        q = input(green + ">> " + normal + "")
        if q == "yes" or q == "y":
            print(green + "Correct!")
            print("################")
        elif q == "no" or q == "n":
            print(red + "Incorrect.")
            print("################")
        cinfo(questions[2])
        q = input(green + ">> " + normal + "")
        if q == "yes" or q == "y":
            print(green + "Correct!")
            print("################")
        elif q == "no" or q == "n":
            print(red + "Incorrect.")
            print("################")
        cinfo(questions[3])
        q = input(green + ">> " + normal + "")
        if q == "yes" or q == "y":
            print(red + "Incorrect.")
            print("################")
        elif q == "no" or q == "n":
            print(green + "Correct!")
            print("################")

        # The end of the Game
        print(" ")
        print(normal + "well, looks like you've reached the end")
        time.sleep(1.5)
        os.system("cls")
        print(normal + "time to go back to menu")
        time.sleep(.7)
        home()
        rungameline()
    else:
        os.system("cls")
        cerror("Unknown Command!")
        scerror("Returning to menu, nerd.")
        time.sleep(.9)
        home()
        rungameline()


mainscript()
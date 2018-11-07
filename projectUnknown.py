'''
Created on Oct 20, 2018

@author: Jordan Deuley
'''

import random
import time
from pynput.keyboard import Key

removeLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."

docHoward = str("Unknown Man")

traitPoints = 25


def lineSkip():
    print("")


def wakeUp():
    print("Hello?")
    lineSkip()
    time.sleep(2)
    print("......")
    lineSkip()
    time.sleep(2)
    print("Wake up!")
    lineSkip()
    time.sleep(3)


def userName():
    print("About time you woke up.")
    lineSkip()
    time.sleep(2)
    playerName = input("So what is your name? ")
    if playerName == "B3T4 T3ST3R":
        print("No you can't be him/her?")
        print("You are a Beta Tester!")
        print("Here take your stuff.")
    lineSkip()
    time.sleep(1)
    print("......")
    time.sleep(1)
    lineSkip()
    print("Your name is " + playerName + "? That is an odd name.")
    time.sleep(3)
    return playerName


def createStrength():
    createStrength = input("How strong would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    if createStrength.isdigit() == True:
        while createStrength.isdigit() == True:
            if int(createStrength) > 10 or int(createStrength) < 0:
                print("ERROR 1")
                print("You used too many points")
                createStrength = input("How strong would you say you are? From a scale 1-10." + "You have " + str(traitPoints) + " trait points remaining. ")
            elif int(createStrength) <= 10 and int(createStrength) <= traitPoints:
                print("Excellent.")
                break
            elif int(createStrength) > 10 or int(createStrength) > traitPoints:
                print("You can't beat the system, try again")
                createStrength = input("How strong would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    elif createStrength.isdigit() == False:
        while createStrength.isdigit() == False:   
            print("ERROR 2")
            print("User input error.")
            createStrength = input("How strong would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
            if createStrength.isdigit() == False:
                print("You can't beat the system, try again")
                createStrength = input("How strong would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    return createStrength


def createSpeed():
    createSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    if createSpeed.isdigit() == True:
        while createSpeed.isdigit() == True:
            if int(createSpeed) > 10 or int(createSpeed) < 0:
                print("ERROR 1")
                print("You used too many points")
                createSpeed = input("How fast would you say you are? From a scale 1-10." + "You have " + str(traitPoints) + " trait points remaining. ")
            elif int(createSpeed) <= 10 and int(createSpeed) <= traitPoints:
                print("Excellent.")
                break
            elif int(createSpeed) > 10 or int(createSpeed) > traitPoints:
                print("You can't beat the system, try again")
                createSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    elif createSpeed.isdigit() == False:
        while createSpeed.isdigit() == False:   
            print("ERROR 2")
            print("User input error.")
            createSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
            if createSpeed.isdigit() == False:
                print("You can't beat the system, try again")
                createSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    return createSpeed
    

def createSmarts():
    createSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    if createSmarts.isdigit() == True:
        while createSmarts.isdigit() == True:
            if int(createSmarts) > 10 or int(createSmarts) < 0:
                print("ERROR 1")
                print("You used too many points")
                createSmarts = input("How smart would you say you are? From a scale 1-10." + "You have " + str(traitPoints) + " trait points remaining. ")
            elif int(createSmarts) <= 10 and int(createSmarts) <= traitPoints:
                print("Excellent.")
                break
            elif int(createSmarts) > 10 or int(createSmarts) > traitPoints:
                print("You can't beat the system, try again")
                createSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    elif createSmarts.isdigit() == False:
        while createSmarts.isdigit() == False:   
            print("ERROR 2")
            print("User input error.")
            createSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
            if createSmarts.isdigit() == False:
                print("You can't beat the system, try again")
                createSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    return createSmarts


def createStats():
    createStats = int(userSmarts) + int(userSpeed) + int(userStrength)
    return createStats
                        
                    
def story1A():
    print("So " + "..... " + myName + " .......")
    lineSkip()
    time.sleep(2)
    print(".....")
    time.sleep(1)
    lineSkip()
    choice1A = input(str(docHoward) + """: I should probably fill you in on some info ehh? Where should I begin?
    1. Where am I?
    2. Who are you?
    3. What is going on?"""
    )
    if choice1A == "1":
        print((str(docHoward)) + ": So, there is a lot to fill you on. As you know the United States was testing bombs, turns out the bomb there were testing was more powerful than they expected.")
        lineSkip()
        time.sleep(2)
        print((str(docHoward)) + ": As far as I know we are the only country that was damaged by this.")
        lineSkip()
        time.sleep(3)
        print((str(docHoward)) + ": I have heard of going up north or the south. I heard that it was better over there.")
        lineSkip()
        time.sleep(3)
        choice1A = input(str(docHoward) + ": Anything else you want to know?")
        if choice1A.lower == "y":
            while choice1A.lower() == "y":
                input(str(docHoward) + """: I should probably fill you in on some info ehh? Where should I begin?
                1. Where am I?
                2. Who are you?
                3. What is going on?"""
                )
        elif choice1A.lower == "n":
            while choice1A.lower() == "n":
                choice1A = input(str(docHoward) + "Are you sure, I mean you just got here?")
        
    print(str(docHoward) + ": Can you help me? Of course you will")
    

userStrength = createStrength()

print("Your Strength is " + userStrength + ".")

traitPoints = (traitPoints - int(userStrength))

print("You have " + str(traitPoints) + " remaining")

lineSkip()

userSpeed = createSpeed()

print("Your Speed is " + userSpeed + ".")

traitPoints = (traitPoints - int(userSpeed))

print("You have " + str(traitPoints) + " remaining")

lineSkip()

userSmarts = createSmarts()

print("Your Smarts is " + str(userSmarts) + ". ")

traitPoints = (traitPoints - int(userSmarts))

print("You have " + str(traitPoints) + " remaining")

lineSkip()

userStats = createStats() 

traitPointsStrength = traitPoints + int(userStrength)
traitPointsSpeed = traitPoints + int(userSpeed)
traitPointsSmarts = traitPoints + int(userSmarts)

changeStats = input("Would you like to change your stats? Type Y for yes and N for no. If you select No you cannot go back. ")
if changeStats.lower() == "y":
    while changeStats.lower() == "y":
        changeChoiceStats = input("What stat would you like to change. Please do S for Strength, A for Speed, and I for Smarts. ")
        if changeChoiceStats.lower() == "s":
            while changeChoiceStats.lower() == "s":
                userStrength = input("How strong are you? From a scale 1-10. " + str(traitPointsStrength) + " trait points remaining. ")
                if userStrength.isdigit() == True:
                    while userStrength.isdigit() == True:
                        if int(userStrength) > 10 or int(userStrength) < 0:
                            print("ERROR 1")
                            print("You used too many points")
                            userStrength = input("How strong would you say you are? From a scale 1-10." + "You have " + str(traitPointsStrength) + " trait points remaining. ")
                        elif int(userStrength) <= 10 and int(userStrength) <= traitPointsStrength:
                            print("Your new Strength is " + userStrength)
                            changeStats = input("Would you like to change another stat? Type Y for yes and N for no.")
                            if changeStats.lower() == "y":
                                changeChoiceStats = ""
                                print(changeChoiceStats)
                                break
                            elif changeStats.lower() == "n":
                                print("Okay let's get started.")
                                lineSkip()
                                time.sleep(1)
                                print("......")
                                lineSkip()            
                                break
                        elif int(userStrength) > 10 or int(userStrength) > traitPointsStrength:
                            print("You can't beat the system, try again")
                            userStrength = input("How strong would you say you are? From a scale 1-10. " + "You have " + str(traitPointsStrength) + " trait points remaining. ")
                        elif userStrength.isdigit() == False:
                            while userStrength.isdigit() == False:   
                                    print("ERROR 2")
                                    print("User input error.")
                                    userStrength = input("How strong would you say you are? From a scale 1-10. " + "You have " + str(traitPointsStrength) + " trait points remaining. ")
        elif changeChoiceStats.lower() == "a":
            while changeChoiceStats.lower() == "a":
                userSpeed = input("How fast are you? From a scale 1-10. " + str(traitPointsSpeed) + " trait points remaining. ")
                if userSpeed.isdigit() == True:
                    while userSpeed.isdigit() == True:
                        if int(userSpeed) > 10 or int(userSpeed) < 0:
                            print("ERROR 1")
                            print("You used too many points")
                            userSpeed = input("How fast would you say you are? From a scale 1-10." + "You have " + str(traitPointsSpeed) + " trait points remaining. ")
                        elif int(userSpeed) <= 10 and int(userSpeed) <= traitPointsSpeed:
                            print("Your new Speed is " + userSpeed)
                            changeStats = input("Would you like to change another stat? Type Y for yes and N for no.")
                            if changeStats.lower() == "y":
                                changeChoiceStats = input("What stat would you like to change. Please do S for Strength, A for Speed, and I for Smarts. ")
                                break
                            elif changeStats.lower() == "n":
                                print("Okay let's get started.")
                                lineSkip()
                                time.sleep(1)
                                print("......")
                                lineSkip()            
                                break
                        elif int(userSpeed) > 10 or int(userSpeed) > traitPointsSpeed:
                            print("You can't beat the system, try again")
                            userSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(traitPointsSpeed) + " trait points remaining. ")
                        elif userSpeed.isdigit() == False:
                            while userSpeed.isdigit() == False:   
                                print("ERROR 2")
                                print("User input error.")
                                userSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(traitPointsSpeed) + " trait points remaining. ")
                                if userSpeed.isdigit() == False:
                                    print("ERROR 2")
                                    print("User input error.")
                                    userSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(traitPointsSpeed) + " trait points remaining. ")    
        elif changeChoiceStats.lower() == "i":
            while changeChoiceStats.lower() == "i":
                userSmarts = input("How smart are you? From a scale 1-10. " + str(traitPointsSmarts) + " trait points remaining. ")
                if userSmarts.isdigit() == True:
                    while userSmarts.isdigit() == True:
                        if int(userSmarts) > 10 or int(userSmarts) < 0:
                            print("ERROR 1")
                            print("You used too many points")
                            userSmarts = input("How smart would you say you are? From a scale 1-10." + "You have " + str(traitPointsSmarts) + " trait points remaining. ")
                        elif int(userSmarts) <= 10 and int(userSmarts) <= traitPointsSmarts:
                            print("Your new Strength is " + userSmarts)
                            changeStats = input("Would you like to change another stat? Type Y for yes and N for no.")
                            if changeStats.lower() == "y":
                                changeChoiceStats = input("What stat would you like to change. Please do S for Strength, A for Smarts, and I for Smarts. ")
                                break
                            elif changeStats.lower() == "n":
                                print("Okay let's get started.")
                                lineSkip()
                                time.sleep(1)
                                print("......")
                                lineSkip()            
                                break
                        elif int(userSmarts) > 10 or int(userSmarts) > traitPointsSmarts:
                            print("You can't beat the system, try again")
                            userSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(traitPointsSmarts) + " trait points remaining. ")
                        elif userSmarts.isdigit() == False:
                            while userSmarts.isdigit() == False:   
                                print("ERROR 2")
                                print("User input error.")
                                userSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(traitPointsSmarts) + " trait points remaining. ")
                                if userSmarts.isdigit() == False:
                                    print("ERROR 2")
                                    print("User input error.")
                                    userSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(traitPointsSmarts) + " trait points remaining. ")
elif changeStats.lower() == "n":
            print("Okay let's get started.")
            lineSkip()
            time.sleep(1)
            print("......")
            lineSkip()
else:
    print("Uhh. Can you repeat that?")
    changeStats = input("Would you like to change your stats? Type Y for yes and N for no. If you select No you cannot go back. ")

time.sleep(1)

wakeUp()

myName = userName()

story1A()

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
'''
Created on Nov 6, 2018

@author: User
'''
import random
import time
from pynput.keyboard import Key

docHoward = str("Unknown Man")

def lineSkip():
    print("")

def userName():
    print((docHoward) + ": About time you woke up.")
    lineSkip()
    time.sleep(2)
    playerName = input((docHoward) + ": So what is your name? ")
    if playerName == "B3T4 T3ST3R":
        print((docHoward) + ": No you can't be him/her?")
        print((docHoward) + ": You are a Beta Tester!")
        print((docHoward) + ": Here take your stuff.")
    lineSkip()
    time.sleep(1)
    print((docHoward) + ": ......")
    time.sleep(1)
    lineSkip()
    print((docHoward) + ": Your name is " + playerName + "? That is an odd name.")
    time.sleep(3)
    return playerName

def story1A():
    print((docHoward) + ": So " + "..... " + myName + " .......")
    lineSkip()
    time.sleep(2)
    print((docHoward) + ": .....")
    time.sleep(1)
    lineSkip()
    choice1A = input(str(docHoward) + """: I should probably fill you in on some info ehh? Where should I begin?
    1. Where am I?
    2. Who are you?
    3. What is going on?"""
    )
    if choice1A == "1":
        print((str(docHoward)) + ": You are in the amazing state we call: Arkansas.")
        lineSkip()
        time.sleep(4)
        print((str(docHoward)) + ": We have a small little town, it does't have much. Just a market, gun store, and a couple of little houses.")
        lineSkip()
        choice1B = input(str(docHoward) + ": Anything else you want to know? \n 1. What are these shops for? \n 2. Can we talk about the other things?")
        choice1A == "stop"
        if choice1B == "1":
            print((str(docHoward)) + ": Ahh okay. We use our market place to trade important items. You can meet everyone there.")
            lineSkip()
            time.sleep(3)
            print((str(docHoward)) + ": The gun shop is run by Sheriff Banks.")
            lineSkip()
            time.sleep(2)
            lineSkip()
            time.sleep(3)
            choice1B = input(str(docHoward) + ": Anything else you want to know? \n 1. What are these shops for? \n 2. Can we talk about the other things?")
        elif choice1B == "2":
            choice1A = input(str(docHoward) + """: What else would you like to known??
            1. Where am I?
            2. Who are you?
            3. What is going on?""")
    elif choice1A == "3":
        print((str(docHoward)) + ": There was a virus that started to make people act odd. I have been researching.")
        lineSkip()
        time.sleep(2)
        print((str(docHoward)) + ": You need to be careful of these people, they may not be able to see well, but their hearing makes up for it.")
        lineSkip()
        time.sleep(3)
        print((str(docHoward)) + ": Something else I don't know if any other states, or even cities were affected.")
        lineSkip()
        time.sleep(3)
        choice1A = input(str(docHoward) + ": Anything else you want to know?")
    

myName = userName()

story1A()

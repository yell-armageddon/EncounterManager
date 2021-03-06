# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 11:01:22 2020

@author: yell
"""


import pandas as pd
import pathlib
import os
from datetime import date
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#path = pathlib.Path(__file__).parent.absolute()
path = r"F:\gits\EncounterManager"
Goals = os.path.join(path,"personal-goals.txt")
GoalsFolder = os.path.join(path, "personal-goals")


GoalsDf = pd.read_csv(Goals, header=None)



helpText = "Press h to show this message \n"
helpText=helpText + "Road Encounter: \n"
helpText=helpText + "\t dr: Draw.\n"
helpText=helpText + "\t sr: Shuffle\n"
helpText=helpText + "\t ar: Add an road encounter.\n"

helpText=helpText + "City Encounter: \n"
helpText=helpText + "\t dc: Draw.\n"
helpText=helpText + "\t sc: Shuffle\n"
helpText=helpText + "\t ac: Add an city encounter.\n"
helpText=helpText + "Press q to quit."


def initializeDeck():
    return 1

def saveGoals()):
    GoalsDf.to_csv(  Goals, header=None, index=False  )


def shuffle(df):
    return df.sample(frac=1)

def showCityImage():
    nr=str(CitiesDf.iloc[0][0])
    image = os.path.join(CityFolder, 'ce-'+nr.zfill(2)+'-f.png')
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    plt.imshow(mpimg.imread(image))
    plt.show()
    image = os.path.join(CityFolder, 'ce-'+nr.zfill(2)+'-b.png')
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    plt.imshow(mpimg.imread(image))
    plt.show()



def AskDestroyOrBottomCard(df):
    while True:
        x=input("Press (d) to destroy the card, or (b) to put to the bottom. (s) to skip")
        if x== "d":
           return df.iloc[1:]
        elif x== "b":
            return df.iloc[1:].append(df.iloc[0:1])
        elif x==  "s":
            return df
        else:
           print("Incorrect user input.")



print(helpText)
while True:
    text = input("Press a key: ")
    text = str(text)
    if text =="h":
        print(helpText)

    elif text == "sr":
        RoadsDf = shuffle(RoadsDf)
        saveRoads()
        print("Roads shuffeled.")
    elif text == "sc":
        CitiesDf = shuffle(CitiesDf)
        saveCities()
        print("Cities shuffeled.")

    elif text == "ar":
         nr=input("Enter the road encounter number to add:")
         try:
           val = int(nr)
         except ValueError:
           print("That's not an int!")
         result = addEncounter(RoadsDf,val)
         if not result is None:
             RoadsDf= result
             RoadsDf = shuffle(RoadsDf)
             saveRoads()
             print("Encounter "+nr+" has been added to the road encounter. Also shuffled & saved.")

    elif text == "sc":
        CitiesDf = shuffle(CitiesDf)
        saveCities()
        print("Cities shuffeled.")
    elif text == "ac":
         nr=input("Enter the city encounter number to add:")
         try:
           val = int(nr)
         except ValueError:
           print("That's not an int!")
         result = addEncounter(CitiesDf,val)
         if not result is None:
            CitiesDf= result
            CitiesDf = shuffle(CitiesDf)
            saveCities()
            print("Encounter "+nr+" has been added to the city encounter. Also shuffled & saved.")


    elif text == "dc":
        showCityImage()
        CitiesDf = AskDestroyOrBottomCard(CitiesDf)
        saveCities()

    elif text == "dr":
        showRoadImage()
        RoadsDf = AskDestroyOrBottomCard(RoadsDf)
        saveRoads()

    elif text == "q":
        sys.exit("Programm quit.")
    else:
        print("Incorrect user input. Press h for help.")

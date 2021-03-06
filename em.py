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
path = os.path.dirname(os.path.abspath("__file__"))
Cities = os.path.join(path,"cities.txt")
Roads =  os.path.join(path,"roads.txt")
CityFolder = os.path.join(path, "city")
RoadFolder = os.path.join(path, "road")

Goals = os.path.join(path,"personal-goals.txt")
GoalsFolder = os.path.join(path, "personal-goals")

LogFile = os.path.join(path, "log.txt")

CitiesDf = pd.read_csv(Cities, header=None)
RoadsDf = pd.read_csv(Roads, header=None)
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

helpText=helpText + "Personal Goals: \n"
helpText=helpText + "\t dg: Draw two Personal Goals.\n"
helpText=helpText + "\t sg: Shuffle\n"
helpText=helpText + "Press q to quit."

def printLog(myString):
    print(myString)
    with open(LogFile, 'a') as the_file:
        the_file.write(myString+'\n')
    

def initializeDeck():
    return 1

def saveRoads():
    RoadsDf.to_csv(  Roads, header=None, index=False  )

def saveCities():
    CitiesDf.to_csv(  Cities, header=None, index=False  )

def saveGoals():
    GoalsDf.to_csv(Goals, header=None, index=False)    

def shuffle(df):
    return df.sample(frac=1)

def addEncounter(df,num):
    if num in df.values:
        printLog("Number "+str(num)+" is already in the deck.")
    else:
        dt = pd.DataFrame(data = {int(num) })
        return df.append(dt)

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


def showRoadImage():
    nr=str(RoadsDf.iloc[0][0])
    image = os.path.join(RoadFolder, 're-'+nr.zfill(2)+'-f.png')
    img = mpimg.imread(image)

    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    plt.imshow(img)
    plt.tight_layout()
    plt.show()
    image = os.path.join(RoadFolder, 're-'+nr.zfill(2)+'-b.png')
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    plt.imshow(mpimg.imread(image))
    plt.tight_layout()
    plt.show()


def AskDestroyOrBottomCard(df):
    while True:
        x=input("Press (d) to destroy the card, or (b) to put to the bottom. (s) to skip")
        if x== "d":
           printLog("Encounter destroyed.")
           return df.iloc[1:]
        elif x== "b":
            printLog("Encounter put to bottom.")
            return df.iloc[1:].append(df.iloc[0:1])
        elif x==  "s":
            return df
        else:
           printLog("Incorrect user input.")

def showPersonalGoals():
    nr=str(GoalsDf.iloc[0][0])
    image = os.path.join(GoalsFolder, 'pg-'+nr.zfill(3)+'.png')
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
   # fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    plt.imshow(mpimg.imread(image))
    nr=str(GoalsDf.iloc[1][0])
    image = os.path.join(GoalsFolder, 'pg-'+nr.zfill(3)+'.png')
    ax2 = fig.add_subplot(1,2,2)
#    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    plt.imshow(mpimg.imread(image))
    plt.show()
    

print(helpText)
while True:
    text = input("Press a key: ")
    text = str(text)
    if text =="h":
        print(helpText)

    elif text == "sr":
        RoadsDf = shuffle(RoadsDf)
        saveRoads()
        printLog("Roads shuffeled.")
    elif text == "sc":
        CitiesDf = shuffle(CitiesDf)
        saveCities()
        printLog("Cities shuffeled.")

    elif text == "ar":
         nr=input("Enter the road encounter number to add:")
         try:
           val = int(nr)
         except ValueError:
           printLog("That's not an int!")
         result = addEncounter(RoadsDf,val)
         if not result is None:
             RoadsDf= result
             RoadsDf = shuffle(RoadsDf)
             saveRoads()
             printLog("Encounter "+nr+" has been added to the road encounter. Also shuffled & saved.")

    elif text == "sc":
        CitiesDf = shuffle(CitiesDf)
        saveCities()
        printLog("Cities shuffeled.")
    elif text == "ac":
         nr=input("Enter the city encounter number to add:")
         try:
           val = int(nr)
         except ValueError:
           printLog("That's not an int!")
         result = addEncounter(CitiesDf,val)
         if not result is None:
            CitiesDf= result
            CitiesDf = shuffle(CitiesDf)
            saveCities()
            printLog("Encounter "+nr+" has been added to the city encounter. Also shuffled & saved.")


    elif text == "dc":
        printLog("Drawing city encounter "+str(CitiesDf.iloc[0:1,0].iloc[0])+".")
        showCityImage()
        CitiesDf = AskDestroyOrBottomCard(CitiesDf)
        saveCities()

    elif text == "dr":
        printLog("Drawing road encounter "+str(RoadsDf.iloc[0:1,0].iloc[0])+".")
        showRoadImage()
        RoadsDf = AskDestroyOrBottomCard(RoadsDf)
        saveRoads()
        
    elif text=="dg":
        showPersonalGoals()
        
        ValueError = True
        while ValueError:
         nr=input("Choose first (1), second (2) or none (3) personal goal?")
         try:
           val = int(nr)
         except ValueError:
           printLog("That's not an int!")
         if val in range(1,4):
             ValueError = False
             
        if val == 1:
            printLog("Removing goal "+str(GoalsDf.iloc[0:1,0].iloc[0]) +"." )
            GoalsDf = GoalsDf.iloc[1:]
        elif val ==2:
            printLog("Removing goal "+str(GoalsDf.iloc[1:2,0].iloc[0]) +"." )
            GoalsDf = pd.concat( [ GoalsDf.iloc[0:1], GoalsDf.iloc[2:] ])
        GoalsDf= shuffle(GoalsDf)
        saveGoals()
        
        
    elif text=="sg":           
        GoalsDf= shuffle(GoalsDf)
        saveGoals()
        printLog("Goals shuffeled.")
        
    elif text == "q":
        sys.exit("Programm quit.")
    else:
        printLog("Incorrect user input. Press h for help.")

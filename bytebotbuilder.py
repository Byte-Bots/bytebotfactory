#!/usr/bin/python

# imports, yo
import os
import random
import time
import json
import math
import collections
from collections import defaultdict
from PIL import Image

# capture directory name
dirname = os.path.dirname(__file__)

# create some reference and maps to our assets and governing rules.
background = Image.open(dirname+"/art/background.png")
fullbody = Image.open(dirname+"/art/full-body.png")
accessories = [
    {"part" : (Image.open(dirname+"/art/accessories/antenna.png")), "name":"antennna", "count":0, "tier":1, "maxPercent":55},
    {"part" : (Image.open(dirname+"/art/accessories/ears.png")), "name":"ears", "count":0, "tier":2, "maxPercent":55},
    {"part" : (Image.open(dirname+"/art/accessories/tesla.png")), "name":"tesla", "count":0, "tier":3, "maxPercent":55},
    {"part" : (Image.open(dirname+"/art/accessories/helmet.png")), "name":"helmet", "count":0, "tier":4, "maxPercent":13},
    {"part" : (Image.open(dirname+"/art/accessories/hat.png")), "name":"hat", "count":0, "tier":5, "maxPercent":8},
    ]
faces = [
    {"part" : (Image.open(dirname+"/art/faces/smiley.png")), "name":"smiley", "count":0, "tier":1, "maxPercent":55},
    {"part" : (Image.open(dirname+"/art/faces/shocked.png")), "name":"shocked", "count":0, "tier":2, "maxPercent":55},
    {"part" : (Image.open(dirname+"/art/faces/angry.png")), "name":"angry", "count":0, "tier":3, "maxPercent":55},
    {"part" : (Image.open(dirname+"/art/faces/bsod.png")), "name":"bsod", "count":0, "tier":4, "maxPercent":13},
    {"part" : (Image.open(dirname+"/art/faces/matrix.png")), "name":"matrix", "count":0, "tier":5, "maxPercent":8},
    ]
locos = [
    {"part" : (Image.open(dirname+"/art/loco/legs.png")), "name":"legs", "count":0, "tier":1, "maxPercent":55},
    {"part" : (Image.open(dirname+"/art/loco/wheel.png")), "name":"wheel", "count":0, "tier":2, "maxPercent":55},
    {"part" : (Image.open(dirname+"/art/loco/spring.png")), "name":"spring", "count":0, "tier":3, "maxPercent":55},
    {"part" : (Image.open(dirname+"/art/loco/jet.png")), "name":"jet", "count":0, "tier":4, "maxPercent":13},
    {"part" : (Image.open(dirname+"/art/loco/antigrav.png")), "name":"antigrav", "count":0, "tier":4, "maxPercent":13},
    {"part" : (Image.open(dirname+"/art/loco/spider.png")), "name":"spider", "count":0, "tier":5, "maxPercent":8},
    ]

borders = [
    {"part" : (Image.open(dirname+"/art/borders/green.png")), "name":"green", "count":0, "percent":0, "valueMin": 3, "valueMax": 7, "maxPercent":55},
    {"part" : (Image.open(dirname+"/art/borders/blue.png")), "name":"blue", "count":0, "percent":0, "valueMin": 8, "valueMax": 11, "maxPercent":30},
    {"part" : (Image.open(dirname+"/art/borders/purple.png")), "name":"purple", "count":0, "percent":0, "valueMin": 12, "valueMax": 13, "maxPercent":15},
    {"part" : (Image.open(dirname+"/art/borders/orange.png")), "name":"orange", "count":0, "percent":0, "valueMin": 14, "valueMax": 15, "maxPercent":2},
    ]    

allParts = {
    "accessories" : accessories,
    "faces" : faces,
    "locos" : locos,
    "borders" : borders,
    }

# keep a manifest of everything being created.
# not used in this iteration.
manifest = []
# manifest = {}

# If I was minting programmatically, I would encode a unique message in the manifest.
# Currently unused.
uniqueMessages = {
    0 : "00000000",
    1 : "00000001",
    2 : "00000010",
    4 : "00000100",
    8 : "00001000",
    16 : "00010000",
    32 : "00100000",
    64 : "01000000",
    128 : "10000000",
    256 : "0x100",
    512 : "0x200",
    1024 : "0x300",
    2048 : "0x400",
    4092 : "0x500",
    5 : "Take the red pill.",
    7 : "Do or do not. There is no try.",
    39 : "Life... is like a grapefruit. It's orange and squishy, and has a few pips in it, and some folks have half a one for breakfast.",
    42 : '“Forty-two,” said Deep Thought, with infinite majesty and calm.',
    66 : "I felt a great disturbance in the Force, as if millions of voices suddenly cried out in terror and were suddenly silenced.",
    69 : "Nice",
    99 : "Bitches, come!",
    420 : "heh heh heh",
    666 : "Its number is six hundred and sixty six.",
    1138 : "",
    1337 : "pWn3d",
}

# Extra orange level outside the normal pattern.
oranges = {1337,2047}

# Pattern dictates how to build the rarirty of bots.
# 0 == green
# 1 == blue
# 2 == purple
# 3 == orange
pattern = [
    borders[1],
    borders[2],
    borders[1],
    borders[0],
    borders[0],
    borders[0],
    borders[0],
    borders[1],
    borders[1],
    borders[0],
    borders[0],
    borders[0],
    borders[0],
    borders[1],
    borders[2],
    borders[0],
]

timeNow = int(time.time())
print(timeNow)
randSeed = 3282021
random.seed(randSeed)
os.mkdir(dirname + "/" + str(timeNow))

# How many bots do we want to make?
maxBots = 2048

# Color to replace
bodyColor = (120, 120, 120, 255)
headColor = (188, 188, 188, 255)

builtMap = defaultdict(lambda: 0)
for i in range(0, maxBots):
    pl = len(pattern)
    trav = i % pl
    iteration = int(i / pl)
    border = {}
    if i % 64 == 0 or i in oranges:
        border = borders[3]
    elif (iteration % 2) == 0:
        border = pattern[trav]
    else:
        border = pattern[pl-1-trav]

    print(str(i) + ": "+border["name"])


    redoBot = True
    while redoBot: 
        points = 0
        randFace = random.randint(0,len(faces)-1)
        randLoco = random.randint(0,len(locos)-1)
        randAccessory = random.randint(0,len(accessories)-1)
        if not (border["name"] == "orange" or border["name"] == "purple"):
            # print(border["name"])
            fp = math.ceil((faces[randFace]["count"]+1)/maxBots*100)
            if (fp >= faces[randFace]["maxPercent"]):
                continue
            lp = math.ceil((locos[randLoco]["count"]+1)/maxBots*100)
            if (lp >= locos[randLoco]["maxPercent"]):
                continue
            ap = math.ceil((accessories[randAccessory]["count"]+1)/maxBots*100)
            if (ap >= accessories[randAccessory]["maxPercent"]):
                continue

        points += faces[randFace]["tier"]
        points += locos[randLoco]["tier"]
        points += accessories[randAccessory]["tier"]

        if border["valueMin"] <= points and border["valueMax"] >= points:
            redoBot = False

    # end while
    randSeed += 256
    random.seed(randSeed)
    bot = Image.new("RGBA", background.size)
    bot = Image.alpha_composite(bot, background)
    bot = Image.alpha_composite(bot, fullbody)
    r = random.randint(10,200)
    g = random.randint(10,200)
    b = random.randint(10,200)
    
    # I keep the two variable colors coupled together, so they are slighlty different.
    newBodyColor = (r,g,b,255)
    newFaceColor = (r+50,g+50,b+50,255)
    
    # If I want to have two completely different colors, change the face again.
    # newFaceColor = ( randint(30,200),randint(30,200),randint(30,200), 255 )
    
    # Replace base face and body color with new one.
    pixdata = bot.load()
    for y in range(bot.size[1]):
        for x in range(bot.size[0]):
            if pixdata[x, y] == bodyColor:
                pixdata[x, y] = newBodyColor
            if pixdata[x, y] == headColor:
                pixdata[x, y] = newFaceColor

    # Debug option to let me see how many duplicates exist
    # botBuild = border["name"]+"-"+faces[randFace]["name"]+"-"+locos[randLoco]["name"]+"-"+accessories[randAccessory]["name"]
    # builtMap[botBuild]+=1

    # Add new layers to the base image. 
    bot = Image.alpha_composite(bot, faces[randFace]["part"])
    bot = Image.alpha_composite(bot, locos[randLoco]["part"])
    bot = Image.alpha_composite(bot, accessories[randAccessory]["part"])
    bot = Image.alpha_composite(bot, border["part"])
    
    # Count how many times a part was used. Mostly for testing, tweaking numbers, and debugging.
    faces[randFace]["count"]+=1
    locos[randLoco]["count"]+=1
    accessories[randAccessory]["count"]+=1
    border["count"]+=1

    # Create a JSON manifest, lets us read in with minting code.
    # Not completed and not used here.
    message = uniqueMessages.get(i, "")
    manifest.append(
        { 
            "bot":i, 
            "border" : borders[border]["name"],
            "message" : message,
        })


    # Save the bot
    imagePath = dirname + '/' + str(timeNow) + '/' + str(i) + '.png'

    # Resize the bot without losing quality (since it is pixelated anyway)
    # For final production bots.
    bigBot = bot.resize((2048,2048), resample=Image.NEAREST)
    bigBot.save(imagePath)

    # For developing prior to final build, I build with the smaller size for speed.
    # bot.save(imagePath)

# Following will display information on what bots where made.
# Print amounts of each property
print("Face count")
for i in range(0, len(faces)):
    count = faces[i]["count"]
    percent = count/maxBots * 100
    percentRound = round(percent, 2)
    print(faces[i]["name"] + ": " + str(count) + " (" + str(percent) + " ~ " + str(percentRound) + "%)")   

print("Accessory count")
for i in range(0, len(accessories)):
    count = accessories[i]["count"]
    percent = count/maxBots * 100
    percentRound = round(percent, 2)
    print(accessories[i]["name"] + ": " + str(count) + " (" + str(percent) + " ~ " + str(percentRound) + "%)")   

print("Locomotion count")
for i in range(0, len(locos)):
    count = locos[i]["count"]
    percent = count/maxBots * 100
    percentRound = round(percent, 2)
    print(locos[i]["name"] + ": " + str(count) + " (" + str(percent) + " ~ " + str(percentRound) + "%)")   

print("Border count")
for i in range(0, len(borders)):
    count = borders[i]["count"]
    percent = count/maxBots * 100
    percentRound = round(percent, 2)
    print(borders[i]["name"] + ": " + str(count) + " (" + str(percent) + " ~ " + str(percentRound) + "%)")   

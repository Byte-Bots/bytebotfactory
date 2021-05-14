#!/usr/bin/python
import os
from random import *
import time
import json
import math
import collections
from collections import defaultdict

from PIL import Image
# import numpy as np

dirname = os.path.dirname(__file__)

background = Image.open(dirname+"/../art/background.png")
fullbody = Image.open(dirname+"/../art/full-body.png")
accessories = [
    {"part" : (Image.open(dirname+"/../art/accessories/antenna.png")), "name":"antennna", "count":0, "tier":1, "maxPercent":55},
    {"part" : (Image.open(dirname+"/../art/accessories/ears.png")), "name":"ears", "count":0, "tier":2, "maxPercent":55},
    {"part" : (Image.open(dirname+"/../art/accessories/tesla.png")), "name":"tesla", "count":0, "tier":3, "maxPercent":55},
    {"part" : (Image.open(dirname+"/../art/accessories/helmet.png")), "name":"helmet", "count":0, "tier":4, "maxPercent":13},
    {"part" : (Image.open(dirname+"/../art/accessories/hat.png")), "name":"hat", "count":0, "tier":5, "maxPercent":8},
    ]
faces = [
    {"part" : (Image.open(dirname+"/../art/faces/smiley.png")), "name":"smiley", "count":0, "tier":1, "maxPercent":55},
    {"part" : (Image.open(dirname+"/../art/faces/shocked.png")), "name":"shocked", "count":0, "tier":2, "maxPercent":55},
    {"part" : (Image.open(dirname+"/../art/faces/angry.png")), "name":"angry", "count":0, "tier":3, "maxPercent":55},
    {"part" : (Image.open(dirname+"/../art/faces/bsod.png")), "name":"bsod", "count":0, "tier":4, "maxPercent":13},
    {"part" : (Image.open(dirname+"/../art/faces/matrix.png")), "name":"matrix", "count":0, "tier":5, "maxPercent":8},
    ]
locos = [
    {"part" : (Image.open(dirname+"/../art/loco/legs.png")), "name":"legs", "count":0, "tier":1, "maxPercent":55},
    {"part" : (Image.open(dirname+"/../art/loco/wheel.png")), "name":"wheel", "count":0, "tier":2, "maxPercent":55},
    {"part" : (Image.open(dirname+"/../art/loco/spring.png")), "name":"spring", "count":0, "tier":3, "maxPercent":55},
    {"part" : (Image.open(dirname+"/../art/loco/jet.png")), "name":"jet", "count":0, "tier":4, "maxPercent":13},
    {"part" : (Image.open(dirname+"/../art/loco/antigrav.png")), "name":"antigrav", "count":0, "tier":4, "maxPercent":13},
    {"part" : (Image.open(dirname+"/../art/loco/spider.png")), "name":"spider", "count":0, "tier":5, "maxPercent":8},
    ]
# borders = [
#     {"part" : (Image.open(dirname+"/../art/borders/grey.png")), "name":"grey", "count":0, "percent":0 , "valueMin": 3, "valueMax": 5, "maxPercent":40},
#     {"part" : (Image.open(dirname+"/../art/borders/green.png")), "name":"green", "count":0, "percent":0, "valueMin": 6, "valueMax": 8, "maxPercent":30},
#     {"part" : (Image.open(dirname+"/../art/borders/blue.png")), "name":"blue", "count":0, "percent":0, "valueMin": 9, "valueMax": 11, "maxPercent":20},
#     {"part" : (Image.open(dirname+"/../art/borders/purple.png")), "name":"purple", "count":0, "percent":0, "valueMin": 12, "valueMax": 13, "maxPercent":8},
#     {"part" : (Image.open(dirname+"/../art/borders/orange.png")), "name":"orange", "count":0, "percent":0, "valueMin": 14, "valueMax": 15, "maxPercent":2},
#     ]

borders = [
    {"part" : (Image.open(dirname+"/../art/borders/green.png")), "name":"green", "count":0, "percent":0, "valueMin": 3, "valueMax": 7, "maxPercent":55},
    {"part" : (Image.open(dirname+"/../art/borders/blue.png")), "name":"blue", "count":0, "percent":0, "valueMin": 8, "valueMax": 11, "maxPercent":30},
    {"part" : (Image.open(dirname+"/../art/borders/purple.png")), "name":"purple", "count":0, "percent":0, "valueMin": 12, "valueMax": 13, "maxPercent":15},
    {"part" : (Image.open(dirname+"/../art/borders/orange.png")), "name":"orange", "count":0, "percent":0, "valueMin": 14, "valueMax": 15, "maxPercent":2},
    ]    

# oranges = {5,39,2047}
oranges = {1337,2047}

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
    69 : "",
    420 : "",
    666 : "",
    1138 : "",
    1337 : "",
}

borderMap = {}
for i in range(0, len(borders)):
    for k in range(borders[i]["valueMin"], borders[i]["valueMax"]+1):
        borderMap[k] = i

# print(borderMap)
# exit()
allParts = {
    "accessories" : accessories,
    "faces" : faces,
    "locos" : locos,
    "borders" : borders,
    }

manifest = []
# manifest = {}

timeNow = int(time.time())
print(timeNow)
# print(dirname)
# print(accessories[0]["name"])

# exit()
# seed(timeNow)
randSeed = 3282021
seed(randSeed)
# seed(5)
os.mkdir(dirname + "/" + str(timeNow))
# for i in range(0, 4096):
maxBots = 300
maxBots = 100
maxBots = 20
maxBots = 64
maxBots = 2048
# maxBots = 64
# maxBots = 300
# maxBots = 256

# Color to replace
bodyColor = (120, 120, 120, 255)
headColor = (188, 188, 188, 255)

builtMap = defaultdict(lambda: 0)
for i in range(0, maxBots):
    pl = len(pattern)
    trav = i % pl
    # direction = True

    iteration = int(i / pl)
    # print("iteration is: " + str(iteration))

    border = {}
    # if i in oranges:
    if i % 64 == 0 or i in oranges:
        border = borders[3]
    # elif i in oranges:
    #     border = borders[3]
    elif (iteration % 2) == 0:
        # print(str(i) + ": forward")
        border = pattern[trav]
        # print(str(i) + ": "+pattern[trav]["name"])

    else:
        border = pattern[pl-1-trav]
        # print(str(i) + ": "+pattern[pl-1-trav]["name"])
        # print(str(i) + ": back")

    print(str(i) + ": "+border["name"])

    # continue
    # dir = i % (len(pattern) * 2)
    # if direction:
    #     print(str(i) + ": "+pattern[trav]["name"])
    #     print(str(i) + ": "+str(trav))
    #     print(str(i) + ": "+str(dir))
    # if not direction:
    #     print(str(i) + ": "+pattern[pl-1-trav]["name"])
    # continue
    # exit()
    redoBot = True
    # points = 0
    while redoBot: 
        points = 0
        randFace = randint(0,len(faces)-1)
        randLoco = randint(0,len(locos)-1)
        randAccessory = randint(0,len(accessories)-1)
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
        # randBorder = randint(0,len(borders)-1)

        points += faces[randFace]["tier"]
        points += locos[randLoco]["tier"]
        points += accessories[randAccessory]["tier"]

        # if 

        # border = borderMap[points]
        if border["valueMin"] <= points and border["valueMax"] >= points:
            redoBot = False


        # count = borders[border]["count"]+1
        # percent = random((count/maxBots * 100), 2)
        # percent = math.ceil(count/maxBots * 100)
        # if (percent <= borders[border]["maxPercent"]):
            # redoBot = False
        # points += faces[randFace]["tier"])
        # if 

        # redoBot = False
    # end while
    randSeed += 256
    seed(randSeed)
    bot = Image.new("RGBA", background.size)
    bot = Image.alpha_composite(bot, background)
    bot = Image.alpha_composite(bot, fullbody)
    r = randint(10,200)
    g = randint(10,200)
    b = randint(10,200)
    newBodyColor = (r,g,b,255)
    newFaceColor = (r+50,g+50,b+50,255)
    # newFaceColor = ( randint(30,200),randint(30,200),randint(30,200), 255 )
    pixdata = bot.load()
    for y in range(bot.size[1]):
        for x in range(bot.size[0]):
            if pixdata[x, y] == bodyColor:
                pixdata[x, y] = newBodyColor
            if pixdata[x, y] == headColor:
                pixdata[x, y] = newFaceColor

    # botBuild = border["name"]+"-"+faces[randFace]["name"]+"-"+locos[randLoco]["name"]+"-"+accessories[randAccessory]["name"]+"-("+str(r)+","+str(g)+","+str(b)+")"
    botBuild = border["name"]+"-"+faces[randFace]["name"]+"-"+locos[randLoco]["name"]+"-"+accessories[randAccessory]["name"]
    builtMap[botBuild]+=1
    # print(botBuild)
    bot = Image.alpha_composite(bot, faces[randFace]["part"])
    bot = Image.alpha_composite(bot, locos[randLoco]["part"])
    bot = Image.alpha_composite(bot, accessories[randAccessory]["part"])
    bot = Image.alpha_composite(bot, border["part"])
    faces[randFace]["count"]+=1
    locos[randLoco]["count"]+=1
    accessories[randAccessory]["count"]+=1
    border["count"]+=1

    # message = uniqueMessages[i]
    message = uniqueMessages.get(i, "")
    # manifest.append(
    #     { 
    #         "bot":i, 
    #         "border" : borders[border]["name"],
    #         "message" : message,
    #     })


    # bot.show()
    # exit()
    # Save the bot
    imagePath = dirname + '/' + str(timeNow) + '/' + str(i) + '.png'
    bigBot = bot.resize((2048,2048), resample=Image.NEAREST)
    bigBot.save(imagePath)
    # bot.save(imagePath)
    # exit()
#     if (i % 64 == 0):
#         print(str(i) + ": "+borders[border]["name"])
# exit()
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

# results = json.dumps(manifest)
# print(manifest)
ordered_dict = collections.OrderedDict(sorted(builtMap.items()))
# for i in range(0, len(ordered_dict)):
    # print(ordered_dict[i])
# print(ordered_dict)
# print(sorted(builtMap))


# for key, value in ordered_dict.items():
    # print(key, ' : ', value)

#!/usr/bin/python
import os
from random import *
import time

from PIL import Image
# import numpy as np

dirname = os.path.dirname(__file__)

background = Image.open(dirname+"/../art/background.png")
fullbody = Image.open(dirname+"/../art/full-body.png")
accessories = [
    {"part" : (Image.open(dirname+"/../art/accessories/antenna.png")), "name":"antennna", "count":0},
    {"part" : (Image.open(dirname+"/../art/accessories/ears.png")), "name":"ears", "count":0},
    {"part" : (Image.open(dirname+"/../art/accessories/hat.png")), "name":"hat", "count":0},
    {"part" : (Image.open(dirname+"/../art/accessories/helmet.png")), "name":"helmet", "count":0},
    {"part" : (Image.open(dirname+"/../art/accessories/tesla.png")), "name":"tesla", "count":0},
    ]
faces = [
    {"part" : (Image.open(dirname+"/../art/faces/smiley.png")), "name":"smiley", "count":0},
    {"part" : (Image.open(dirname+"/../art/faces/shocked.png")), "name":"shocked", "count":0},
    {"part" : (Image.open(dirname+"/../art/faces/angry.png")), "name":"angry", "count":0},
    {"part" : (Image.open(dirname+"/../art/faces/bsod.png")), "name":"bsod", "count":0},
    {"part" : (Image.open(dirname+"/../art/faces/matrix.png")), "name":"matrix", "count":0},
    ]
locos = [
    {"part" : (Image.open(dirname+"/../art/loco/legs.png")), "name":"legs", "count":0},
    {"part" : (Image.open(dirname+"/../art/loco/wheel.png")), "name":"wheel", "count":0},
    {"part" : (Image.open(dirname+"/../art/loco/spring.png")), "name":"spring", "count":0},
    {"part" : (Image.open(dirname+"/../art/loco/jet.png")), "name":"jet", "count":0},
    {"part" : (Image.open(dirname+"/../art/loco/antigrav.png")), "name":"antigrav", "count":0},
    {"part" : (Image.open(dirname+"/../art/loco/spider.png")), "name":"spider", "count":0},
    ]
borders = [
    {"part" : (Image.open(dirname+"/../art/borders/grey.png")), "name":"grey", "count":0},
    {"part" : (Image.open(dirname+"/../art/borders/green.png")), "name":"green", "count":0},
    {"part" : (Image.open(dirname+"/../art/borders/blue.png")), "name":"blue", "count":0},
    {"part" : (Image.open(dirname+"/../art/borders/purple.png")), "name":"purple", "count":0},
    {"part" : (Image.open(dirname+"/../art/borders/orange.png")), "name":"orange", "count":0},
    ]

timeNow = int(time.time())
print(timeNow)
# print(dirname)
# print(accessories[0]["name"])

# exit()
seed(timeNow)
# seed(5)
os.mkdir(dirname + "/" + str(timeNow))
# for i in range(0, 4096):
maxBots = 300
maxBots = 10

bodyColor = (120, 120, 120, 255)
headColor = (188, 188, 188, 255)

for i in range(0, maxBots):
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

    # Get a random face
    randFace = randint(0,len(faces)-1)
    bot = Image.alpha_composite(bot, faces[randFace]["part"])
    faces[randFace]["count"]+=1

    # Get a random locomotion
    randLoco = randint(0,len(locos)-1)
    bot = Image.alpha_composite(bot, locos[randLoco]["part"])
    locos[randLoco]["count"]+=1

    # Get a random accessory
    randAccessory = randint(0,len(accessories)-1)
    bot = Image.alpha_composite(bot, accessories[randAccessory]["part"])
    accessories[randAccessory]["count"]+=1

    # Get a random border (for now)
    randBorder = randint(0,len(borders)-1)
    bot = Image.alpha_composite(bot, borders[randBorder]["part"])
    borders[randBorder]["count"]+=1

    # bot.show()
    # exit()
    # Save the bot
    imagePath = dirname + '/' + str(timeNow) + '/' + str(i) + '.png'
    # bigBot = bot.resize((2048,2048), resample=Image.NEAREST)
    # bigBot.save(imagePath)
    bot.save(imagePath)
    # exit()

# Print amounts of each property
print("Face count")
for i in range(0, len(faces)):
    count = faces[i]["count"]
    percent = round((count/maxBots * 100), 2)
    print(faces[i]["name"] + ": " + str(count) + " (" + str(percent) + "%)")   

print("Accessory count")
for i in range(0, len(accessories)):
    count = accessories[i]["count"]
    percent = round((count/maxBots * 100), 2)
    print(accessories[i]["name"] + ": " + str(count) + " (" + str(percent) + "%)")   

print("Locomotion count")
for i in range(0, len(locos)):
    count = locos[i]["count"]
    percent = round((count/maxBots * 100), 2)
    print(locos[i]["name"] + ": " + str(count) + " (" + str(percent) + "%)")   

print("Border count")
for i in range(0, len(borders)):
    count = borders[i]["count"]
    percent = round((count/maxBots * 100), 2)
    print(borders[i]["name"] + ": " + str(count) + " (" + str(percent) + "%)")   


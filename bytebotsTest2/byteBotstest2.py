import os
from random import *
import time

from PIL import Image
# import numpy as np

dirname = os.path.dirname(__file__)

background = Image.open("../art/background.png")
fullbody = Image.open("../art/full-body.png")
accessories = [
    (Image.open("../art/accessories/antenna.png")),
    (Image.open("../art/accessories/ears.png")),
    (Image.open("../art/accessories/hat.png")),
    (Image.open("../art/accessories/helmet.png")),
    (Image.open("../art/accessories/tesla.png")),
    ]
faces = [
    (Image.open("../art/faces/smiley.png")),
    (Image.open("../art/faces/shocked.png")),
    (Image.open("../art/faces/angry.png")),
    (Image.open("../art/faces/bsod.png")),
    (Image.open("../art/faces/matrix.png")),
    ]
locos = [
    (Image.open("../art/loco/legs.png")),
    (Image.open("../art/loco/wheel.png")),
    (Image.open("../art/loco/spring.png")),
    (Image.open("../art/loco/jet.png")),
    (Image.open("../art/loco/antigrav.png")),
    (Image.open("../art/loco/spider.png")),
    ]
borders = [
    (Image.open("../art/borders/grey.png")),
    (Image.open("../art/borders/green.png")),
    (Image.open("../art/borders/blue.png")),
    (Image.open("../art/borders/purple.png")),
    (Image.open("../art/borders/orange.png")),
    ]
test = [
    (Image.open("../art/full-body.png")),
    (Image.open("../art/full-body.png"))
]

timeNow = int(time.time())
print(timeNow)

seed(timeNow)
# seed(5)
#Open image using Image module
# fb = Image.open("../art/full-body.png")
# background = Image.open("../art/background.png")
# border = Image.open("../art/borders/blue.png")
# face = Image.open("../art/faces/matrix.png")
# loco = Image.open("../art/loco/jet.png")
# accessory = Image.open("../art/accessories/helmet.png")


bot = Image.new("RGBA", background.size)
bot = Image.alpha_composite(bot, background)
bot = Image.alpha_composite(bot, fullbody)
bot = Image.alpha_composite(bot, faces[randint(0,len(faces)-1)])
bot = Image.alpha_composite(bot, accessories[randint(0,len(accessories)-1)])
bot = Image.alpha_composite(bot, locos[randint(0,len(locos)-1)])
bot = Image.alpha_composite(bot, borders[randint(0,len(borders)-1)])
# final.show()
bot.save("bytebot-test-2-original.png")
# finalBig = final.resize((512,512), resample=Image.NEAREST)
bigBot = bot.resize((2048,2048), resample=Image.NEAREST)
# finalBig = final.resize((2048,2048))
bigBot.save("bytebot-test-2-big.png")


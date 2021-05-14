from PIL import Image
#Open image using Image module
fb = Image.open("../art/full-body.png")
background = Image.open("../art/background.png")
border = Image.open("../art/borders/blue.png")
face = Image.open("../art/faces/matrix.png")
loco = Image.open("../art/loco/jet.png")
accessory = Image.open("../art/accessories/helmet.png")


final = Image.new("RGBA", background.size)
final = Image.alpha_composite(final, background)
final = Image.alpha_composite(final, fb)
final = Image.alpha_composite(final, border)
final = Image.alpha_composite(final, face)
final = Image.alpha_composite(final, loco)
final = Image.alpha_composite(final, accessory)
final.save("bytebot-test-1-original.png")
finalBig = final.resize((2048,2048), resample=Image.NEAREST)
finalBig.save("bytebot-test-1-big.png")


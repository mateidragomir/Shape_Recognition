from PIL import Image, ImageDraw
import random

im = Image.new('RGB', (255, 255))
draw = ImageDraw.Draw(im)
random.seed()
def randShape(shape):
    draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill = 'white')
    if (shape == 3):
        draw.polygon([( random.randint(0, 255),random.randint(0, 255)), ( random.randint(0, 255),random.randint(0, 255)), ( random.randint(0, 255),random.randint(0, 255))], fill = 'black')
    elif (shape == 4):
        draw.polygon([( random.randint(0, 150),random.randint(0, 150)), ( random.randint(0, 150),random.randint(100, 255)), ( random.randint(100, 255),random.randint(100, 255)),( random.randint(100, 255),random.randint(0, 150))], fill = 'black')
    elif (shape == 5):
        draw.polygon([( random.randint(0, 120),random.randint(130, 255)), ( random.randint(130, 255),random.randint(130, 255)), ( random.randint(170, 255),random.randint(0, 120)),( random.randint(85, 170),random.randint(0, 120)),( random.randint(0, 85),random.randint(0, 120))], fill = 'black')
    else:
        print ("3, 4, or 5")

path= "C:\\python code\\shape recognition\\AI test folder\\GeneratedShape"
fileroot = "image_"

for i in range(1,501):
    randShape (shape = 3)
    filename= path +"\\training\\triangle\\"+fileroot+str(i)+".png"
    im.save(filename)
    
for i in range(1,501):
    randShape (shape = 4)
    filename= path +"\\training\\quadrilateral\\"+fileroot+str(i)+".png"
    im.save(filename)
for i in range(1,501):
    randShape (shape = 5)
    filename= path +"\\training\\pentagon\\"+fileroot+str(i)+".png"
    im.save(filename)

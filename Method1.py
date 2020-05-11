import random, PIL, os
from random import randint, choice
from PIL import Image

def makeImage(w: int=100, h: int=100):
    """Size Min: 0,0    Size Max: 16383,16383"""
    img = Image.new('RGB',(w,h))
    pixels = img.load()

def randomizePixels(redRangeStart:int=0,redRangeStop:int=255,greenRangeStart:int=0,greenRangeStop:int=255,blueRangeStart:int=0,blueRangeStop=:int=255):
    """Valid Range: 0,255"""
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixels[x,y] = (randint(redRangeStart,redRangeStop),randint(greenRangeStart,greenRangeStop),randint(blueRangeStart,blueRangeStop))

def getDesktop():
    if os.environ["ONEDRIVE"]:
        fp = f"{os.environ['ONEDRIVE']}\\Desktop"
    elif os.environ["USERPROFILE"]:
        fp = f"{os.environ['USERPROFILE']}\\Desktop"
    return fp

def saveImage(filepath=getDesktop(), name=f"{''.join(choice("abcdefABCDEF012345") for i in range(8))}", format='png'):
    """Formats: ['jpeg', 'jpg', 'png', 'tiff', 'bmp', 'raw', 'ppm', 'pgm', 'pbm', 'pnm', 'webp', 'svg', 'jfif']"""
    img.save(f"{filepath}\\{name}\\.{format}")

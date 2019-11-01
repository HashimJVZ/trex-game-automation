from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class Cordi():
    replayb=(683,187)
    dino=(171,210)
def restartgame():
    pyautogui.click(Cordi.replayb)
def space():
    pyautogui.keyDown('space')
    #    time.sleep(0.05)
    pyautogui.keyUp('space')
def image():
    box=(452,202,523,227)
    image = ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    print(a.sum())
    return (a.sum())

def main():

    restartgame()
    while True:
        if(image()!=2030):
                space()
main()
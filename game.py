from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

def restartGame():
    pyautogui.click(340, 235)  #make as per screen requirements

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump") #just to see in the log
    pyautogui.keyUp('space')

def imageGrab():
    box = (190,250,230,270)  #make as per screen requirements
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    #print(a.sum())
    return a.sum()

restartGame()
while True:
    print(imageGrab())
    if (imageGrab()!=1055):  #1055 is my value, you choose yours by noting the value when box is empty or most repeating number in the log
        pressSpace()
        time.sleep(0.1)

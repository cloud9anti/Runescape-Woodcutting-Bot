from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def drop():
    logs = None
    while logs is None:
        for logs in pyautogui.locateAllOnScreen(r'C:\Users\antic\pics\logs.png',grayscale=False, confidence = 0.75):
            pyautogui.moveTo(logs)
            pyautogui.click(button='right')
            drop = pyautogui.locateOnScreen(r'C:\Users\antic\pics\drop.png',grayscale=False)
            pyautogui.moveTo(drop)
            pyautogui.click()
            time.sleep(.1)
    cut_trees()
def cut_trees():
    print("Looking for tree")
    tree = None
    while tree is None:
        tree = pyautogui.locateOnScreen(r'C:\Users\antic\pics\tree.png',grayscale=False, confidence = 0.75)
    pyautogui.moveTo(tree)
    pyautogui.click()
        
    stump = None
    while stump is None:
        stump = pyautogui.locateOnScreen(r'C:\Users\antic\pics\stump.png',grayscale=False, confidence = 0.75)
    drop()
for i in range(100):
    cut_trees()

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def drop():
""" This function drops all of the logs in your inventory if they exist.
    Once it is finished, it calls cut_trees() """

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
""" This function tries to locate a willow tree on the screen and cut it.
    Once the tree has been cut, the drop() function is called. """

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
    #run the script 100 times.
    cut_trees()

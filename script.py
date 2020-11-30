from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)


r'''
l = None
while l is None:
    l=pyautogui.locateOnScreen(r'C:\Users\antic\pics\ball.png',grayscale=False)

r= None 
print("Looking for T")

while r is None:
    r=pyautogui.locateOnScreen(r'C:\Users\antic\pics\T.png',grayscale=False)
print("Found the T")
pyautogui.moveTo(r)
pyautogui.click()

r = None
print("Looking for start")
while r is None:
    r=pyautogui.locateOnScreen(r'C:\Users\antic\pics\start.png',grayscale=False)
print("Found the start")
pyautogui.moveTo(r)
pyautogui.click()

for i in range(100):
    pyautogui.typewrite('Spam ', interval=.0001)
    if i%10 == 0 and i!=0:
        pyautogui.typewrite('\n', interval=.0001)
'''
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

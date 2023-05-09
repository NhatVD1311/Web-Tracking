import pyautogui as pu 
import time

time.sleep(3)

for line in open("URL-list.txt", "r"):

    pu.typewrite(line)
    pu.press('Enter')

    time.sleep(30)

    pu.keyDown('ctrl')
    pu.press('f4')
    pu.keyUp('ctrl')

    pu.keyDown('ctrl')
    pu.press('t')
    pu.keyUp('ctrl')
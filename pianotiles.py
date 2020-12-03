# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:15:46 2020

@author: alessiosca
"""

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#1 X:  773 Y:  679 RGB: ( 17,  17,  17)
#2 X:  873 Y:  679 RGB: ( 17,  17,  17)
#3 X:  970 Y:  679 RGB: ( 17,  17,  17)
#4 X:  1067 Y:  679 RGB: ( 17,  17,  17)


def click_lento(x,y):
    pyautogui.click(x,y) # max click 3.606/s
    
def click_veloce(x,y): #max 4.038/s
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

        if pyautogui.pixel(719, 500)[0] == 0: # controlla se R (da RGB) è 0 --- [0] = R [1] = G [2] = B
            click_veloce(719, 500)
        if pyautogui.pixel(865, 500)[0] == 0: # controlla se R (da RGB) è 0 --- [0] = R [1] = G [2] = B
            click_veloce(865, 500)
        if pyautogui.pixel(989, 500)[0] == 0: # controlla se R (da RGB) è 0 --- [0] = R [1] = G [2] = B
            click_veloce(989, 500)
        if pyautogui.pixel(1142, 500)[0] == 0: # controlla se R (da RGB) è 0 --- [0] = R [1] = G [2] = B
            click_veloce(1142, 500)


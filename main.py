import time
import pyautogui as pg
import mss
import numpy as np
import mss.tools
import keyboard

INLG = []
def debug_color(inl):
    global INLG
    if inl == INLG:
        pass
    else:
        print(inl)
        INLG = inl

monitor = {
    "left" : 950,
    "top" : 1000,
    "width" : 1,
    "height" : 1
}
while True:
    if keyboard.is_pressed('esc'):
        break
    with mss.mss() as sct:
        img = sct.grab(monitor)
        img_array = np.array(img)
        color = [img_array[0][0][0], img_array[0][0][1], img_array[0][0][2]]
        if color == [12, 112, 222]:
            pg.press('f')
            print("f")
        elif color == [186, 131, 24]:
            pg.press('d')
            print("d")
        elif color == [21, 41, 186]:
            pg.press('j')
            print("j")
        elif color == [93, 41, 160]:
            pg.press('k')
            print("k")
        #debug_color(color)
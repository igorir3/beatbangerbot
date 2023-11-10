import time
from pynput.keyboard import Key, Controller
import mss
import mss.tools
import numpy as np
import json
import os.path

keyboard = Controller()
debug_color_bool = False

INLG = None
def debug_color(inl):
    global INLG
    if inl == INLG:
        pass
    else:
        if abs(inl[0] - inl[1]) > 10 and abs(inl[1] - inl[2]) > 10 and abs(inl[2] - inl[0]) > 10:
            print(inl)
        INLG = inl
while True:
    if not(os.path.exists("settings.json")):
        print("settings.json not found, creation...")
        classical_dict = {"monitor" : [1920, 1080], "coordinatesratio" : True, "coordinates" : [973, 920], "buttons": {"d":[164, 116, 21], "f":[10, 99, 196], "j":[19, 36, 164], "k":[82, 36, 141]}, "outputcolor" : False}
        with open("settings.json", "w+") as jsonfile:
            json.dump(classical_dict, jsonfile, sort_keys=True, indent=4)
        print("settings.json is created!")
        input("Check the settings and press Enter to continue")
    else:
        break

with open("settings.json", "r") as jsonfile:
    settdict = json.load(jsonfile)

if settdict["outputcolor"]:
    debug_color_bool = True

if settdict["coordinatesratio"] == True and settdict["monitor"] == [1920, 1080]:
    monitor = {
        "left" : 973,
        "top" : 920,
        "width" : 1,
        "height" : 1
    }
elif settdict["coordinatesratio"] == True:
    monitor = {
        "left" : settdict["monitor"][0] * (1920 / 973),
        "top" : settdict["monitor"][1] * (1080 / 920),
        "width" : 1,
        "height" : 1
    }
else:
    monitor = {
        "left" : settdict["coordinates"][0],
        "top" : settdict["coordinates"][1],
        "width" : 1,
        "height" : 1
    }

buttons = []
buttons_color = []
buttdict = settdict["buttons"]
for x in buttdict:
    buttons.append(x)
    buttons_color.append(buttdict[x])

button = None
log_buttons = ""
log_buttons_count = 0

print("Bot set up and run!")
while True:
    with mss.mss() as sct:
        img = sct.grab(monitor)
        img_array = np.array(img)
    color = [img_array[0][0][0], img_array[0][0][1], img_array[0][0][2]]
    if color in buttons_color and button == None: button = buttons[buttons_color.index(color)]
    if button != None:
        keyboard.press(button)
        time.sleep(0.05) # Если ты читаешь это, то учти что этот параметр отвечает за задержку нажатия (И да, она нужна). И ни в коем случае 
                         #не делай модификаций кода, позволяющие менять этот параметр каким либо образом, кроме открытия исходного кода
        keyboard.release(button)
        
        log_buttons = log_buttons + button
        if log_buttons_count < 25:
            print(log_buttons, end='\r')
            log_buttons_count = log_buttons_count + 1
        else:
            print(log_buttons)
            log_buttons = ""
            log_buttons_count = 0

        button = None
    if debug_color_bool == True:
        debug_color(color)
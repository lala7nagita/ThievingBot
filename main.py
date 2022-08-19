import json
import time
import secrets
from pynput.keyboard import Key, Controller

keyboard = Controller()
path = "C:/Users/Kevin/Desktop/PyBot/live_data.json"

def rng(first,second):
    options = [0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4]
    dec = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]
    return (options[secrets.randbelow(first)])+(dec[secrets.randbelow(second)])

while True:
    time.sleep(rng(6,9))
    myjson = open(path,"r")
    jsondata = myjson.read()

    try:
        objt = json.loads(jsondata)
    except json.decoder.JSONDecodeError:
        print("f")

    inv = objt['inventory']
    equip = objt['equipment']
    skills = objt['skills']

    cp = inv[0].get("index")
    neck = equip[2].get("index")
    hp = skills[5].get("boostedLevel")
    
    if hp <= 10 or neck !=2:
        keyboard.press(Key.f2)
        time.sleep(rng(6,9))
        keyboard.release(Key.f2) 
        time.sleep(10)   
    elif cp == 0:
        count = inv[0].get("amount")
        if count >= 17:
            time.sleep((rng(11,9))*6.3)
            keyboard.press(Key.f2)
            time.sleep(rng(6,9))
            keyboard.release(Key.f2)
            time.sleep(rng(11,9))
            keyboard.press(Key.f4)
            time.sleep(rng(6,9))
            keyboard.release(Key.f4)
            time.sleep(rng(11,9))
            keyboard.press(Key.f4)
            time.sleep(rng(6,9))
            keyboard.release(Key.f4)
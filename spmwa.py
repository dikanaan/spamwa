import pyautogui as gui
import random

#pesan1 = input("pesan 1 : ")
#pesan2 = input("pesan 2 : ")
#pesan3 = input("pesan 3 : ")
pesan1 = "brooooo"
pesan2 = "haduhhhhh"
pesan3 = "amsyonggg"
pesan = (pesan1,pesan2,pesan3)
jmlh = input("intr : ")

for i  in range(int(jmlh)):
    gui.typewrite(random.choice(pesan))
    gui.press('Enter')
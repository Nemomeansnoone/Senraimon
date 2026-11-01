import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import time
import random 

playername = str()
enemylist: dict[str] = ['Su-27P Flanker-B', 'MiG-29 9.12 Fulcrum-A', 'Infantry Platoon', 'AA Infantry Platoon', 'BMP-3 IFV', 'T-90M', 'Pantsir-S1', 'S-300', 'ZSU-57']
enemy1 = None
enemy2 = None
enemy3 = None
enemy1health = int(0)
enemy2health = int(0)
enemy3health = int(0)
enemy1image = None
enemy2image = None
enemy3image = None
unit1 = None
unit2 = None
unit3 = None
unit1health = int(0)
unit2health = int(0)
unit3health = int(0)
unit1image = None
unit2image = None
unit3image = None
attack1 = "brrrt"
attack2 = "brrrrrrrrrrrt"
dialogue = "salut amigos"
currentturn = "unit"
currentunitturn = "unit1"
currentunittarget = "enemy1"
prevunitturn = None
currentenemyturn = "enemy1"
currentenemytarget = None
prevenemyturn = None

def settarget1():
    global currentunittarget
    currentunittarget = "enemy1"

def settarget2():
    global currentunittarget
    currentunittarget = "enemy2"

def settarget3():
    global currentunittarget
    currentunittarget = "enemy3"

def attack():
    global currentunitturn
    global currentunittarget
    global prevunitturn
    global currentturn
    global enemy1health
    global enemy2health
    global enemy3health
    if currentunittarget == "enemy1":
        enemy1health -= int(50)
        currentturn = "enemy"
        dialoguelb = tk.Label(main_frame, text="Attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
        dialoguelb.place(x=0, y=330, width=420, height=70)
    elif currentunittarget == "enemy2":
        enemy2health -= int(50)
        currentturn = "enemy"
        dialoguelb = tk.Label(main_frame, text="Attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
        dialoguelb.place(x=0, y=330, width=420, height=70)
    elif currentunittarget == "enemy3":
        enemy3health -= int(50)
        currentturn = "enemy"
        dialoguelb = tk.Label(main_frame, text="Attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
        dialoguelb.place(x=0, y=330, width=420, height=70)
    afterturnload()

def attacke():
    global currentenemyturn
    global currentenemytarget
    global prevenemyturn
    global currentturn
    global unit1health
    global unit2health
    global unit3health
    if prevenemyturn == "enemy1":
        if currentenemytarget == "unit1":
            unit1health -= int(50)
            currentturn = "unit"
            dialoguelb = tk.Label(main_frame, text="Enemy attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
        if currentenemytarget == "unit2":
            unit2health -= int(50)
            currentturn = "unit"
            dialoguelb = tk.Label(main_frame, text="Enemy attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
        if currentenemytarget == "unit3":
            unit3health -= int(50)
            currentturn = "unit"
            dialoguelb = tk.Label(main_frame, text="Enemy attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
    elif prevenemyturn == "enemy2":
        if currentenemytarget == "unit1":
            unit1health -= int(50)
            currentturn = "unit"
            dialoguelb = tk.Label(main_frame, text="Enemy attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
        if currentenemytarget == "unit2":
            unit2health -= int(50)
            currentturn = "unit"
            dialoguelb = tk.Label(main_frame, text="Enemy attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
        if currentenemytarget == "unit3":
            unit3health -= int(50)
            currentturn = "unit"
            dialoguelb = tk.Label(main_frame, text="Enemy attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
    elif prevenemyturn == "enemy3":
        if currentenemytarget == "unit1":
            unit1health -= int(50)
            currentturn = "unit"
            dialoguelb = tk.Label(main_frame, text="Enemy attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
        if currentenemytarget == "unit2":
            unit2health -= int(50)
            currentturn = "unit"
            dialoguelb = tk.Label(main_frame, text="Enemy attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
        if currentenemytarget == "unit3":
            unit3health -= int(50)
            currentturn = "unit"
            dialoguelb = tk.Label(main_frame, text="Enemy attack hit! 50 damage dealt!", fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
    afterturnload()

def turnthing():
    global unit1
    global unit2
    global unit3
    global enemy1
    global enemy2
    global enemy3
    global currentturn
    global currentunitturn
    global currentunittarget
    global prevunitturn
    global currentenemyturn
    global currentenemytarget
    global prevenemyturn
    global attack1
    global attack2
    if currentturn == "unit":
        if currentunitturn == "unit1":
            prevunitturn = "unit1"
            currentunitturn = "unit2"
            if unit1 == "F-16CM Block 50 (Air)":
                dialoguelb = tk.Label(main_frame, text="F-16CM Block 50 (Air)'s turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon strafe", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Air to air missile", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit1 == ("F-16CM Block 50 (Ground)"):
                dialoguelb = tk.Label(main_frame, text="F-16CM Block 50 (Ground)'s turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon strafe", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="LDGP Mk 82 500lb bomb", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit1 == ("Infantry Platoon"):
                dialoguelb = tk.Label(main_frame, text="Infantry Platoon's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Rifle fire", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Grenade launcher", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit1 == ("AA Infantry Platoon"):
                dialoguelb = tk.Label(main_frame, text="AA Infantry Platoon's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Rifle fire", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Stinger MANPADS", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit1 == ("M163 VADS"):
                dialoguelb = tk.Label(main_frame, text="M163 VADS's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon burst", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="20mm cannon burst", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit1 == ("AN/TWQ-1 Avenger"):
                dialoguelb = tk.Label(main_frame, text="AN/TWQ-1 Avenger's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Stinger MANPADS", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Stinger MANPADS", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit1 == ("MIM-104 Patriot"):
                dialoguelb = tk.Label(main_frame, text="MIM-104 Patriot's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Patriot missile", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Patriot missile", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit1 == ("Dead"):
                currentunitturn = "unit2"
                turnthing()
        elif currentunitturn == "unit2":
            prevunitturn = "unit2"
            currentunitturn = "unit3"
            if unit2 == ("F-16CM Block 50 (Air)"):
                dialoguelb = tk.Label(main_frame, text="F-16CM Block 50 (Air)'s turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon strafe", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Air to air missile", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit2 == ("F-16CM Block 50 (Ground)"):
                dialoguelb = tk.Label(main_frame, text="F-16CM Block 50 (Ground)'s turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon strafe", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="LDGP Mk 82 500lb bomb", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit2 == ("Infantry Platoon"):
                dialoguelb = tk.Label(main_frame, text="Infantry Platoon's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Rifle fire", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Grenade launcher", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit2 == ("AA Infantry Platoon"):
                dialoguelb = tk.Label(main_frame, text="AA Infantry Platoon's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Rifle fire", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Stinger MANPADS", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit2 == ("M163 VADS"):
                dialoguelb = tk.Label(main_frame, text="M163 VADS's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon burst", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="20mm cannon burst", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit2 == ("AN/TWQ-1 Avenger"):
                dialoguelb = tk.Label(main_frame, text="AN/TWQ-1 Avenger's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Stinger MANPADS", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Stinger MANPADS", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit2 == ("MIM-104 Patriot"):
                dialoguelb = tk.Label(main_frame, text="MIM-104 Patriot's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Patriot missile", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Patriot missile", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit2 == ("Dead"):
                currentunitturn = "unit2"
                turnthing()
        elif currentunitturn == "unit3":
            prevunitturn = "unit3"
            currentunitturn = "unit1"
            if unit3 == ("F-16CM Block 50 (Air)"):
                dialoguelb = tk.Label(main_frame, text="F-16CM Block 50 (Air)'s turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon strafe", command=attack(), bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Air to air missile", command=attack(), bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("F-16CM Block 50 (Ground)"):
                dialoguelb = tk.Label(main_frame, text="F-16CM Block 50 (Ground)'s turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon strafe", command=attack(), bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="LDGP Mk 82 500lb bomb", command=attack(), bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("Infantry Platoon"):
                dialoguelb = tk.Label(main_frame, text="Infantry Platoon's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Rifle fire", command=attack(), bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Grenade launcher", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("AA Infantry Platoon"):
                dialoguelb = tk.Label(main_frame, text="AA Infantry Platoon's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Rifle fire", command=attack(), bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Stinger MANPADS", command=attack(), bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("M163 VADS"):
                dialoguelb = tk.Label(main_frame, text="M163 VADS's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon burst", command=attack(), bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="20mm cannon burst", command=attack(), bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("AN/TWQ-1 Avenger"):
                dialoguelb = tk.Label(main_frame, text="AN/TWQ-1 Avenger's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Stinger MANPADS", command=attack(), bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Stinger MANPADS", command=attack(), bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("MIM-104 Patriot"):
                dialoguelb = tk.Label(main_frame, text="MIM-104 Patriot's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Patriot missile", command=attack(), bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Patriot missile", command=attack(), bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("Dead"):
                currentunitturn = "unit1"
                turnthing()
    elif currentturn == "enemy":
        if currentenemyturn == "enemy1":
            prevenemyturn = "enemy1"
            currentenemyturn = "enemy2"
            currentenemytarget = "".join(random.choices(["unit1", "unit2", "unit3"]))
            if enemy1 == ("Su-27P Flanker-B"):
                enemyattackchoice = "".join(random.choices(["30mm cannon strafe", "R-73"]))
                if enemyattackchoice == ("30mm cannon strafe"):
                    attacke()
                elif enemyattackchoice == ("R-73"):
                    attacke()
            elif enemy1 == ("MiG-29 9.12 Fulcrum-A"):
                enemyattackchoice = "".join(random.choices(["30mm cannon strafe", "FAB-500M-62"]))
                if enemyattackchoice == ("30mm cannon strafe"):
                    attacke()
                elif enemyattackchoice == ("FAB-500M-62"):
                    attacke()
            elif enemy1 == ("Infantry Platoon"):
                enemyattackchoice = "".join(random.choices(["Rifle fire", "Grenade launcher"]))
                if enemyattackchoice == ("Rifle fire"):
                    attacke()
                elif enemyattackchoice == ("Grenade launcher"):
                    attacke()
            elif enemy1 == ("AA Infantry Platoon"):
                enemyattackchoice = "".join(random.choices(["Rifle fire", "9K38 Igla"]))
                if enemyattackchoice == ("Rifle fire"):
                    attacke()
                elif enemyattackchoice == ("9K38 Igla"):
                    attacke()
            elif enemy1 == ("BMP-3 IFV"):
                enemyattackchoice = "".join(random.choices(["100mm cannon", "9M133M Kornet-M"]))
                if enemyattackchoice == ("100mm cannon"):
                    attacke()
                elif enemyattackchoice == ("9M133M Kornet-M"):
                    attacke()
            elif enemy1 == ("Pantsir-S1"):
                enemyattackchoice = "".join(random.choices(["30mm cannon burst", "57E6"]))
                if enemyattackchoice == ("30mm cannon burst"):
                    attacke()
                elif enemyattackchoice == ("57E6"):
                    attacke()
            elif enemy1 == ("S-300"):
                enemyattackchoice = "9M96E1"
                attacke()
            elif enemy1 == ("ZSU-57"):
                enemyattackchoice = "57mm cannon burst"
                attacke()
            elif enemy1 == ("T-90M"):
                enemyattackchoice = "".join(random.choices(["125mm cannon", "12.7mm Kord HMG"]))
                if enemyattackchoice == ("125mm cannon"):
                    attacke()
                elif enemyattackchoice == ("12.7mm Kord HMG"):
                    attacke()
            elif enemy1 == ("Dead"):
                currentenemyturn = "enemy2"
                turnthing()
        elif currentenemyturn == "enemy2":
            prevenemyturn = "enemy2"
            currentenemyturn = "enemy3"
            currentenemytarget = "".join(random.choices(["unit1", "unit2", "unit3"]))
            if enemy2 == ("Su-27P Flanker-B"):
                enemyattackchoice = "".join(random.choices(["30mm cannon strafe", "R-73"]))
                if enemyattackchoice == ("30mm cannon strafe"):
                    attacke()
                elif enemyattackchoice == ("R-73"):
                    attacke()
            elif enemy2 == ("MiG-29 9.12 Fulcrum-A"):
                enemyattackchoice = "".join(random.choices(["30mm cannon strafe", "FAB-500M-62"]))
                if enemyattackchoice == ("30mm cannon strafe"):
                    attacke()
                elif enemyattackchoice == ("FAB-500M-62"):
                    attacke()
            elif enemy2 == ("Infantry Platoon"):
                enemyattackchoice = "".join(random.choices(["Rifle fire", "Grenade launcher"]))
                if enemyattackchoice == ("Rifle fire"):
                    attacke()
                elif enemyattackchoice == ("Grenade launcher"):
                    attacke()
            elif enemy2 == ("AA Infantry Platoon"):
                enemyattackchoice = "".join(random.choices(["Rifle fire", "9K38 Igla"]))
                if enemyattackchoice == ("Rifle fire"):
                    attacke()
                elif enemyattackchoice == ("9K38 Igla"):
                    attacke()
            elif enemy2 == ("BMP-3 IFV"):
                enemyattackchoice = "".join(random.choices(["100mm cannon", "9M133M Kornet-M"]))
                if enemyattackchoice == ("100mm cannon"):
                    attacke()
                elif enemyattackchoice == ("9M133M Kornet-M"):
                    attacke()
            elif enemy2 == ("Pantsir-S1"):
                enemyattackchoice = "".join(random.choices(["30mm cannon burst", "57E6"]))
                if enemyattackchoice == ("30mm cannon burst"):
                    attacke()
                elif enemyattackchoice == ("57E6"):
                    attacke()
            elif enemy2 == ("S-300"):
                enemyattackchoice = "9M96E1"
                attacke()
            elif enemy2 == ("ZSU-57"):
                enemyattackchoice = "57mm cannon burst"
                attacke()
            elif enemy2 == ("T-90M"):
                enemyattackchoice = "".join(random.choices(["125mm cannon", "12.7mm Kord HMG"]))
                if enemyattackchoice == ("125mm cannon"):
                    attacke()
                elif enemyattackchoice == ("12.7mm Kord HMG"):
                    attacke()
            elif enemy2 == ("Dead"):
                currentenemyturn = "enemy3"
                turnthing()
        elif currentenemyturn == "enemy3":
            prevenemyturn = "enemy3"
            currentenemyturn = "enemy1"
            currentenemytarget = "".join(random.choices(["unit1", "unit2", "unit3"]))
            if enemy3 == ("Su-27P Flanker-B"):
                enemyattackchoice = "".join(random.choices(["30mm cannon strafe", "R-73"]))
                if enemyattackchoice == ("30mm cannon strafe"):
                    attacke()
                elif enemyattackchoice == ("R-73"):
                    attacke()
            elif enemy3 == ("MiG-29 9.12 Fulcrum-A"):
                enemyattackchoice = "".join(random.choices(["30mm cannon strafe", "FAB-500M-62"]))
                if enemyattackchoice == ("30mm cannon strafe"):
                    attacke()
                elif enemyattackchoice == ("FAB-500M-62"):
                    attacke()
            elif enemy3 == ("Infantry Platoon"):
                enemyattackchoice = "".join(random.choices(["Rifle fire", "Grenade launcher"]))
                if enemyattackchoice == ("Rifle fire"):
                    attacke()
                elif enemyattackchoice == ("Grenade launcher"):
                    attacke()
            elif enemy3 == ("AA Infantry Platoon"):
                enemyattackchoice = "".join(random.choices(["Rifle fire", "9K38 Igla"]))
                if enemyattackchoice == ("Rifle fire"):
                    attacke()
                elif enemyattackchoice == ("9K38 Igla"):
                    attacke()
            elif enemy3 == ("BMP-3 IFV"):
                enemyattackchoice = "".join(random.choices(["100mm cannon", "9M133M Kornet-M"]))
                if enemyattackchoice == ("100mm cannon"):
                    attacke()
                elif enemyattackchoice == ("9M133M Kornet-M"):
                    attacke()
            elif enemy3 == ("Pantsir-S1"):
                enemyattackchoice = "".join(random.choices(["30mm cannon burst", "57E6"]))
                if enemyattackchoice == ("30mm cannon burst"):
                    attacke()
                elif enemyattackchoice == ("57E6"):
                    attacke()
            elif enemy3 == ("S-300"):
                enemyattackchoice = "9M96E1"
                attacke()
            elif enemy3 == ("ZSU-57"):
                enemyattackchoice = "57mm cannon burst"
                attacke()
            elif enemy3 == ("T-90M"):
                enemyattackchoice = "".join(random.choices(["125mm cannon", "12.7mm Kord HMG"]))
                if enemyattackchoice == ("125mm cannon"):
                    attacke()
                elif enemyattackchoice == ("12.7mm Kord HMG"):
                    attacke()
            elif enemy3 == ("Dead"):
                currentenemyturn = "enemy1"
                turnthing()

def afterturnload():
    global enemy1
    global enemy2
    global enemy3
    global enemy1health
    global enemy2health
    global enemy3health
    global enemy1image
    global enemy2image
    global enemy3image
    global unit1
    global unit2
    global unit3
    global unit1health
    global unit2health
    global unit3health
    global unit1image
    global unit2image
    global unit3image
    global dialogue
    global attack1
    global attack2
    for widget in main_frame.winfo_children():
        widget.destroy()

    line_image = ImageTk.PhotoImage(Image.open("line.png").resize((600, 20)))
    line_label = tk.Label(main_frame, image=line_image)
    line_label.image = line_image
    line_label.place(x=0, y=170, width=600, height=20)
    
    enemy1_img_obj = ImageTk.PhotoImage(Image.open(enemy1image).resize((160, 80)))
    enemy1_label = tk.Label(main_frame, image=enemy1_img_obj)
    enemy1_label.image = enemy1_img_obj
    enemy1_label.place(x=20, y=80, width=160, height=80)

    enemy2_img_obj = ImageTk.PhotoImage(Image.open(enemy2image).resize((160, 80)))
    enemy2_label = tk.Label(main_frame, image=enemy2_img_obj)
    enemy2_label.image = enemy2_img_obj
    enemy2_label.place(x=220, y=80, width=160, height=80)

    enemy3_img_obj = ImageTk.PhotoImage(Image.open(enemy3image).resize((160, 80)))
    enemy3_label = tk.Label(main_frame, image=enemy3_img_obj)
    enemy3_label.image = enemy3_img_obj
    enemy3_label.place(x=420, y=80, width=160, height=80)

    unit1_img_obj = ImageTk.PhotoImage(Image.open(unit1image).resize((160, 80)))
    unit1_label = tk.Label(main_frame, image=unit1_img_obj)
    unit1_label.image = unit1_img_obj
    unit1_label.place(x=20, y=200, width=160, height=80)

    unit2_img_obj = ImageTk.PhotoImage(Image.open(unit2image).resize((160, 80)))
    unit2_label = tk.Label(main_frame, image=unit2_img_obj)
    unit2_label.image = unit2_img_obj
    unit2_label.place(x=220, y=200, width=160, height=80)

    unit3_img_obj = ImageTk.PhotoImage(Image.open(unit3image).resize((160, 80)))
    unit3_label = tk.Label(main_frame, image=unit3_img_obj)
    unit3_label.image = unit3_img_obj
    unit3_label.place(x=420, y=200, width=160, height=80)

    enemy1btn = tk.Button(main_frame, text=f'{enemy1}', fg="#1e1e1e", bg="#ffffff", command=settarget1)
    enemy1btn.place(x=20, y=30, width=160, height=20)

    enemy2btn = tk.Button(main_frame, text=f'{enemy2}', fg="#1e1e1e", bg="#ffffff", command=settarget2)
    enemy2btn.place(x=220, y=30, width=160, height=20)

    enemy3btn = tk.Button(main_frame, text=f'{enemy3}', fg="#1e1e1e", bg="#ffffff", command=settarget3)
    enemy3btn.place(x=420, y=30, width=160, height=20)

    enemy1healthlab = tk.Label(main_frame, text=f'{enemy1health}', fg="#ffffff")
    enemy1healthlab.place(x=20, y=60, width=160, height=20)

    enemy2healthlab = tk.Label(main_frame, text=f'{enemy2health}', fg="#ffffff")
    enemy2healthlab.place(x=220, y=60, width=160, height=20)

    enemy3healthlab = tk.Label(main_frame, text=f'{enemy3health}', fg="#ffffff")
    enemy3healthlab.place(x=420, y=60, width=160, height=20)

    unit1lab = tk.Label(main_frame, text=f'{unit1}', fg="#ffffff")
    unit1lab.place (x=20, y=310, width=160, height=20)

    unit2lab = tk.Label(main_frame, text=f'{unit2}', fg="#ffffff")
    unit2lab.place(x=220, y=310, width=160, height=20)

    unit3lab = tk.Label(main_frame, text=f'{unit3}', fg="#ffffff")
    unit3lab.place(x=420, y=310, width=160, height=20)

    unit1healthlab = tk.Label(main_frame, text=f'{unit1health}', fg="#ffffff")
    unit1healthlab.place(x=20, y=280, width=160, height=20)

    unit2healthlab = tk.Label(main_frame, text=f'{unit2health}', fg="#ffffff")
    unit2healthlab.place(x=220, y=280, width=160, height=20)

    unit3healthlab = tk.Label(main_frame, text=f'{unit3health}', fg="#ffffff")
    unit3healthlab.place(x=420, y=280, width=160, height=20)

    blankspacething = tk.Label(main_frame, text="", bg="#ffffff")
    blankspacething.place(x=420, y=330, width=180, height=70)

    enemytext = tk.Label(main_frame, text="Enemy", fg="#1e1e1e", bg="#ffffff")
    enemytext.place(x=220, y=0, width=160, height=20)

    turnthing()

def startload():
    global enemy1
    global enemy2
    global enemy3
    global enemy1health
    global enemy2health
    global enemy3health
    global enemy1image
    global enemy2image
    global enemy3image
    global unit1
    global unit2
    global unit3
    global unit1health
    global unit2health
    global unit3health
    global unit1image
    global unit2image
    global unit3image
    global dialogue
    global attack1
    global attack2
    for widget in main_frame.winfo_children():
        widget.destroy()

    line_image = ImageTk.PhotoImage(Image.open("line.png").resize((600, 20)))
    line_label = tk.Label(main_frame, image=line_image)
    line_label.image = line_image
    line_label.place(x=0, y=170, width=600, height=20)
    
    enemy1_img_obj = ImageTk.PhotoImage(Image.open(enemy1image).resize((160, 80)))
    enemy1_label = tk.Label(main_frame, image=enemy1_img_obj)
    enemy1_label.image = enemy1_img_obj
    enemy1_label.place(x=20, y=80, width=160, height=80)

    enemy2_img_obj = ImageTk.PhotoImage(Image.open(enemy2image).resize((160, 80)))
    enemy2_label = tk.Label(main_frame, image=enemy2_img_obj)
    enemy2_label.image = enemy2_img_obj
    enemy2_label.place(x=220, y=80, width=160, height=80)

    enemy3_img_obj = ImageTk.PhotoImage(Image.open(enemy3image).resize((160, 80)))
    enemy3_label = tk.Label(main_frame, image=enemy3_img_obj)
    enemy3_label.image = enemy3_img_obj
    enemy3_label.place(x=420, y=80, width=160, height=80)

    unit1_img_obj = ImageTk.PhotoImage(Image.open(unit1image).resize((160, 80)))
    unit1_label = tk.Label(main_frame, image=unit1_img_obj)
    unit1_label.image = unit1_img_obj
    unit1_label.place(x=20, y=200, width=160, height=80)

    unit2_img_obj = ImageTk.PhotoImage(Image.open(unit2image).resize((160, 80)))
    unit2_label = tk.Label(main_frame, image=unit2_img_obj)
    unit2_label.image = unit2_img_obj
    unit2_label.place(x=220, y=200, width=160, height=80)

    unit3_img_obj = ImageTk.PhotoImage(Image.open(unit3image).resize((160, 80)))
    unit3_label = tk.Label(main_frame, image=unit3_img_obj)
    unit3_label.image = unit3_img_obj
    unit3_label.place(x=420, y=200, width=160, height=80)

    enemy1btn = tk.Button(main_frame, text=f'{enemy1}', fg="#1e1e1e", bg="#ffffff", command=settarget1)
    enemy1btn.place(x=20, y=30, width=160, height=20)

    enemy2btn = tk.Button(main_frame, text=f'{enemy2}', fg="#1e1e1e", bg="#ffffff", command=settarget2)
    enemy2btn.place(x=220, y=30, width=160, height=20)

    enemy3btn = tk.Button(main_frame, text=f'{enemy3}', fg="#1e1e1e", bg="#ffffff", command=settarget3)
    enemy3btn.place(x=420, y=30, width=160, height=20)

    enemy1healthlab = tk.Label(main_frame, text=f'{enemy1health}', fg="#ffffff")
    enemy1healthlab.place(x=20, y=60, width=160, height=20)

    enemy2healthlab = tk.Label(main_frame, text=f'{enemy2health}', fg="#ffffff")
    enemy2healthlab.place(x=220, y=60, width=160, height=20)

    enemy3healthlab = tk.Label(main_frame, text=f'{enemy3health}', fg="#ffffff")
    enemy3healthlab.place(x=420, y=60, width=160, height=20)

    unit1lab = tk.Label(main_frame, text=f'{unit1}', fg="#ffffff")
    unit1lab.place (x=20, y=310, width=160, height=20)

    unit2lab = tk.Label(main_frame, text=f'{unit2}', fg="#ffffff")
    unit2lab.place(x=220, y=310, width=160, height=20)

    unit3lab = tk.Label(main_frame, text=f'{unit3}', fg="#ffffff")
    unit3lab.place(x=420, y=310, width=160, height=20)

    unit1healthlab = tk.Label(main_frame, text=f'{unit1health}', fg="#ffffff")
    unit1healthlab.place(x=20, y=280, width=160, height=20)

    unit2healthlab = tk.Label(main_frame, text=f'{unit2health}', fg="#ffffff")
    unit2healthlab.place(x=220, y=280, width=160, height=20)

    unit3healthlab = tk.Label(main_frame, text=f'{unit3health}', fg="#ffffff")
    unit3healthlab.place(x=420, y=280, width=160, height=20)

    blankspacething = tk.Label(main_frame, text="", bg="#ffffff")
    blankspacething.place(x=420, y=330, width=180, height=70)

    enemytext = tk.Label(main_frame, text="Enemy", fg="#1e1e1e", bg="#ffffff")
    enemytext.place(x=220, y=0, width=160, height=20)

    turnthing()

    


    
def startprep():
    global enemy1
    global enemy2
    global enemy3
    global enemy1health
    global enemy2health
    global enemy3health
    global enemy1image
    global enemy2image
    global enemy3image
    global unit1
    global unit2
    global unit3
    global unit1health
    global unit2health
    global unit3health
    global unit1image
    global unit2image
    global unit3image

    enemy1 = random.choice(enemylist)
    if enemy1 == ("Su-27P Flanker-B"):
        enemy1health = int(200)
        enemy1image = "su-27.png"
    elif enemy1 == ("MiG-29 9.12 Fulcrum-A"):
        enemy1health = int(200)
        enemy1image = "mig-29.png"
    elif enemy1 == ("Infantry Platoon"):
        enemy1health = int(150)
        enemy1image = "infantry_e.png"
    elif enemy1 == ("AA Infantry Platoon"):
        enemy1health = int(150)
        enemy1image = ("aa_infantry_e.png")
    elif enemy1 == ("BMP-3 IFV"):
        enemy1health = int(250)
        enemy1image = "bmp-3.png"
    elif enemy1 == ("Pantsir-S1"):
        enemy1health = int(250)
        enemy1image = "pantsir.png"
    elif enemy1 == ("S-300"):
        enemy1health = int(250)
        enemy1image = "s-300.png"
    elif enemy1 == ("ZSU-57"):
        enemy1health = int(250)
        enemy1image = "zsu-57.png"
    elif enemy1 == ("T-90M"):
        enemy1health = int(400)
        enemy1image = "t-90m.png"
    enemy2 = random.choice(enemylist)
    if enemy2 == ("Su-27P Flanker-B"):
        enemy2health = int(200)
        enemy2image = "su-27.png"
    elif enemy2 == ("MiG-29 9.12 Fulcrum-A"):
        enemy2health = int(200)
        enemy2image = "mig-29.png"
    elif enemy2 == ("Infantry Platoon"):
        enemy2health = int(150)
        enemy2image = "infantry_e.png"
    elif enemy2 == ("AA Infantry Platoon"):
        enemy2health = int(150)
        enemy2image = ("aa_infantry_e.png")
    elif enemy2 == ("BMP-3 IFV"):
        enemy2health = int(250)
        enemy2image = "bmp-3.png"
    elif enemy2 == ("Pantsir-S1"):
        enemy2health = int(250)
        enemy2image = "pantsir.png"
    elif enemy2 == ("S-300"):
        enemy2health = int(250)
        enemy2image = "s-300.png"
    elif enemy2 == ("ZSU-57"):
        enemy2health = int(250)
        enemy2image = "zsu-57.png"
    elif enemy2 == ("T-90M"):
        enemy2health = int(400)
        enemy2image = "t-90m.png"
    enemy3 = random.choice(enemylist)
    if enemy3 == ("Su-27P Flanker-B"):
        enemy3health = int(200)
        enemy3image = "su-27.png"
    elif enemy3 == ("MiG-29 9.12 Fulcrum-A"):
        enemy3health = int(200)
        enemy3image = "mig-29.png"
    elif enemy3 == ("Infantry Platoon"):
        enemy3health = int(150)
        enemy3image = "infantry_e.png"
    elif enemy3 == ("AA Infantry Platoon"):
        enemy3health = int(150)
        enemy3image = ("aa_infantry_e.png")
    elif enemy3 == ("BMP-3 IFV"):
        enemy3health = int(250)
        enemy3image = "bmp-3.png"
    elif enemy3 == ("Pantsir-S1"):
        enemy3health = int(250)
        enemy3image = "pantsir.png"
    elif enemy3 == ("S-300"):
        enemy3health = int(250)
        enemy3image = "s-300.png"
    elif enemy3 == ("ZSU-57"):
        enemy3health = int(250)
        enemy3image = "zsu-57.png"
    elif enemy3 == ("T-90M"):
        enemy3health = int(400)
        enemy3image = "t-90m.png"

    unit1 = selectedunit1.get().strip()
    unit2 = selectedunit2.get().strip()
    unit3 = selectedunit3.get().strip()

    if unit1 == ("F-16CM Block 50 (Air)"):
        unit1health = int(200)
        unit1image = "f-16_a.png"
    elif unit1 == ("F-16CM Block 50 (Ground)"):
        unit1health = int(200)
        unit1image = "f-16_g.png"
    elif unit1 == ("Infantry Platoon"):
        unit1health = int(150)
        unit1image = "infantry_u.png"
    elif unit1 == ("AA Infantry Platoon"):
        unit1health = int(150)
        unit1image = "aa_infantry_u.png"
    elif unit1 == ("M163 VADS"):
        unit1health = int(250)
        unit1image = "m163.png"
    elif unit1 == ("AN/TWQ-1 Avenger"):
        unit1health = int(250)
        unit1image = "avenger.png"
    elif unit1 == ("MIM-104 Patriot"):
        unit1health = int(250)
        unit1image = "patriot.png"

    if unit2 == ("F-16CM Block 50 (Air)"):
        unit2health = int(200)
        unit2image = "f-16_a.png"
    elif unit2 == ("F-16CM Block 50 (Ground)"):
        unit2health = int(200)
        unit2image = "f-16_g.png"
    elif unit2 == ("Infantry Platoon"):
        unit2health = int(150)
        unit2image = "infantry_u.png"
    elif unit2 == ("AA Infantry Platoon"):
        unit2health = int(150)
        unit2image = "aa_infantry_u.png"
    elif unit2 == ("M163 VADS"):
        unit2health = int(250)
        unit2image = "m163.png"
    elif unit2 == ("AN/TWQ-1 Avenger"):
        unit2health = int(250)
        unit2image = "avenger.png"
    elif unit2 == ("MIM-104 Patriot"):
        unit2health = int(250)
        unit2image = "patriot.png"

    if unit3 == ("F-16CM Block 50 (Air)"):
        unit3health = int(200)
        unit3image = "f-16_a.png"
    elif unit3 == ("F-16CM Block 50 (Ground)"):
        unit3health = int(200)
        unit3image = "f-16_g.png"
    elif unit3 == ("Infantry Platoon"):
        unit3health = int(150)
        unit3image = "infantry_u.png"
    elif unit3 == ("AA Infantry Platoon"):
        unit3health = int(150)
        unit3image = "aa_infantry_u.png"
    elif unit3 == ("M163 VADS"):
        unit3health = int(250)
        unit3image = "m163.png"
    elif unit3 == ("AN/TWQ-1 Avenger"):
        unit3health = int(250)
        unit3image = "avenger.png"
    elif unit3 == ("MIM-104 Patriot"):
        unit3health = int(250)
        unit3image = "patriot.png"

    startload()



def pickunits():
    global playername
    global selectedunit1
    global selectedunit2
    global selectedunit3
    playername = txt_entry.get().strip()
    if not playername.strip():
        playername = "Commander"
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text = f'Welcome, {playername}!', font=("Arial", 14, "bold"), fg="white", bg="#1e1e1e").pack(pady=5)
    tk.Label(main_frame, text = "Please pick your units", font=("Arial", 11, "bold"), fg="white", bg="#1e1e1e").pack(pady=5)

    unit_options = [
        "F-16CM Block 50 (Air)",
        "F-16CM Block 50 (Ground)",
        "Infantry Platoon",
        "AA Infantry Platoon",
        "M163 VADS",
        "AN/TWQ-1 Avenger",
        "MIM-104 Patriot"
    ]

    tk.Label(main_frame, text = "Unit 1").pack()
    selectedunit1 = ttk.Combobox(main_frame, values=unit_options, width=40, state="readonly")
    selectedunit1.pack()
    selectedunit1.set("Infantry Platoon")

    tk.Label(main_frame, text = "Unit 2").pack()
    selectedunit2 = ttk.Combobox(main_frame, values=unit_options, width=40, state="readonly")
    selectedunit2.pack()
    selectedunit2.set("Infantry Platoon")

    tk.Label(main_frame, text = "Unit 3").pack()
    selectedunit3 = ttk.Combobox(main_frame, values=unit_options, width=40, state="readonly")
    selectedunit3.pack()
    selectedunit3.set("Infantry Platoon")

    tk.Button(main_frame, text = "Start battle", fg = "blue", command=startprep, font=("Arial", 11, "bold")).pack(pady=15)


def intro():
    global txt_entry
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text = "Senraimon: Pokemon battles but its war thunder", font =("Arial", 14, "bold")).pack(pady=10)
    tk.Label(main_frame, text = "Please enter your name", font=("Arial", 12)).pack(pady=5)
    txt_entry = tk.Entry(main_frame, width = 24, font=("Arial", 12), fg="#1e1e1e", bg="white")
    txt_entry.pack(pady=10)
    tk.Button(main_frame, text = "Start" , fg = "blue", font=("Arial", 11, "bold"), width=10, command=pickunits).pack(pady=10)

root = tk.Tk()
root.geometry("600x400")
root.configure(bg="#1e1e1e")
root.title("Senraimon")
main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(fill="both", expand = True)

intro()
root.mainloop()

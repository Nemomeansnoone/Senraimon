import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import time
import random 
import assignunits
import assignenemy

playername = str()
enemylist: dict[str] = ['Su-27P Flanker-B', 'MiG-29 9.12 Fulcrum-A', 'Infantry Platoon', 'AA Infantry Platoon', 'BMP-3', 'T-90M', 'Pantsir-S1', 'S-300', 'ZSU-57']
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
u1a1 = None
u1a2 = None
u2a1 = None
u2a2 = None
u3a1 = None
u3a2 = None
e1a1 = None
e1a2 = None
e2a1 = None
e2a2 = None
e3a1 = None
e3a2 = None
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

def winorlose():
    for widget in main_frame.winfo_children():
        widget.destroy()
    if enemy1 == "Dead" and enemy2 == "Dead" and enemy3 == "Dead":
        wintext = tk.Label(main_frame, text="Congrats, you win!", fg="#ffffff", bg="#1e1e1e")
        wintext.place(x=0, y=20, width=600, height=230)
        winrestartbutton = tk.Button(main_frame, text="Restart", command=intro, fg="#1e1e1e", bg="#ffffff")
        winrestartbutton.place(x=252, y=234, width=96, height=32)
    elif unit1 == "Dead" and unit2 == "Dead" and unit3 == "Dead":
        losetext = tk.Label(main_frame, text="You lost!", fg="#ffffff", bg="#1e1e1e")
        losetext.place(x=0, y=20, width=600, height=230)
        loserestartbutton = tk.Button(main_frame, text="Restart", command=intro, fg="#1e1e1e", bg="#ffffff")
        loserestartbutton.place(x=252, y=234, width=96, height=32)
    else:
        afterturnload()

def checkfordead():
    global unit1
    global unit2
    global unit3
    global unit1health
    global unit2health
    global unit3health
    global enemy1
    global enemy2
    global enemy3
    global enemy1health
    global enemy2health
    global enemy3health
    if unit1health <= 0 or unit1health == 0:
        unit1health = 0
        unit1 = "Dead"
    if unit2health <= 0 or unit2health == 0:
        unit2health = 0
        unit2 = "Dead"
    if unit3health <= 0 or unit3health == 0:
        unit3health = 0
        unit3 = "Dead"
    if enemy1health <= 0 or enemy1health == 0:
        enemy1health = 0
        enemy1 = "Dead"
    if enemy2health <= 0 or enemy2health == 0:
        enemy2health = 0
        enemy2 = "Dead"
    if enemy3health <= 0 or enemy3health == 0:
        enemy3health = 0
        enemy3 = "Dead"
    winorlose()

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
    root.update()
    time.sleep(3)
    checkfordead()

def attacke():
    global currentenemyturn
    global currentenemytarget
    global prevenemyturn
    global currentturn
    global unit1health
    global unit2health
    global unit3health
    if prevenemyturn == "enemy1":
        dialoguelb = tk.Label(main_frame, text=f"{unit1}'s turn:", fg="#1e1e1e", bg="#ffffff")
        main_frame.update()
        time.sleep(2)
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
        dialoguelb = tk.Label(main_frame, text=f"{unit2}'s turn:", fg="#1e1e1e", bg="#ffffff")
        root.update()
        time.sleep(2)
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
        dialoguelb = tk.Label(main_frame, text=f"{unit3}'s turn:", fg="#1e1e1e", bg="#ffffff")
        root.update()
        time.sleep(2)
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
    root.update()
    time.sleep(3)
    checkfordead()

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
                attack1button = tk.Button(main_frame, text="20mm cannon strafe", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Air to air missile", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("F-16CM Block 50 (Ground)"):
                dialoguelb = tk.Label(main_frame, text="F-16CM Block 50 (Ground)'s turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon strafe", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="LDGP Mk 82 500lb bomb", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("Infantry Platoon"):
                dialoguelb = tk.Label(main_frame, text="Infantry Platoon's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Rifle fire", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Grenade launcher", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("AA Infantry Platoon"):
                dialoguelb = tk.Label(main_frame, text="AA Infantry Platoon's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Rifle fire", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Stinger MANPADS", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("M163 VADS"):
                dialoguelb = tk.Label(main_frame, text="M163 VADS's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="20mm cannon burst", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="20mm cannon burst", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("AN/TWQ-1 Avenger"):
                dialoguelb = tk.Label(main_frame, text="AN/TWQ-1 Avenger's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Stinger MANPADS", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Stinger MANPADS", command=attack, bg="#1e1e1e")
                attack2button.place(x=440, y=360, width=140, height=30)
            elif unit3 == ("MIM-104 Patriot"):
                dialoguelb = tk.Label(main_frame, text="MIM-104 Patriot's turn:", fg="#1e1e1e", bg="#ffffff")
                dialoguelb.place(x=0, y=330, width=420, height=70)
                attack1button = tk.Button(main_frame, text="Patriot missile", command=attack, bg="#1e1e1e")
                attack1button.place(x=440, y=330, width=140, height=30)
                attack2button = tk.Button(main_frame, text="Patriot missile", command=attack, bg="#1e1e1e")
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
            elif enemy1 == ("BMP-3"):
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
            elif enemy2 == ("BMP-3"):
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
            elif enemy3 == ("BMP-3"):
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
    global currentturn
    global currentunitturn
    global currentunittarget
    global currentenemyturn
    global u1a1
    global u1a2
    global u2a1
    global u2a2
    global u3a1
    global u3a2
    global e1a1
    global e1a2
    global e2a1
    global e2a2
    global e3a1
    global e3a2

    enemy1, enemy1health, enemy1image, e1a1, e1a2 = assignenemy.assign()
    enemy2, enemy2health, enemy2image, e2a1, e2a2 = assignenemy.assign()
    enemy3, enemy3health, enemy3image, e3a1, e3a2 = assignenemy.assign()

    unit1 = selectedunit1.get().strip()
    unit2 = selectedunit2.get().strip()
    unit3 = selectedunit3.get().strip()

    unit1health, unit1image, u1a1, u1a2 = assignunits.assignunit1(unit1)
    unit2health, unit2image, u2a1, u2a2 = assignunits.assignunit2(unit2)
    unit3health, unit3image, u3a1, u3a2 = assignunits.assignunit3(unit3)

    currentturn = "unit"
    currentunitturn = "unit1"
    currentenemyturn = "enemy1"
    currentunittarget = "enemy1"
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

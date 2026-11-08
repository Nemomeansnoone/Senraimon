import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import time
import random 
from scripts import assignunits
from scripts import assignenemy
from scripts import unitattack
from scripts import enemyattack
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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
enemy1imagesub = None
enemy2imagesub = None
enemy3imagesub = None
unit1 = None
unit2 = None
unit3 = None
unit1health = int(0)
unit2health = int(0)
unit3health = int(0)
unit1image = None
unit2image = None
unit3image = None
unit1imagesub = None
unit2imagesub = None
unit3imagesub = None
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
u1a1t = None
u1a2t = None
u2a1t = None
u2a2t = None
u3a1t = None
u3a2t = None
e1a1t = None
e1a2t = None
e2a1t = None
e2a2t = None
e3a1t = None
e3a2t = None
attack1 = "brrrt"
attack2 = "brrrrrrrrrrrt"
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

def attacknew(target, attackname):
    global unit1
    global unit2
    global unit3
    global enemy1
    global enemy2
    global enemy3
    global enemy1health
    global enemy2health
    global enemy3health
    global currentturn
    global currentunitturn
    global currentunittarget
    global prevunitturn
    global currentenemyturn
    global currentenemytarget
    global prevenemyturn
    global dialogue
    if globals()[prevunitturn] == "Dead":
        if prevunitturn == "unit1":
            currentunitturn = "unit2"
            currentturn = "unit"
            turnthing()
        elif prevunitturn == "unit2":
            currentunitturn == "unit3"
            currentturn = "unit"
            turnthing()
        elif prevunitturn == "unit3":
            currentunitturn == "unit1"
            currentturn = "unit"
            turnthing()
    else:
        damage = unitattack.attack(globals()[target], attackname)
        if damage == 0:
            dialogue.set("Attack missed! No damage dealt!")
            dialoguelb = tk.Label(main_frame, text=dialogue.get(), fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
        elif damage > 0:
            dialogue.set(f"{globals()[prevunitturn]}'s attack hit! {damage} damage dealt to {globals()[currentunittarget]}!")
            dialoguelb = tk.Label(main_frame, text=dialogue.get(), fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
            if currentunittarget == "enemy1":
                enemy1health -= int(damage)
            elif currentunittarget == "enemy2":
                enemy2health -= int(damage)
            elif currentunittarget == "enemy3":
                enemy3health -= int(damage)
        root.update()
        time.sleep(3)
        checkfordead()

def attackenew(target, attackname):
    global unit1
    global unit2
    global unit3
    global enemy1
    global enemy2
    global enemy3
    global unit1health
    global unit2health
    global unit3health
    global currentturn
    global currentunitturn
    global currentunittarget
    global prevunitturn
    global currentenemyturn
    global currentenemytarget
    global prevenemyturn
    global dialogue
    if globals()[prevenemyturn] == "Dead":
        if prevenemyturn == "enemy1":
            currentenemyturn = "enemy2"
            currentturn = "enemy"
            turnthing()
        elif prevenemyturn == "enemy2":
            currentenemyturn = "enemy3"
            currentturn = "enemy"
            turnthing()
        elif prevenemyturn == "enemy3":
            currentenemyturn = "enemy1"
            currentturn = "enemy"
            turnthing()
    else:
        damage = enemyattack.attack(target, attackname)
        if damage == 0:
            dialogue.set("Attack missed! No damage dealt")
            dialoguelb = tk.Label(main_frame, text=dialogue.get(), fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
        elif damage > 0:
            dialogue.set(f"{globals()[prevenemyturn]}'s attack hit! {damage} dealt to {globals()[currentenemytarget]}!")
            dialoguelb = tk.Label(main_frame, text=dialogue.get(), fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
            if currentenemytarget == "unit1":
                unit1health -= int(damage)
            elif currentenemytarget == "unit2":
                unit2health -= int(damage)
            elif currentenemytarget == "unit3":
                unit3health -= int(damage)
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
    global u1a1t
    global u1a2t
    global u2a1t
    global u2a2t
    global u3a1t
    global u3a2t
    global e1a1t
    global e1a2t
    global e2a1t
    global e2a2t
    global e3a1t
    global e3a2t
    global dialogue

    if currentturn == "unit":
        currentturn = "enemy"
        if currentunitturn == "unit1" and unit1 != "Dead":
            prevunitturn = "unit1"
            currentunitturn = "unit2"
            dialogue.set(f"{unit1}'s turn:")
            dialoguelb = tk.Label(main_frame, text=dialogue.get(), fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
            attack1button = tk.Button(main_frame, text=u1a1t, command=lambda: attacknew(currentunittarget, u1a1))
            attack1button.place(x=440, y=330, width=140, height=30)
            attack2button = tk.Button(main_frame, text=u1a2t, command=lambda: attacknew(currentunittarget, u1a2))
            attack2button.place(x=440, y=360, width=140, height=30)
        elif currentunitturn == "unit2" and unit2 != "Dead":
            prevunitturn = "unit2"
            currentunitturn = "unit3"
            dialogue.set(f"{unit2}'s turn:")
            dialoguelb = tk.Label(main_frame, text=dialogue.get(), fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
            attack1button = tk.Button(main_frame, text=u2a1t, command=lambda: attacknew(currentunittarget, u2a1))
            attack1button.place(x=440, y=330, width=140, height=30)
            attack2button = tk.Button(main_frame, text=u2a2t, command=lambda: attacknew(currentunittarget, u2a2))
            attack2button.place(x=440, y=360, width=140, height=30)
        elif currentunitturn == "unit3" and unit3 != "Dead":
            prevunitturn = "unit3"
            currentunitturn = "unit1"
            dialogue.set(f"{unit3}'s turn:")
            dialoguelb = tk.Label(main_frame, text=dialogue.get(), fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
            attack1button = tk.Button(main_frame, text=u3a1t, command=lambda: attacknew(currentunittarget, u3a1))
            attack1button.place(x=440, y=330, width=140, height=30)
            attack2button = tk.Button(main_frame, text=u3a2t, command=lambda: attacknew(currentunittarget, u3a2))
            attack2button.place(x=440, y=360, width=140, height=30)
        elif currentunitturn == "unit1" and unit1 == "Dead":
            currentturn = "unit"
            currentunitturn = "unit2"
            turnthing()
        elif currentunitturn == "unit2" and unit2 == "Dead":
            currentturn = "unit"
            currentunitturn = "unit3"
            turnthing()
        elif currentunitturn == "unit3" and unit3 == "Dead":
            currentturn = "unit"
            currentunitturn = "unit1"
            turnthing()
    elif currentturn == "enemy":
        currentturn = "unit"
        if currentenemyturn == "enemy1" and enemy1 != "Dead":
            prevenemyturn = "enemy1"
            currentenemyturn = "enemy2"
            currentenemytarget = "".join(random.choices(["unit1", "unit2", "unit3"]))
            attackchoice = "".join(random.choice([e1a1, e1a2]))
            dialogue.set(f"{enemy1}'s turn:")
            dialoguelb = tk.Label(main_frame, text=dialogue.get(), fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
            root.update()
            time.sleep(3)
            attackenew(globals()[currentenemytarget], attackchoice)
        elif currentenemyturn == "enemy2" and enemy2 != "Dead":
            prevenemyturn = "enemy2"
            currentenemyturn = "enemy3"
            currentenemytarget = "".join(random.choices(["unit1", "unit2", "unit3"]))
            attackchoice = "".join(random.choice([e2a1, e2a2]))
            dialogue.set(f"{enemy2}'s turn:")
            dialoguelb = tk.Label(main_frame, text=dialogue.get(), fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
            root.update()
            time.sleep(3)
            attackenew(globals()[currentenemytarget], attackchoice)
        elif currentenemyturn == "enemy3" and enemy3 != "Dead":
            prevenemyturn = "enemy3"
            currentenemyturn = "enemy1"
            currentenemytarget = "".join(random.choices(["unit1", "unit2", "unit3"]))
            attackchoice = "".join(random.choice([e3a1, e3a2]))
            dialogue.set(f"{enemy3}'s turn:")
            dialoguelb = tk.Label(main_frame, text=dialogue.get(), fg="#1e1e1e", bg="#ffffff")
            dialoguelb.place(x=0, y=330, width=420, height=70)
            root.update()
            time.sleep(3)
            attackenew(globals()[currentenemytarget], attackchoice)
        elif currentenemyturn == "enemy1" and enemy1 == "Dead":
            currentturn = "enemy"
            currentenemyturn = "enemy2"
            turnthing()
        elif currentenemyturn == "enemy2" and enemy2 == "Dead":
            currentturn = "enemy"
            currentenemyturn = "enemy3"
            turnthing()
        elif currentenemyturn == "enemy3" and enemy3 == "Dead":
            currentturn = "enemy"
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
    global attack1
    global attack2
    global BASE_DIR

    linedir = os.path.join(BASE_DIR, "assets", "line.png")

    for widget in main_frame.winfo_children():
        widget.destroy()

    line_image = ImageTk.PhotoImage(Image.open(linedir).resize((600, 20)))
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
    global attack1
    global attack2
    global BASE_DIR

    line_dir = os.path.join(BASE_DIR, "assets", "line.png")

    for widget in main_frame.winfo_children():
        widget.destroy()

    line_image = ImageTk.PhotoImage(Image.open(line_dir).resize((600, 20)))
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
    global enemy1imagesub
    global enemy2imagesub
    global enemy3imagesub
    global unit1
    global unit2
    global unit3
    global unit1health
    global unit2health
    global unit3health
    global unit1image
    global unit2image
    global unit3image
    global unit1imagesub
    global unit2imagesub
    global unit3imagesub
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
    global u1a1t
    global u1a2t
    global u2a1t
    global u2a2t
    global u3a1t
    global u3a2t
    global e1a1t
    global e1a2t
    global e2a1t
    global e2a2t
    global e3a1t
    global e3a2t


    enemy1, enemy1health, enemy1imagesub, e1a1t, e1a2t, e1a1, e1a2 = assignenemy.assign()
    enemy2, enemy2health, enemy2imagesub, e2a1t, e2a2t, e2a1, e2a2 = assignenemy.assign()
    enemy3, enemy3health, enemy3imagesub, e3a1t, e3a2t, e3a1, e3a2 = assignenemy.assign()

    unit1 = selectedunit1.get().strip()
    unit2 = selectedunit2.get().strip()
    unit3 = selectedunit3.get().strip()

    unit1health, unit1imagesub, u1a1t, u1a2t, u1a1, u1a2 = assignunits.assignunit1(unit1)
    unit2health, unit2imagesub, u2a1t, u2a2t, u2a1, u2a2 = assignunits.assignunit2(unit2)
    unit3health, unit3imagesub, u3a1t, u3a2t, u3a1, u3a2 = assignunits.assignunit3(unit3)

    unit1image = os.path.join(BASE_DIR, "assets", unit1imagesub)
    unit2image = os.path.join(BASE_DIR, "assets", unit2imagesub)
    unit3image = os.path.join(BASE_DIR, "assets", unit3imagesub)

    enemy1image = os.path.join(BASE_DIR, "assets", enemy1imagesub)
    enemy2image = os.path.join(BASE_DIR, "assets", enemy2imagesub)
    enemy3image = os.path.join(BASE_DIR, "assets", enemy3imagesub)

    currentturn = "unit"
    currentunitturn = "unit1"
    currentenemyturn = "enemy1"
    currentunittarget = "enemy1"
    startload()



def pickunits():
    global selectedunit1
    global selectedunit2
    global selectedunit3
    for widget in main_frame.winfo_children():
        widget.destroy()
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

def tutorialpg4():
    for widget in main_frame.winfo_children():
        widget.destroy()

    tutpg4 = os.path.join(BASE_DIR, "assets", "tutpg4.png")
    tut4img_obj = ImageTk.PhotoImage(Image.open(tutpg4))
    tut4img_label = tk.Label(main_frame, image=tut4img_obj)
    tut4img_label.image = tut4img_obj
    tut4img_label.place(x=0, y=0, width=600, height=350)
    tut4btn = tk.Button(main_frame, text = "Let's go!", fg = "blue", font=("Arial", 11, "bold"), width=10, command=pickunits)
    tut4btn.place(x=252, y=360)

def tutorialpg3():
    for widget in main_frame.winfo_children():
        widget.destroy()

    tutpg3 = os.path.join(BASE_DIR, "assets", "tutpg3.png")
    tut3img_obj = ImageTk.PhotoImage(Image.open(tutpg3))
    tut3img_label = tk.Label(main_frame, image=tut3img_obj)
    tut3img_label.image = tut3img_obj
    tut3img_label.place(x=0, y=0, width=600, height=350)
    tut3btn = tk.Button(main_frame, text = "Contunue", fg = "blue", font=("Arial", 11, "bold"), width=10, command=tutorialpg4)
    tut3btn.place(x=252, y=360)

def tutorialpg2():
    for widget in main_frame.winfo_children():
        widget.destroy()

    tutpg2 = os.path.join(BASE_DIR, "assets", "tutpg2.png")
    tut2img_obj = ImageTk.PhotoImage(Image.open(tutpg2))
    tut2img_label = tk.Label(main_frame, image=tut2img_obj)
    tut2img_label.image = tut2img_obj
    tut2img_label.place(x=0, y=0, width=600, height=350)
    tut2btn = tk.Button(main_frame, text = "Continue", fg = "blue", font=("Arial", 11, "bold"), width=10, command=tutorialpg3)
    tut2btn.place(x=252, y=360)

def tutorialpg1():
    for widget in main_frame.winfo_children():
        widget.destroy()

    tutpg1 = os.path.join(BASE_DIR, "assets", "tutpg1.png")
    tut1img_obj = ImageTk.PhotoImage(Image.open(tutpg1))
    tut1img_label = tk.Label(main_frame, image=tut1img_obj)
    tut1img_label.image = tut1img_obj
    tut1img_label.place(width=600, height=350)
    tut1btn = tk.Button(main_frame, text = "Continue", fg = "blue", font=("Arial", 11, "bold"), width=10, command=tutorialpg2)
    tut1btn.place(x=252, y=360)

    

def tutorialyesorno():
    global playername
    playername = txt_entry.get().strip()
    if not playername.strip():
        playername = "Commander"
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text = f'Welcome, {playername}!', font=("Arial", 14, "bold"), fg="white", bg="#1e1e1e").pack(pady=5)
    tk.Label(main_frame, text = "Would you like to see the tutorial?").pack(pady=5)
    tk.Button(main_frame, text = "Yes", fg = "blue", font=("Arial", 11, "bold"), width=10, command=tutorialpg1).pack(pady=10)
    tk.Button(main_frame, text = "No", fg = "blue", font=("Arial", 11, "bold"), width=10, command=pickunits).pack(pady=10)


def intro():
    global txt_entry
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text = "Senraimon: Pokemon battles but its war thunder", font =("Arial", 14, "bold")).pack(pady=10)
    tk.Label(main_frame, text = "Please enter your name", font=("Arial", 12)).pack(pady=5)
    txt_entry = tk.Entry(main_frame, width = 24, font=("Arial", 12), fg="#1e1e1e", bg="white")
    txt_entry.pack(pady=10)
    tk.Button(main_frame, text = "Start" , fg = "blue", font=("Arial", 11, "bold"), width=10, command=tutorialyesorno).pack(pady=10)

root = tk.Tk()
root.geometry("600x400")
root.configure(bg="#1e1e1e")
root.title("Senraimon")
main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(fill="both", expand = True)
dialogue = tk.StringVar(value="salut amigos")


intro()
root.mainloop()

import tkinter as tk
from tkinter import ttk
from asyncio import wait
import random 

playername = str()
enemylist: dict[str] = ['Sukhoi Su-27P Flanker-B', 'Mikoyan-Guervich MiG-29 9.12 Fulcrum-A', 'Infantry Platoon', 'AA Infantry Platoon', 'BMP-3 IFV', 'T-90M', 'Pantsir-S1', 'S-300', 'ZSU-57']
enemy1 = set()
enemy2 = set()
enemy3 = set()
enemy1health = 0
enemy2health = 0
enemy3health = 0

def start():
    global enemy1
    global enemy2
    global enemy3
    global enemy1health
    global enemy2health
    global enemy3health
    enemy1 = [random.choice(enemylist)]
    if enemy1[0] in ("Sukhoi Su-27P Flanker-B", "Mikoyan-Guervich MiG-29 9.12 Fulcrum-A"):
        enemy1health = 200
    elif enemy1[0] in ("Infantry Platoon", "AA Infantry Platoon"):
        enemy1health = 150
    elif enemy1[0] in ("BMP-3 IFV", "Pantsir-S1", "S-300", "ZSU-57"):
        enemy1health = 250
    elif enemy1[0] in ("T-90M"):
        enemy1health = 400
    enemy2 = [random.choice(enemylist)]
    if enemy2[0] in ("Sukhoi Su-27P Flanker-B", "Mikoyan-Guervich MiG-29 9.12 Fulcrum-A"):
        enemy2health = 200
    elif enemy2[0] in ("Infantry Platoon", "AA Infantry Platoon"):
        enemy2health = 150
    elif enemy2[0] in ("BMP-3 IFV", "Pantsir-S1", "S-300", "ZSU-57"):
        enemy2health = 250
    elif enemy2[0] in ("T-90M"):
        enemy2health = 400
    enemy3 = [random.choice(enemylist)]
    if enemy3[0] in ("Sukhoi Su-27P Flanker-B", "Mikoyan-Guervich MiG-29 9.12 Fulcrum-A"):
        enemy3health = 200
    elif enemy3[0] in ("Infantry Platoon", "AA Infantry Platoon"):
        enemy3health = 150
    elif enemy3[0] in ("BMP-3 IFV", "Pantsir-S1", "S-300", "ZSU-57"):
        enemy3health = 250
    elif enemy3[0] in ("T-90M"):
        enemy3health = 400
    print(enemy1)
    print(enemy1health)
    print(enemy2)
    print(enemy2health)
    print(enemy3)
    print(enemy3health)

def pickunits():
    root = tk.Tk()
    root.title("Senraimon")
    root.geometry('600x400')
    lbl = tk.Label(root, text = f'Welcome, {playername}!').pack()
    lbl = tk.Label(root, text = "Please pick your units").pack()
    lbl = tk.Label(root, text = "Unit 1").pack()
    selectedunit1 = ttk.Combobox(
        root,
        values=["General Dynamics F-16CM Block 50 (Air)", "General Dynamics F-16CM Block 50 (Ground)", "Infantry Platoon", "AA Infantry Platoon", "M163 VADS", "AN/TWQ-1 Avenger", "MIM-104 Patriot"]

    )
    selectedunit1.pack()
    selectedunit1.set("Select unit")
    lbl = tk.Label(root, text = "Unit 2").pack()
    selectedunit2 = ttk.Combobox(
        root,
        values=["General Dynamics F-16CM Block 50 (Air)", "General Dynamics F-16CM Block 50 (Ground)", "Infantry Platoon", "AA Infantry Platoon", "M163 VADS", "AN/TWQ-1 Avenger", "MIM-104 Patriot"]

    )
    selectedunit2.pack()
    selectedunit2.set("Select unit")
    lbl = tk.Label(root, text = "Unit 3").pack()
    selectedunit3 = ttk.Combobox(
        root,
        values=["General Dynamics F-16CM Block 50 (Air)", "General Dynamics F-16CM Block 50 (Ground)", "Infantry Platoon", "AA Infantry Platoon", "M163 VADS", "AN/TWQ-1 Avenger", "MIM-104 Patriot"]

    )
    selectedunit3.pack()
    selectedunit3.set("Select unit")
    btn = tk.Button(root, text = "Start battle", fg = "blue", command=start).pack()


def intro():
    root = tk.Tk()
    root.title("Senraimon")
    root.geometry('600x400')
    lbl = tk.Label(root, text = "Senraimon: Pokemon battles but its war thunder").pack()
    lbl = tk.Label(root, text = "Please enter your name").pack()
    txt = tk.Entry(root, width = 20).pack()
    btn = tk.Button(root, text = "Start" , fg = "blue", command=pickunits).pack()
    root.mainloop()

intro()
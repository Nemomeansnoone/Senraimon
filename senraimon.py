import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import asyncio
import random 

playername = str()
enemylist: dict[str] = ['Su-27P Flanker-B', 'MiG-29 9.12 Fulcrum-A', 'Infantry Platoon', 'AA Infantry Platoon', 'BMP-3 IFV', 'T-90M', 'Pantsir-S1', 'S-300', 'ZSU-57']
enemy1 = None
enemy2 = None
enemy3 = None
enemy1health = 0
enemy2health = 0
enemy3health = 0
enemy1image = None
enemy2image = None
enemy3image = None
unit1 = None
unit2 = None
unit3 = None
unit1health = 0
unit2health = 0
unit3health = 0
unit1image = None
unit2image = None
unit3image = None
attack1 = "brrrt"
attack2 = "brrrrrrrrrrrt"
dialogue = "salut amigos"
currentunitturn = None
currentunittarget = None
currentenemyturn = None
currentenemytarget = None

async def wait3():
    await asyncio.sleep(3)

def settarget1():
    global currentunittarget
    currentunittarget = "enemy1"

def settarget2():
    global currentunittarget
    currentunittarget = "enemy2"

def settarget3():
    global currentunittarget
    currentunittarget = "enemy3"

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
    line_label.image = line_image  # <-- KEEP REFERENCE
    line_label.place(x=0, y=170, width=600, height=20)
    
    enemy1_img_obj = ImageTk.PhotoImage(Image.open(enemy1image).resize((160, 80)))
    enemy1_label = tk.Label(main_frame, image=enemy1_img_obj)
    enemy1_label.image = enemy1_img_obj  # <-- KEEP REFERENCE
    enemy1_label.place(x=20, y=80, width=160, height=80)

    enemy2_img_obj = ImageTk.PhotoImage(Image.open(enemy2image).resize((160, 80)))
    enemy2_label = tk.Label(main_frame, image=enemy2_img_obj)
    enemy2_label.image = enemy2_img_obj  # <-- KEEP REFERENCE
    enemy2_label.place(x=220, y=80, width=160, height=80)

    enemy3_img_obj = ImageTk.PhotoImage(Image.open(enemy3image).resize((160, 80)))
    enemy3_label = tk.Label(main_frame, image=enemy3_img_obj)
    enemy3_label.image = enemy3_img_obj  # <-- KEEP REFERENCE
    enemy3_label.place(x=420, y=80, width=160, height=80)

    unit1_img_obj = ImageTk.PhotoImage(Image.open(unit1image).resize((160, 80)))
    unit1_label = tk.Label(main_frame, image=unit1_img_obj)
    unit1_label.image = unit1_img_obj  # <-- KEEP REFERENCE
    unit1_label.place(x=20, y=200, width=160, height=80)

    unit2_img_obj = ImageTk.PhotoImage(Image.open(unit2image).resize((160, 80)))
    unit2_label = tk.Label(main_frame, image=unit2_img_obj)
    unit2_label.image = unit2_img_obj  # <-- KEEP REFERENCE
    unit2_label.place(x=220, y=200, width=160, height=80)

    unit3_img_obj = ImageTk.PhotoImage(Image.open(unit3image).resize((160, 80)))
    unit3_label = tk.Label(main_frame, image=unit3_img_obj)
    unit3_label.image = unit3_img_obj  # <-- KEEP REFERENCE
    unit3_label.place(x=420, y=200, width=160, height=80)

    enemy1 = tk.Button(main_frame, text=f'{enemy1}', fg="#1e1e1e", bg="#ffffff", command=settarget1)
    enemy1.place(x=20, y=30, width=160, height=20)

    enemy2 = tk.Button(main_frame, text=f'{enemy2}', fg="#1e1e1e", bg="#ffffff", command=settarget2)
    enemy2.place(x=220, y=30, width=160, height=20)

    enemy3 = tk.Button(main_frame, text=f'{enemy3}', fg="#1e1e1e", bg="#ffffff", command=settarget3)
    enemy3.place(x=420, y=30, width=160, height=20)

    enemy1health = tk.Label(main_frame, text=f'{enemy1health}', fg="#ffffff")
    enemy1health.place(x=20, y=60, width=160, height=20)

    enemy2health = tk.Label(main_frame, text=f'{enemy2health}', fg="#ffffff")
    enemy2health.place(x=220, y=60, width=160, height=20)

    enemy3health = tk.Label(main_frame, text=f'{enemy3health}', fg="#ffffff")
    enemy3health.place(x=420, y=60, width=160, height=20)

    unit1 = tk.Label(main_frame, text=f'{unit1}', fg="#ffffff")
    unit1.place (x=20, y=310, width=160, height=20)

    unit2 = tk.Label(main_frame, text=f'{unit2}', fg="#ffffff")
    unit2.place(x=220, y=310, width=160, height=20)

    unit3 = tk.Label(main_frame, text=f'{unit3}', fg="#ffffff")
    unit3.place(x=420, y=310, width=160, height=20)

    unit1health = tk.Label(main_frame, text=f'{unit1health}', fg="#ffffff")
    unit1health.place(x=20, y=280, width=160, height=20)

    unit2health = tk.Label(main_frame, text=f'{unit2health}', fg="#ffffff")
    unit2health.place(x=220, y=280, width=160, height=20)

    unit3health = tk.Label(main_frame, text=f'{unit3health}', fg="#ffffff")
    unit3health.place(x=420, y=280, width=160, height=20)

    dialogue = tk.Label(main_frame, text=f'{dialogue}', fg="#1e1e1e", bg="#ffffff")
    dialogue.place(x=0, y=330, width=420, height=70)

    blankspacething = tk.Label(main_frame, text="", bg="#ffffff")
    blankspacething.place(x=420, y=330, width=180, height=70)

    attack1 = tk.Button(main_frame, text="attack1", command=attack1, bg="#1e1e1e")
    attack1.place(x=440, y=330, width=140, height=30)

    attack2 = tk.Button(main_frame, text="attack2", command=attack2, bg="#1e1e1e")
    attack2.place(x=440, y=360, width=140, height=30)

    enemytext = tk.Label(main_frame, text="Enemy", fg="#1e1e1e", bg="#ffffff")
    enemytext.place(x=220, y=0, width=160, height=20)

    


    
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
        enemy1health = 200
        enemy1image = "su-27.png"
    elif enemy1 == ("MiG-29 9.12 Fulcrum-A"):
        enemy1health = 200
        enemy1image = "mig-29.png"
    elif enemy1 == ("Infantry Platoon"):
        enemy1health = 150
        enemy1image = "infantry_e.png"
    elif enemy1 == ("AA Infantry Platoon"):
        enemy1health = 150
        enemy1image = ("aa_infantry_e.png")
    elif enemy1 == ("BMP-3 IFV"):
        enemy1health = 250
        enemy1image = "bmp-3.png"
    elif enemy1 == ("Pantsir-S1"):
        enemy1health = 250
        enemy1image = "pantsir.png"
    elif enemy1 == ("S-300"):
        enemy1health = 250
        enemy1image = "s-300.png"
    elif enemy1 == ("ZSU-57"):
        enemy1health = 250
        enemy1image = "zsu-57.png"
    elif enemy1 == ("T-90M"):
        enemy1health = 400
        enemy1image = "t-90m.png"
    enemy2 = random.choice(enemylist)
    if enemy2 == ("Su-27P Flanker-B"):
        enemy2health = 200
        enemy2image = "su-27.png"
    elif enemy2 == ("MiG-29 9.12 Fulcrum-A"):
        enemy2health = 200
        enemy2image = "mig-29.png"
    elif enemy2 == ("Infantry Platoon"):
        enemy2health = 150
        enemy2image = "infantry_e.png"
    elif enemy2 == ("AA Infantry Platoon"):
        enemy2health = 150
        enemy2image = ("aa_infantry_e.png")
    elif enemy2 == ("BMP-3 IFV"):
        enemy2health = 250
        enemy2image = "bmp-3.png"
    elif enemy2 == ("Pantsir-S1"):
        enemy2health = 250
        enemy2image = "pantsir.png"
    elif enemy2 == ("S-300"):
        enemy2health = 250
        enemy2image = "s-300.png"
    elif enemy2 == ("ZSU-57"):
        enemy2health = 250
        enemy2image = "zsu-57.png"
    elif enemy2 == ("T-90M"):
        enemy2health = 400
        enemy2image = "t-90m.png"
    enemy3 = random.choice(enemylist)
    if enemy3 == ("Su-27P Flanker-B"):
        enemy3health = 200
        enemy3image = "su-27.png"
    elif enemy3 == ("MiG-29 9.12 Fulcrum-A"):
        enemy3health = 200
        enemy3image = "mig-29.png"
    elif enemy3 == ("Infantry Platoon"):
        enemy3health = 150
        enemy3image = "infantry_e.png"
    elif enemy3 == ("AA Infantry Platoon"):
        enemy3health = 150
        enemy3image = ("aa_infantry_e.png")
    elif enemy3 == ("BMP-3 IFV"):
        enemy3health = 250
        enemy3image = "bmp-3.png"
    elif enemy3 == ("Pantsir-S1"):
        enemy3health = 250
        enemy3image = "pantsir.png"
    elif enemy3 == ("S-300"):
        enemy3health = 250
        enemy3image = "s-300.png"
    elif enemy3 == ("ZSU-57"):
        enemy3health = 250
        enemy3image = "zsu-57.png"
    elif enemy3 == ("T-90M"):
        enemy3health = 400
        enemy3image = "t-90m.png"
    print(enemy1)
    print(enemy1health)
    print(enemy2)
    print(enemy2health)
    print(enemy3)
    print(enemy3health)

    unit1 = selectedunit1.get().strip()
    unit2 = selectedunit2.get().strip()
    unit3 = selectedunit3.get().strip()

    if unit1 == ("General Dynamics F-16CM Block 50 (Air)"):
        unit1health = 200
        unit1image = "f-16_a.png"
    elif unit1 == ("General Dynamics F-16CM Block 50 (Ground)"):
        unit1health = 200
        unit1image = "f-16_g.png"
    elif unit1 == ("Infantry Platoon"):
        unit1health = 150
        unit1image = "infantry_u.png"
    elif unit1 == ("AA Infantry Platoon"):
        unit1health = 150
        unit1image = "aa_infantry_u.png"
    elif unit1 == ("M163 VADS"):
        unit1health = 250
        unit1image = "m163.png"
    elif unit1 == ("AN/TWQ-1 Avenger"):
        unit1health = 250
        unit1image = "avenger.png"
    elif unit1 == ("MIM-104 Patriot"):
        unit1health = 250
        unit1image = "patriot.png"

    if unit2 == ("General Dynamics F-16CM Block 50 (Air)"):
        unit2health = 200
        unit2image = "f-16_a.png"
    elif unit2 == ("General Dynamics F-16CM Block 50 (Ground)"):
        unit2health = 200
        unit2image = "f-16_g.png"
    elif unit2 == ("Infantry Platoon"):
        unit2health = 150
        unit2image = "infantry_u.png"
    elif unit2 == ("AA Infantry Platoon"):
        unit2health = 150
        unit2image = "aa_infantry_u.png"
    elif unit2 == ("M163 VADS"):
        unit2health = 250
        unit2image = "m163.png"
    elif unit2 == ("AN/TWQ-1 Avenger"):
        unit2health = 250
        unit2image = "avenger.png"
    elif unit2 == ("MIM-104 Patriot"):
        unit2health = 250
        unit2image = "patriot.png"

    if unit3 == ("General Dynamics F-16CM Block 50 (Air)"):
        unit3health = 200
        unit3image = "f-16_a.png"
    elif unit3 == ("General Dynamics F-16CM Block 50 (Ground)"):
        unit3health = 200
        unit3image = "f-16_g.png"
    elif unit3 == ("Infantry Platoon"):
        unit3health = 150
        unit3image = "infantry_u.png"
    elif unit3 == ("AA Infantry Platoon"):
        unit3health = 150
        unit3image = "aa_infantry_u.png"
    elif unit3 == ("M163 VADS"):
        unit3health = 250
        unit3image = "m163.png"
    elif unit3 == ("AN/TWQ-1 Avenger"):
        unit3health = 250
        unit3image = "avenger.png"
    elif unit3 == ("MIM-104 Patriot"):
        unit3health = 250
        unit3image = "patriot.png"

    print(unit1)
    print(unit2)
    print(unit3)

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
        "General Dynamics F-16CM Block 50 (Air)",
        "General Dynamics F-16CM Block 50 (Ground)",
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
main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(fill="both", expand = True)

intro()
root.mainloop()

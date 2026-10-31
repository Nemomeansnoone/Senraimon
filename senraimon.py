import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTK
import asyncio
import random 

playername = str()
enemylist: dict[str] = ['Sukhoi Su-27P Flanker-B', 'Mikoyan-Guervich MiG-29 9.12 Fulcrum-A', 'Infantry Platoon', 'AA Infantry Platoon', 'BMP-3 IFV', 'T-90M', 'Pantsir-S1', 'S-300', 'ZSU-57']
enemy1 = None
enemy2 = None
enemy3 = None
enemy1health = 0
enemy2health = 0
enemy3health = 0
unit1 = None
unit2 = None
unit3 = None
unit1health = 0
unit2health = 0
unit3health = 0
dialogue = None

async def wait3():
    await asyncio.sleep(3)

def start(self, main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()

    self.line_image = ImageTK.PhotoImage(Image.open("line.png").resize((600,20)))
    self.line = tk.Label(main_frame, image = self.line_image)
    self.line.place(x=0, y=170, width=600, height=20)
    
    self.enemy1_image = ImageTk.PhotoImage(Image.open(enemy1image).resize((160,80)))
    self.enemy1 = tk.Label(main_frame, image=self.enemy1_image)
    self.enemy1 = place(x=20, y=80, width=160, height=80)

    self.enemy2_image = ImageTk.PhotoImage(Image.open(enemy2image).resize((160,80)))
    self.enemy2 = tk.Label(main_frame, image=self.enemy2_image)
    self.enemy2 = place(x=220, y=80, width=160, height=80)

    self.enemy3_image = ImageTk.PhotoImage(Image.open(enemy3image).resize((160,80)))
    self.enemy3 = tk.Label(main_frame, image=self.enemy3_image)
    self.enemy3 = place(x=420, y=80, width=160, height=80)

    self.unit1_image = ImageTk.PhotoImage(Image.open(unit1image).resize((160,80)))
    self.unit1 = tk.Label(main_frame, image=self.unit1_image)
    self.unit1 = place(x=20, y=200, width=160, height=80)

    self.unit2_image = ImageTk.PhotoImage(Image.open(unit2image).resize((160,80)))
    self.unit2 = tk.Label(main_frame, image=self.unit2_image)
    self.unit2 = place(x=220, y=200, width=160, height=80)

    self.unit3_image = ImageTk.PhotoImage(Image.open(unit3image).resize((160,80)))
    self.unit2 = tk.Label(main_frame, image=self.unit3_image)
    self.unit3 = place(x=420, y=200, width=160, height=80)

    self.enemy1 = tk.Label(main_frame, text=f'{enemy1}', fg="#ffffff")
    self.enemy1.place(x=20, y=30, width=160, height=20)

    self.enemy2 = tk.Label(main_frame, text=f'{enemy2}', fg="#ffffff")
    self.enemy2.place(x=220, y=30, width=160, height=20)

    self.enemy3 = tk.Label(main_frame, text=f'{enemy3}', fg="#ffffff")
    self.enemy3.place(x=420, y=30, width=160, height=20)

    self.enemy1health = tk.Label(main_frame, text=f'{enemy1health}', fg="#ffffff")
    self.enemy1health.place(x=20, y=60, width=160, heigh=20)

    self.enemy2health = tk.Label(main_frame, text=f'{enemy2health}', fg="#ffffff")
    self.enemy2health.place(x=220, y=60, width=160, height=20)

    self.enemy3health = tk.Label(main_frame, text=f'{enemy3health}', fg="#ffffff")
    self.enemy3health.place(x=420, y=60, width=160, height=20)

    self.unit1 = tk.Label(main_frame, text=f'{unit1}', fg="#ffffff")
    self.unit1.place (x=20, y=310, width=160, height=20)

    self.unit2 = tk.Label(main_frame, text=f'{unit2}', fg="#ffffff")
    self.unit2.place(x=220, y=310, width=160, height=20)

    self.unit3 = tk.Label(main_frame, text=f'{unit3}', fg="#ffffff")
    self.unit3.place(x=420, y=310, width=160, height=20)

    self.unit1health = tk.Label(main_frame, text=f'{unit1health}', fg="#ffffff")
    self.unit1health.place(x=20, y=280, width=160, height=20)

    self.unit2health = tk.Label(main_frame, text=f'{unit2health}', fg="#ffffff")
    self.unit2health.place(x=220, y=280, width=160, height=20)

    self.unit3health = tk.Label(main_frame, text=f'{unit3health}', fg="#ffffff")
    self.unit3health.place(x=420, y=280, width=160, height=20)

    self.dialogue = tk.Label(main_frame, text=f'{dialogue}', fg="#ffffff")
    self.dialogue.place(x=0, y=330, width=420, height=70)

    self.blankspacething = tk.Label(main_frame, text="", fg="#ffffff")
    self.blankspacething.place(x=420, y=330, width=180, height=70)

    self.attack1 = tk.Button(main_frame, text="attack1", command=self.attack1, bg="#1e1e1e")
    self.attack1.place(x=440, y=330, width=140, height=30)

    self.attack2 = tk.Button(main_frame, text="attack2", command=self.attack2, bg="#1e1e1e")
    self.attack2.place(x=440, y=360, width=140, height=30)

    self.enemytext = tk.Label(main_frame, text="Enemy", fg="#1e1e1e", bg="#ffffff")
    self.enemytext.place(x=220, y=0, width=160, height=20)

    


    
def startprep():
    global enemy1
    global enemy2
    global enemy3
    global enemy1health
    global enemy2health
    global enemy3health
    global unit1
    global unit2
    global unit3
    global unit1health
    global unit2health
    global unit3health

    enemy1 = random.choice(enemylist)
    if enemy1 in ("Sukhoi Su-27P Flanker-B", "Mikoyan-Guervich MiG-29 9.12 Fulcrum-A"):
        enemy1health = 200
    elif enemy1 in ("Infantry Platoon", "AA Infantry Platoon"):
        enemy1health = 150
    elif enemy1 in ("BMP-3 IFV", "Pantsir-S1", "S-300", "ZSU-57"):
        enemy1health = 250
    elif enemy1 == "T-90M":
        enemy1health = 400
    enemy2 = random.choice(enemylist)
    if enemy2 in ("Sukhoi Su-27P Flanker-B", "Mikoyan-Guervich MiG-29 9.12 Fulcrum-A"):
        enemy2health = 200
    elif enemy2 in ("Infantry Platoon", "AA Infantry Platoon"):
        enemy2health = 150
    elif enemy2 in ("BMP-3 IFV", "Pantsir-S1", "S-300", "ZSU-57"):
        enemy2health = 250
    elif enemy2 == "T-90M":
        enemy2health = 400
    enemy3 = random.choice(enemylist)
    if enemy3 in ("Sukhoi Su-27P Flanker-B", "Mikoyan-Guervich MiG-29 9.12 Fulcrum-A"):
        enemy3health = 200
    elif enemy3 in ("Infantry Platoon", "AA Infantry Platoon"):
        enemy3health = 150
    elif enemy3 in ("BMP-3 IFV", "Pantsir-S1", "S-300", "ZSU-57"):
        enemy3health = 250
    elif enemy3 == "T-90M":
        enemy3health = 400
    print(enemy1)
    print(enemy1health)
    print(enemy2)
    print(enemy2health)
    print(enemy3)
    print(enemy3health)

    unit1 = selectedunit1.get().strip()
    unit2 = selectedunit2.get().strip()
    unit3 = selectedunit3.get().strip()

    if unit1 in ("General Dynamics F-16CM Block 50 (Air)", "General Dynamics F-16CM Block 50 (Ground)"):
        unit1health = 200
    elif unit1 in ("Infantry Platoon", "AA Infantry Platoon"):
        unit1health = 150
    elif unit1 in ("M163 VADS", "AN/TWQ-1 Avenger, MIM-104 Patriot"):
        unit1health = 250

    if unit2 in ("General Dynamics F-16CM Block 50 (Air)", "General Dynamics F-16CM Block 50 (Ground)"):
        unit2health = 200
    elif unit2 in ("Infantry Platoon", "AA Infantry Platoon"):
        unit2health = 150
    elif unit2 in ("M163 VADS", "AN/TWQ-1 Avenger, MIM-104 Patriot"):
        unit2health = 250

    if unit3 in ("General Dynamics F-16CM Block 50 (Air)", "General Dynamics F-16CM Block 50 (Ground)"):
        unit3health = 200
    elif unit3 in ("Infantry Platoon", "AA Infantry Platoon"):
        unit3health = 150
    elif unit3 in ("M163 VADS", "AN/TWQ-1 Avenger, MIM-104 Patriot"):
        unit3health = 250
    print(unit1)
    print(unit2)
    print(unit3)

    start()



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

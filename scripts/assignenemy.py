import random

enemies = {
    "Su-27P Flanker-B": ("Su-27P Flanker-B", 200, "su-27.png", "30mm cannon strafe", "R-73"),
    "MiG-29 9.12 Fulcrum-A": ("MiG-29 9.12 Fulcrum-A", 200, "mig-29.png", "30mm cannon strafe", "FAB-500M-62"),
    "Infantry Platoon": ("Infantry Platoon", 150, "infantry_e.png", "Rifle fire", "Grenade Launcher"),
    "AA Infantry Platoon": ("AA Infantry Platoon", 150, "aa_infantry_e.png", "Rifle fire", "9K38 Igla"),
    "BMP-3": ("BMP-3", 250, "bmp-3.png", "100mm cannon", "9M133M Kornet-M"),
    "Pantsir-S1": ("Pantsir-S1", 250, "pantsir.png", "30mm cannon burst", "57E6"),
    "S-300": ("S-300", 250, "s-300.png", "9M96E1", "9M96E1"),
    "ZSU-57": ("ZSU-57", 250, "zsu-57.png", "57mm cannon burst", "57mm cannon burst"),
    "T-90M": ("T-90M", 400, "t-90m.png", "125mm cannon", "12.7mm Kord HMG")
}
enemylist: dict[str] = ['Su-27P Flanker-B', 'MiG-29 9.12 Fulcrum-A', 'Infantry Platoon', 'AA Infantry Platoon', 'BMP-3', 'T-90M', 'Pantsir-S1', 'S-300', 'ZSU-57']

def assign():
    chosen = random.choice(enemylist)
    return enemies.get(str(chosen).strip())




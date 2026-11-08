units = {
    "F-16CM Block 50 (Air)": (200, "f-16_a.png", "20mm cannon strafe", "AIM-9M"),
    "F-16CM Block 50 (Ground)": (200, "f-16_g.png", "20mm cannon strafe", "LDGP Mk 83"),
    "Infantry Platoon": (150, "infantry_u.png", "Rifle fire", "Grenade Launcher"),
    "AA Infantry Platoon": (150, "aa_infantry_u.png", "Rifle fire", "Stinger"),
    "M163 VADS": (250, "m163.png", "20mm cannon burst", "20mm cannon burst"),
    "AN/TWQ-1 Avenger": (250, "avenger.png", "Stinger", "Stinger"),
    "MIM-104 Patriot": (250, "patriot.png", "Patriot PAC-3", "Patriot PAC-3")
}

def assignunit1(unit):
    return units.get(str(unit).strip())

def assignunit2(unit):
    return units.get(str(unit).strip())

def assignunit3(unit):
    return units.get(str(unit).strip())

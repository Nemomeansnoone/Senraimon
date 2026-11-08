units = {
    "F-16CM Block 50 (Air)": (200, "f-16_a.png", "20mm cannon strafe", "AIM-9M", "twmmstr", "aim9m"),
    "F-16CM Block 50 (Ground)": (200, "f-16_g.png", "20mm cannon strafe", "LDGP Mk 83", "twmmstr", "ldgp"),
    "Infantry Platoon": (150, "infantry_u.png", "Rifle fire", "Grenade Launcher", "rifleu", "grenadelu"),
    "AA Infantry Platoon": (150, "aa_infantry_u.png", "Rifle fire", "Stinger", "rifleu", "stinger"),
    "M163 VADS": (250, "m163.png", "20mm cannon burst", "20mm cannon burst", "twmmbur", "twmmbur"),
    "AN/TWQ-1 Avenger": (250, "avenger.png", "Stinger", "Stinger", "stinger", "stinger"),
    "MIM-104 Patriot": (250, "patriot.png", "Patriot PAC-3", "Patriot PAC-3", "patriot", "patriot")
}

def assignunit1(unit):
    return units.get(str(unit))

def assignunit2(unit):
    return units.get(str(unit))

def assignunit3(unit):
    return units.get(str(unit))

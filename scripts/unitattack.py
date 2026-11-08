import random

attackchance = {

}



def twmmstr(target):
    if target == "Infantry Platoon" or target == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.3, 0.7])
        if hitornot == ['hit']:
            return 75
        else: 
            return 0
    elif target == "S-300" or target == "Pantsir-S1" or target == "ZSU-57":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
        if hitornot == ['hit']:
            return 60
        else:
            return 0
    elif target == "BMP-3":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
        if hitornot == ['hit']:
            return 50
        else:
            return 0
    elif target == "T-90M":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
        if hitornot == ['hit']:
            return 40
        else:
            return 0
    elif target == "Su-27P Flanker-B" or "MiG-29 9.12 Fulcrum-A":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.7, 0.3])
        if hitornot == ['hit']:
            return 60
        else:
            return 0
    else:
        return 0

def ldgp(target):
    if target == "Infantry Platoon" or target == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.4, 0.6])
        if hitornot == ['hit']:
            return 125
        else:
            return 0
    elif target == "S-300" or target == "Pantsir-S1" or target == "ZSU-57":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.65, 0.35])
        if hitornot == ['hit']:
            return 200
        else: 
            return 0
    elif target == "BMP=3":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.65, 0.35])
        if hitornot == ['hit']:
            return 225
        else:
            return 0
    elif target == "T-90M":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.65, 0.35])
        if hitornot == ['hit']:
            return 250
        else:
            return 0
    else:
        return 0

def aim9x(target):
    if target == "Su-27P Flanker-B" or target == "MiG-29 9.12 Fulcrum-A":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.9, 0.1])
        if hitornot == ['hit']:
            return 100
        else:
            return 0
    else:
        return 0

def rifleu(target):
    if target == "Infantry Platoon" or target == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 30
        else:
            return 0
    elif target == "S-300" or target == "Pantsir-S1" or target == "ZSU-57":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 15
        else:
            return 0
    elif target == "Su-27P Flanker-B" or target == "MiG-29 9.12 Fulcrum-A":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.05, 0.95])
        if hitornot == ['hit']:
            return 30
        else:
            return 0
    else:
        return 0

def grenadelu(target):
    if target == "Infantry Platoon" or target == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 50
        else:
            return 0
    elif target == "S-300" or target == "Pantsir-S1" or target == "ZSU-57":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 80
        else:
            return 0
    elif target == "BMP-3":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 70
        else:
            return 0
    elif target == "T-90M":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 65
        else:
            return 0
    elif target == "Su-27 Flanker-B" or target == "MiG-29 9.12 Fulcrum-A":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.01, 0.99])
        if hitornot == ['hit']:
            return 80
        else:
            return 0
    else:
        return 0

def stinger(target):
    if target == "Su-27P Flanker-B" or target == "MiG-29 9.12 Fulcrum-A":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 90
        else:
            return 0
    else:
        return 0

def twmmbr(target):
    if target == "Infantry Platoon" or target == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 75
        else: 
            return 0
    elif target == "S-300" or target == "Pantsir-S1" or target == "ZSU-57":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 60
        else:
            return 0
    elif target == "BMP-3":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 50
        else:
            return 0
    elif target == "T-90M":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 40
        else:
            return 0
    elif target == "Su-27P Flanker-B" or "MiG-29 9.12 Fulcrum-A":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 60
        else:
            return 0
    else:
        return 0

def patriot(target):
    if target == "Su-27P Flanker-B" or target == "MiG-29 9.12 Fulcrum-A":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.9, 0.1])
        if hitornot == ['hit']:
            return 110
        else:
            return 0
    else:
        return 0

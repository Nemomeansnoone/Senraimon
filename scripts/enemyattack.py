import random

def trmmstr(etarget):
    if etarget == "Infantry Platoon" or etarget == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.3, 0.7])
        if hitornot == ['hit']:
            return 75
        else:
            return 0
    elif etarget == "M163 VADS" or etarget == "AN/TWQ-1 Avenger" or etarget == "MIM-104 Patriot":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
        if hitornot == ['hit']:
            return 60
        else:
            return 0
    elif etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'])
        if hitornot == ['hit']:
            return 60
        else:
            return 0
    else:
        return 0

def fab500(etarget):
    if etarget == "Infantry Platoon" or etarget == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.4, 0.6])
        if hitornot == ['hit']:
            return 125
        else:
            return 0
    elif etarget == "M163 VADS" or etarget == "AN/TWQ-1 Avenger" or etarget == "MIM-104 Patriot":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.65, 0.35])
        if hitornot == ['hit']:
            return 200
        else:
            return 0
    else:
        return 0

def r73(etarget):
    if etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.9, 0.1])
        if hitornot == ['hit']:
            return 100
        else:
            return 0
    else:
        return 0

def riflee(etarget):
    if etarget == "Infantry Platoon" or etarget == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 30
        else:
            return 0
    elif etarget == "M163 VADS" or etarget == "AN/TWQ-1 Avenger" or etarget == "MIM-104 Patriot":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 15
        else:
            return 0
    elif etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.05, 0.95])
        if hitornot == ['hit']:
            return 30
        else:
            return 0
    else: 
        return 0

def grenadele(etarget):
    if etarget == "Infantry Platoon" or etarget == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 50
        else:
            return 0
    elif etarget == "M163 VADS" or etarget == "AN/TWQ-1 Avenger" or etarget == "MIM-104 Patriot":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 80
        else:
            return 0
    elif etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.01, 0.99])
        if hitornot == ['hit']:
            return 80
        else:
            return 0
    else:
        return 0

def igla(etarget):
    if etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 90
        else:
            return 0
    else:
        return 0

def hummcannon(etarget):
    if etarget == "Infantry Platoon" or etarget == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
        if hitornot == ['hit']:
            return 60
        else:
            return 0
    elif etarget == "M163 VADS" or etarget == "AN/TWQ-1 Avenger" or etarget == "MIM-104 Patriot":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
        if hitornot == ['hit']:
            return 90
        else:
            return 0
    elif etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.01, 0.99])
        if hitornot == ['hit']:
            return 110
        else:
            return 0
    else: 
        return 0

def kornet(etarget):
    if etarget == "Infantry Platoon" or etarget == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.4, 0.6])
        if hitornot == ['hit']:
            return 60
        else:
            return 0
    elif etarget == "M163 VADS" or etarget == "AN/TWQ-1 Avenger" or etarget == "MIM-104 Patriot":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.7, 0.3])
        if hitornot == ['hit']:
            return 90
        else:
            return 0
    elif etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.05, 0.95])
        if hitornot == ['hit']:
            return 90
        else:
            return 0
    else:
        return 0

def trmmbur(etarget):
    if etarget == "Infantry Platoon" or etarget == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
        if hitornot == ['hit']:
            return 75
        else:
            return 0
    elif etarget == "M163 VADS" or etarget == "AN/TWQ-1 Avenger" or etarget == "MIM-104 Patriot":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.7, 0.3])
        if hitornot == ['hit']:
            return 60
        else:
            return 0
    elif etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 60
        else:
            return 0
    else: return 0

def fvsvesx(etarget):
    if etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 90
        else:
            return 0
    else:
        return 0

def nnmnnsxeon(etarget):
    if etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.9, 0.1])
        if hitornot == ['hit']:
            return 110
        else:
            return 0
    else: 
        return 0

def fvsvmmbr(etarget):
    if etarget == "Infantry Platoon" or etarget == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
        if hitornot == ['hit']:
            return 75
        else:
            return 0
    elif etarget == "M163 VADS" or etarget == "AN/TWQ-1 Avenger" or etarget == "MIM-104 Patriot":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.7, 0.3])
        if hitornot == ['hit']:
            return 70
        else:
            return 0
    elif etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 70
        else:
            return 0
    else:
        return 0

def kord(etarget):
    if etarget == "Infantry Platoon" or etarget == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 40
        else:
            return 0
    elif etarget == "M163 VADS" or etarget == "AN/TWQ-1 Avenger" or etarget == "MIM-104 Patriot":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
        if hitornot == ['hit']:
            return 20
        else:
            return 0
    elif etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.05, 0.95])
        if hitornot == ['hit']:
            return 40
        else:
            return 0
    else:
        return 0

def hutwfvmmcannon(etarget):
    if etarget == "Infantry Platoon" or etarget == "AA Infantry Platoon":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
        if hitornot == ['hit']:
            return 70
        else:
            return 0
    elif etarget == "M163 VADS" or etarget == "AN/TWQ-1 Avenger" or etarget == "MIM-104 Patriot":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
        if hitornot == ['hit']:
            return 125
        else:
            return 0
    elif etarget == "F-16CM Block 50 (Air)" or etarget == "F-16CM Block 50 (Ground)":
        hitornot = random.choices(['hit', 'not hit'], weights=[0.01, 0.99])
        if hitornot == ['hit']:
            return 125
        else:
            return 0
    else:
        return 0

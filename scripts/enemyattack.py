import random

def attack(target, attackname):
    if attackname == "trmmstr":
        if target == "Infantry Platoon" or target == "AA Infantry Platoon":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.4, 0.6])
            if hitornot == ['hit']:
                return 75
            else:
                return 0
        elif target == "M163 VADS" or target == "AN/TWQ-1 Avenger" or target == "MIM-104 Patriot":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
            if hitornot == ['hit']:
                return 60
            else:
                return 0
        elif target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.7, 0.3])
            if hitornot == ['hit']:
                return 60
            else:
                return 0
        else:
            return 0
    elif attackname == "fab500":
        if target == "Infantry Platoon" or target == "AA Infantry Platoon":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.5, 0.5])
            if hitornot == ['hit']:
                return 125
            else:
                return 0
        elif target == "M163 VADS" or target == "AN/TWQ-1 Avenger" or target == "MIM-104 Patriot":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.7, 0.3])
            if hitornot == ['hit']:
                return 200
            else:
                return 0
        else:
            return 0
    elif attackname == "r73":
        if target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.9, 0.1])
            if hitornot == ['hit']:
                return 100
            else:
                return 0
        else:
            return 0
    elif attackname == "riflee":
        if target == "Infantry Platoon" or target == "AA Infantry Platoon":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
            if hitornot == ['hit']:
                return 30
            else:
                return 0
        elif target == "M163 VADS" or target == "AN/TWQ-1 Avenger" or target == "MIM-104 Patriot":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
            if hitornot == ['hit']:
                return 15
            else:
                return 0
        elif target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.05, 0.95])
            if hitornot == ['hit']:
                return 30
            else:
                return 0
        else: 
            return 0
    elif attackname == "grenadele":
        if target == "Infantry Platoon" or target == "AA Infantry Platoon":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
            if hitornot == ['hit']:
                return 50
            else:
                return 0
        elif target == "M163 VADS" or target == "AN/TWQ-1 Avenger" or target == "MIM-104 Patriot":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
            if hitornot == ['hit']:
                return 80
            else:
                return 0
        elif target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.01, 0.99])
            print("yez")
            print(hitornot)
            if hitornot == ['hit']:
                return 80
            else:
                return 0
        else:
            return 0
    elif attackname == "igla":
        if target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
            if hitornot == ['hit']:
                return 90
            else:
                return 0
        else:
            return 0
    elif attackname == "hummcannon":
        if target == "Infantry Platoon" or target == "AA Infantry Platoon":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
            if hitornot == ['hit']:
                return 60
            else:
                return 0
        elif target == "M163 VADS" or target == "AN/TWQ-1 Avenger" or target == "MIM-104 Patriot":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
            if hitornot == ['hit']:
                return 90
            else:
                return 0
        elif target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.01, 0.99])
            if hitornot == ['hit']:
                return 110
            else:
                return 0
        else: 
            return 0
    elif attackname == "kornet":
        if target == "Infantry Platoon" or target == "AA Infantry Platoon":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.4, 0.6])
            if hitornot == ['hit']:
                return 60
            else:
                return 0
        elif target == "M163 VADS" or target == "AN/TWQ-1 Avenger" or target == "MIM-104 Patriot":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.7, 0.3])
            if hitornot == ['hit']:
                return 90
            else:
                return 0
        elif target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.05, 0.95])
            if hitornot == ['hit']:
                return 90
            else:
                return 0
        else:
            return 0
    elif attackname == "trmmbur":
        if target == "Infantry Platoon" or target == "AA Infantry Platoon":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
            if hitornot == ['hit']:
                return 75
            else:
                return 0
        elif target == "M163 VADS" or target == "AN/TWQ-1 Avenger" or target == "MIM-104 Patriot":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.7, 0.3])
            if hitornot == ['hit']:
                return 60
            else:
                return 0
        elif target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
            if hitornot == ['hit']:
                return 60
            else:
                return 0
        else: 
            return 0
    elif attackname == "fvsvesx":
        if target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
            if hitornot == ['hit']:
                return 90
            else:
                return 0
        else:
            return 0
    elif attackname == "nnmnnsxeon":
        if target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.9, 0.1])
            if hitornot == ['hit']:
                return 110
            else:
                return 0
        else: 
            return 0
    elif attackname == "fvsvmmbur":
        if target == "Infantry Platoon" or target == "AA Infantry Platoon":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
            if hitornot == ['hit']:
                return 75
            else:
                return 0
        elif target == "M163 VADS" or target == "AN/TWQ-1 Avenger" or target == "MIM-104 Patriot":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.7, 0.3])
            if hitornot == ['hit']:
                return 70
            else:
                return 0
        elif target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
            if hitornot == ['hit']:
                return 70
            else:
                return 0
        else:
            return 0
    elif attackname == "kord":
        if target == "Infantry Platoon" or target == "AA Infantry Platoon":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
            if hitornot == ['hit']:
                return 40
            else:
                return 0
        elif target == "M163 VADS" or target == "AN/TWQ-1 Avenger" or target == "MIM-104 Patriot":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.8, 0.2])
            if hitornot == ['hit']:
                return 20
            else:
                return 0
        elif target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.05, 0.95])
            if hitornot == ['hit']:
                return 40
            else:
                return 0
        else:
            return 0
    elif attackname == "hutwfvmmcannon":
        if target == "Infantry Platoon" or target == "AA Infantry Platoon":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
            if hitornot == ['hit']:
                return 70
            else:
                return 0
        elif target == "M163 VADS" or target == "AN/TWQ-1 Avenger" or target == "MIM-104 Patriot":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.6, 0.4])
            if hitornot == ['hit']:
                return 125
            else:
                return 0
        elif target == "F-16CM Block 50 (Air)" or target == "F-16CM Block 50 (Ground)":
            hitornot = random.choices(['hit', 'not hit'], weights=[0.01, 0.99])
            if hitornot == ['hit']:
                return 125
            else:
                return 0
        else:
            return 0
    else:
        return 0

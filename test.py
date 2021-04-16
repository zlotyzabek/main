import random

t = [0]
r = 0

def ifRandomRSet(n, r1, r2):
    if t[-1] == n:
        return random.randrange(r1, r2)
    else:
        return None


def GenerateTerainGrassland(szerokosc=2048):
    for i in range(szerokosc):

        r = ifRandomRSet(0, 0, 2)
        if r != None:
            t.append(r)

        r = ifRandomRSet(1, 0, 3)
        if r != None:
            t.append(r)

        r = ifRandomRSet(2, 1, 4)
        if r != None:
            t.append(r)

        r = ifRandomRSet(3, 2, 5)
        if r != None:
            t.append(r)

        r = ifRandomRSet(4, 3, 6)
        if r != None:
            t.append(r)


        r = ifRandomRSet(5, 4, 5)
        if r != None:
            t.append(r)
            t.append(4)

    return t



print("Generator Świata")
print("Wpisz na ile kratek ma być świat(Szerokosćcc)")
dlugosc = int(input("->"))

swiat = GenerateTerainGrassland(dlugosc)

swiatFileToWrite = []

# [{"x": 0, "y": -168, "z": 0}, {"x": 0, "y": -120, "z": 0}]

def swiat0(sz):
    for i in range(35 * 48, -48, -48):
        swiatFileToWrite[sz].append(f"{sz * 48},{792 - i},0\n")
    swiatFileToWrite[sz].append(f"{sz * 48},840,3\n")
    swiatFileToWrite[sz].append(f"{sz * 48},888,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},936,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},984,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},1032,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},1080,1\n")
    for i in range(0, 57 * 48, 48):
        swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")

def swiat1(sz):
    for i in range(34 * 48, -48, -48):
        swiatFileToWrite[sz].append(f"{sz * 48},{744 - i},0\n")
    swiatFileToWrite[sz].append(f"{sz * 48},792,3\n")
    swiatFileToWrite[sz].append(f"{sz * 48},840,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},888,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},936,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},984,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},1032,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},1080,1\n")
    for i in range(0, 57 * 48, 48):
        swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")

def swiat2(sz):
    for i in range(33 * 48, -48, -48):
        swiatFileToWrite[sz].append(f"{sz * 48},{696 - i},0\n")
    swiatFileToWrite[sz].append(f"{sz * 48},744,3\n")
    swiatFileToWrite[sz].append(f"{sz * 48},792,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},840,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},888,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},936,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},984,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},{1032},1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},{1080},1\n")
    for i in range(0, 57 * 48, 48):
        swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")

def swiat3(sz):
    for i in range(32 * 48, -48, -48):
        swiatFileToWrite[sz].append(f"{sz * 48},{648 - i},0\n")
    swiatFileToWrite[sz].append(f"{sz * 48},696,3\n")
    swiatFileToWrite[sz].append(f"{sz * 48},744,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},792,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},840,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},888,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},936,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},984,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},1032,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},1080,1\n")
    for i in range(0, 57 * 48, 48):
        swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")

def swiat4(sz):
    for i in range(31 * 48, -48, -48):
        swiatFileToWrite[sz].append(f"{sz * 48},{600 - i},0\n")
    swiatFileToWrite[sz].append(f"{sz * 48},648,3\n")
    swiatFileToWrite[sz].append(f"{sz * 48},696,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},744,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},792,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},840,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},888,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},936,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},984,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},1032,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},1080,1\n")
    for i in range(0, 57 * 48, 48):
        swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")

def swiat5(sz):
    for i in range(30 * 48, -48, -48):
        swiatFileToWrite[sz].append(f"{sz * 48},{552 - i},0\n")
    swiatFileToWrite[sz].append(f"{sz * 48},600,4\n")
    swiatFileToWrite[sz].append(f"{sz * 48},648,3\n")
    swiatFileToWrite[sz].append(f"{sz * 48},696,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},744,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},792,2\n")
    swiatFileToWrite[sz].append(f"{sz * 48},840,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},888,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},936,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},984,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},1032,1\n")
    swiatFileToWrite[sz].append(f"{sz * 48},1080,1\n")
    for i in range(0, 57 * 48, 48):
        swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")

opcje = {0: swiat0, 1: swiat1, 2: swiat2, 3: swiat3, 4: swiat4, 5: swiat5}

for sz in range(dlugosc):
    swiatFileToWrite.append([])
    opcje[swiat[sz]](sz)

saveTemp = []

for szerokosc in range(dlugosc):
    for wysokosc in range(99):
        if swiatFileToWrite[szerokosc][wysokosc].split(",")[2].split("\n")[0] == "4":
            try:
                swiatFileToWrite[szerokosc][wysokosc - 1] = str(swiatFileToWrite[szerokosc][wysokosc - 1])[::-1].replace("0,", "4,", 1)[::-1]
                swiatFileToWrite[szerokosc][wysokosc - 2] = str(swiatFileToWrite[szerokosc][wysokosc - 2])[::-1].replace("0,", "4,", 1)[::-1]
                swiatFileToWrite[szerokosc - 1][wysokosc - 2] = str(swiatFileToWrite[szerokosc - 1][wysokosc - 2])[::-1].replace("0,", "5,", 1)[::-1]
                swiatFileToWrite[szerokosc + 1][wysokosc - 2] = str(swiatFileToWrite[szerokosc + 1][wysokosc - 2])[::-1].replace("0,", "5,", 1)[::-1]
                swiatFileToWrite[szerokosc - 1][wysokosc - 1] = str(swiatFileToWrite[szerokosc - 1][wysokosc - 1])[::-1].replace("0,", "5,", 1)[::-1]
                swiatFileToWrite[szerokosc + 1][wysokosc - 1] = str(swiatFileToWrite[szerokosc + 1][wysokosc - 1])[::-1].replace("0,", "5,", 1)[::-1]
                swiatFileToWrite[szerokosc][wysokosc - 3] = str(swiatFileToWrite[szerokosc][wysokosc - 3])[::-1].replace("0,", "5,", 1)[::-1]

            except Exception:
                pass
            break

for szerokosc in range(dlugosc):
    for wysokosc in range(99):
        saveTemp.append(swiatFileToWrite[szerokosc][wysokosc])

f = open("save.mov", "w")

f.writelines(saveTemp)

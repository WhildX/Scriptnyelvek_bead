import VillainBetrayException as hiba
import numpy as np
from tkinter import *

root = Tk()
root.title("HeroVSVillain")

class Letforma:
    def __init__(self, nev, faj="ember"):
        self.nev = nev
        self.faj = faj


class Szuperhos(Letforma):
    def __init__(self, nev, faj, hosnev, jotettekSzama = 1, szuperero=50):
        super().__init__(nev, faj)
        self.hosnev = hosnev
        self._jotettekSzama = jotettekSzama
        self._szuperero = szuperero

    #Getterek
    @property
    def jotettekSzama(self):
        return self._jotettekSzama
    @property
    def szuperero(self):
        return self._szuperero

    #Setterek
    @jotettekSzama.setter
    def jotettekSzama(self, ertek):
        self._jotettekSzama = ertek
    @szuperero.setter
    def szuperero(self, ertek):
        self._szuperero = ertek

    def szuperhosEdzes(self):
        self.szuperero = self.szuperero + 10

    # Objektum szöveggé alakítása
    def __str__(self):
        return self.hosnev + " egy szuperhős, akinek szuperereje " + str(self.szuperero) + " és " + str(self.jotettekSzama) + " jótettet hajtott végre."

    # Két szuperhős akkor egyenlő ha a szupererő megegyezik és ugyannyi jó tettek hajtottak végre
    def __eq__(self, masik_hos):
        if isinstance(masik_hos, Szuperhos):
            return self._szuperero == masik_hos._szuperero and self._jotettekSzama == masik_hos._jotettekSzama
        else:
            return "Egy szuperhőst csak egy másik szuperhőssel lehet összehasonlítani!"

    def __gt__(self, masik_hos):
        if not isinstance(masik_hos, Szuperhos):
            return "Egy szuperhőst csak egy másik szuperhőssel lehet összehasonlítani!"
        if self.szuperero == masik_hos.szuperero:
            if self.jotettekSzama > masik_hos.jotettekSzama:
                return 1
            else:
                return 0
        if self.szuperero > masik_hos.szuperero:
            return 1
        else:
            return 0

    # Két szuperhős összeadása során a szupererejük és jótetteik száma összeadódik
    # A szupercsapat vezetője az lesz aki a jobb szuperhős
    def __add__(self, masik_hos):
        if not isinstance(masik_hos, Szuperhos):
            return "Egy szuperhőst csak egy másik szuperhőssel lehet összeadni!"
        if self > masik_hos:
            uj_nev = self.nev
            uj_faj = self.faj
        else:
            uj_nev = masik_hos.nev
            uj_faj = masik_hos.faj
        uj_szuperero = self._szuperero + masik_hos._szuperero
        uj_jutettekSzama = self._jotettekSzama + masik_hos._jotettekSzama
        uj_szuperhos = Szuperhos(uj_nev, uj_faj, "Megahős", uj_jutettekSzama, uj_szuperero)
        return uj_szuperhos

class Gonosztevo(Letforma):
    def __init__(self, nev, faj, alnev, buntenyekSzama = 1, gonoszsag=50):
        super().__init__(nev, faj)
        self.alnev = alnev
        self._buntenyekSzama = buntenyekSzama
        self._gonoszsag = gonoszsag

    #Getterek
    @property
    def buntenyekSzama(self):
        return self._buntenyekSzama
    @property
    def gonoszsag(self):
        return self._gonoszsag

    #Setterek
    @buntenyekSzama.setter
    def buntenyekSzama(self, ertek):
        self._buntenyekSzama = ertek
    @gonoszsag.setter
    def gonoszsag(self, ertek):
        self._gonoszsag = ertek

    def buntElkovet(self):
        self.buntenyekSzama = self.buntenyekSzama + 1
        self.gonoszsag = self.gonoszsag + 10

    # Objektum szöveggé alakítása
    def __str__(self):
        return self.alnev + " egy gonosztevő akinek " + str(self.gonoszsag) + " a gonoszsága és " + str(self.buntenyekSzama) + " bűntényt hajtott végre."

    # Két Gonosz nem fog csapatot alkotni mert nem bíznak meg egymásban

    def __add__(self, masik_gonosz):
        if not isinstance(masik_gonosz, Gonosztevo):
            return "Másik gonoszt kell megadnod!"
        else:
            try:
                raise hiba.VillainBetrayException("Két gonosz nem tud csapatot alkotni, mert nem bíznak egymásban!")
            except hiba.VillainBetrayException as vbe:
                print(vbe)

# === tesztelés ===
try:
    file = open("szuperhos.txt", "r")
except FileNotFoundError as fnfe :
    print("Hiányzik a szuperhos.txt file!")
else:
    sorok = file.readlines()
    lista = []
    for sor in sorok:
        sor = sor.rstrip()
        sor = sor.split(",")
        lista.append(Szuperhos(sor[0], sor[1], sor[2], int(sor[3]), int(sor[4])))
        iras = open("szuperhos_teljes.txt.txt", "w", encoding="utf-8")
        for i in range(len(lista)):
            iras.write(lista[i].__str__() + "\n")
        iras.close()
    file.close()

counter = 0
listLabel = Label(root, text="A hősök listája:")
listLabel.grid(row=counter, column=0)
counter += 1
for i in range(len(lista)):
    hosLabel = Label(root, text=lista[i])
    hosLabel.grid(row=counter, column=0)
    counter+=1

e = Entry(root)
e.grid(row=counter, column=0)
counter += 1
e2 = Entry(root)
e2.grid(row=counter, column=0)
counter += 1

def myClick():
    try:
        if(int(e.get()) > len(lista) or int(e.get()) < 1 or int(e2.get()) > len(lista) or int(e2.get()) < 1):
            hosLabel = Label(root, text="Nem megfelelő számot adtál meg!", fg="#F60404")
            hosLabel.grid(row=counter, column=0)
            return
        hos1 = lista[int(e.get())-1] + lista[int(e2.get())-1]
        hosLabel = Label(root, text=hos1)
        hosLabel.grid(row=counter, column=0)
    except ValueError as ve:
        hosLabel = Label(root, text="Számot kell megadni!", fg="#F60404")
        hosLabel.grid(row=counter, column=0)

myButton = Button(root, text="Adj össze 2 hőst!", command=myClick)
myButton.grid(row=counter, column=0)
counter += 1

gonosz1 = Gonosztevo("Norman Osborn", "ember", "Zöld Manó", 10, 75)
gonosz2 = Gonosztevo("Otto Gunther", "ember", "Dr Octopus", 40, 120)
gonosz3 = gonosz1+gonosz2


villainLabel = Label(root, text="A gonosztevők listája:")
villainLabel.grid(row=counter, column=0)
Vlista = []
counter += 1
Vlista.append(gonosz1)
villainLabel = Label(root, text=gonosz1)
villainLabel.grid(row=counter, column=0)
counter += 1
Vlista.append(gonosz2)
villainLabel = Label(root, text=gonosz2)
villainLabel.grid(row=counter, column=0)
counter += 1

textLabel = Label(root, text="Válasz 1 hőst és 1 gonosztevők akik harcoljanak:")
textLabel.grid(row=counter, column=0)
counter += 1

def Harc():
    try:
        if(int(eHero.get()) > len(lista) or int(eHero.get()) < 1 or int(eVillian.get()) > len(Vlista) or int(eVillian.get()) < 1):
            textLabel = Label(root, text="Nem megfelelő számot adtál meg!", fg="#F60404")
            textLabel.grid(row=counter, column=0)
            return
        heroPower = np.round(np.sqrt(lista[int(eHero.get())-1].jotettekSzama)) + int(lista[int(eHero.get())-1].szuperero)
        villainPower = np.round(np.sqrt(int(Vlista[int(eVillian.get())-1].buntenyekSzama))) + int(Vlista[int(eVillian.get())-1].gonoszsag)
        if(heroPower > villainPower):
            victoryLabel = Label(root, text="A hős győzőtt!", fg="#00ff00")
            victoryLabel.grid(row=counter, column=0)
        else:
            victoryLabel = Label(root, text="A gonosz győzőtt!", fg="#aa00ff")
            victoryLabel.grid(row=counter, column=0)
    except ValueError as ve:
        hosLabel = Label(root, text="Számot kell megadni!", fg="#F60404")
        hosLabel.grid(row=counter, column=0)


eHero = Entry(root)
eHero.grid(row=counter, column=0)
counter += 1
eVillian = Entry(root)
eVillian.grid(row=counter, column=0)
counter += 1

myButton2 = Button(root, text="Harc!", command=Harc)
myButton2.grid(row=counter, column=0)
counter += 1

root.mainloop()
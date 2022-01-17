import random
import os
def cardGenerator():
    szamlista=["123456789"]
    betulista=["qwertzuioplkjhgfdsayxcvbnm"]
    random.choice(szamlista,betulista)
    return cardGenerator

def gyartasGenerator():
    evlista=["1988,2001,2006,2010,2021,2022"]
    random.choice(evlista)
    return gyartasGenerator

pontszam=100
eredmeny=("")
ev=2022
if ev==1988 or ev==2001:
    100+150
    print(eredmeny)
if ev==2006 or ev==2021 +100*2:
    print(eredmeny)
if ev==2022 and +200%80:
    print(eredmeny)
elif 2022 -3:
    print(eredmeny)

def nevgenerator():    
    Vnevlista=["Kovadcs,Molnár,Kiss,Tóth,Nagy,Horváth,Szabó,Papp,Farkax"]
    Knevlista=["József,Sándor,Katalin,Béla,Bettina,Éva,Benedek,Péter,Erika"]
    random.choice(Vnevlista,Knevlista)
    return nevgenerator

def kiiras():
    os.system('cls')
    dbszam={}
    dbszam=input("Hány darab kártyát szeretnél létre hozni.")
    random.choice(dbszam)
    return kiiras

print("-----------------------------------------")

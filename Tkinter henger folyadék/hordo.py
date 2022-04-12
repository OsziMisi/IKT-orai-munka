'''
Van egy henger alakú hordónk, melybe nem tudjuk, hogy belefér-e a rendelkezésre
álló bor. Kérd be a bor mennyiségét literben, majd a hordó összes szükséges adatát cmben.
Adj tájékoztatást, hogy hány literes a hordó, és hogy belefér-e a hordóba a bor! Ha
belefér, akkor add meg, hogy mennyi férne még bele! Írd ki százalékosan is a
telítettséget! Az adatokat egészre kerekítve írd ki!
'''

from tkinter import *
import math
from tkinter import messagebox
import math
import os

ablak1=Tk()
szamlalo = Frame(root)
hordo_kep = PhotoImage(file = f"{os.path.dirname(os.path.realpath(__file__))}\\hordo.jpg")
hordo_label = Label(image = hordo_kep)


szam = int(mezo1.get())    
print(szam)
    
sugarka_label = Label(szamlalo, text = 'Ide a sugarat(cm)')
magassagocska_label = Label(szamlalo, text = 'Ide magassagot(m)')
borocska_label = Label(szamlalo, text = 'Bort ide(liter)')    

Button1 =ablak1.Button(text = 'enter', command = liter).pack()

kertszamok = int(input("Hany liter borunk van?"))
hordo = 100

cimke = Label(ablak1, text = "Hány liter borunk van?")

cimke.pack(anchor = "center")
mezo1 = Entry(ablak1)mezo1.pack(anchor = "center")
cimke1 = Label(ablak1, text = ("A hordóba", hordo, " liter folyadék fér"))
cimke1.pack(anchor = "center")
cimke2 = Label(ablak1, text = " ")
cimke2.pack(anchor = "center")

    if hordo > cimke:     
        cimke3 = Label(ablak1, text = "Belefér a bor!")    
        cimke3.pack(anchor = "center")
    else:    
        cimke4 = Label(ablak1, text = "Nem fér bele a bor!")    
        cimke4.pack(anchor = "center")

ablak1.mainloop()



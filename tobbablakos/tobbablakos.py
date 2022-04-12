from tkinter import *

ablak1 = Tk()

def ujablak():
    ablak2 = Toplevel(ablak1)
    uzenet2 = Message(ablak2, text='Készítette: Gipsz Jakab\nPiripócs\n2009.06.04', width=600) 
    gomb2=Button(ablak2, text ='Kilép', command=ablak2.destroy)
    uzenet2.pack(side = TOP)
    gomb2.pack(side = TOP)
    ablak2.mainloop()

#a widgetek létrehozása

szovegegy = Label(ablak1, text = 'Kattints a gombra!')
gombegy = Button(ablak1, text ='Névjegy', command=ujablak)

#laptördelés a'pack' metódus segítségével:

szovegegy.pack(side = TOP)
gombegy.pack(side = TOP)

#indítás:
ablak1.mainloop()
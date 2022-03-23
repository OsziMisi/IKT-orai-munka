'''
Feladat:
Henger sugara es magassaag CM-ben.
Sulya
terfogata
*Kerekitsuk ket tizedere*
'''

from tkinter import * 

def osszeg():
    a = int(mezo1.get())

    b = int (mezo2.get())

    c=a+b

    mezo3.delete(0, END)
    mezo3.insert(0,'Összeg ' +str(c))
ablaksok = Tk()
ablaksok.title('IKT henger kiszamito program nagyon menooo xd')
ablaksok.config(background = "white")


l2 = Label(ablaksok, text = "Magassag")
l2.grid(row = 0, column = 0, sticky = W, pady = 2)
l1.grid(row = 1, column = 0, sticky = W, pady = 2)
e1 = Entry(ablaksok)
e2 = Entry(ablaksok)
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)
l1 = Label(ablaksok, text = "Sugar")
gomb4 = Button(ablaksok, text = 'Majd', command = osszeg)
gomb4.pack(side = RIGHT)
gomb1 = Button(ablaksok, text = 'OK')
gomb1.pack(side = RIGHT) 
gomb2 = Button(ablaksok, text = 'Mégse')
gomb2.pack(side = RIGHT)
gomb3 = Button(ablaksok, text='Bezar', command=ablaksok.destroy)
gomb3.pack(side = RIGHT)
mezo1 = Entry(ablaksok)
mezo1.pack(side = RIGHT)
mezo2 = Entry(ablaksok)
mezo2.pack(side = RIGHT)



ablaksok.mainloop()


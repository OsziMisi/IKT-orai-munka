from tkinter import *

abalak1 = Tk()
abalak1.title(' A teglatest adatai')
abalak1.minsize(width = 410, height=200)

def masodikalbalak():
    abalak2 = Toplevel(abalak1)
    abalak2.title(' Eredemenyek')
    abalak2.minsize(width = 410, height=200)
    
    #widgwt
    szam1 = Label(abalak2, Text= 'Felszine')
    szam2 = Label(abalak2, Text = 'terfogata')
    m1 = Entry(abalak2)
    m2 = Entry(abalak2)
    
    #laptores
    szam1.grid(row = 1)
    szam2.grid(row = 2)
    m1.grid(row = 1, column = 2, sticky = W )
    m2.grid(row = 2, column = 2, sticky = W )
    
    a = eval(mezo1.get())    
    b = eval(mezo2.get())
    c =eval (mezo3.get())
    
    felszin = 2*(a*b+a*b+b*c)
    terfogat = a*b*c
    
    m1.delete(0, END)
    m1.insert(0,str(felszin))
    m2.delete(0, END)
    m2.insert(0, str(terfogat))
    
    abalak2.mainloop()
    
#widgetek kiszanolasa

szoveg1 = Label(abalak1, Text= 'a?')
szoveg2 = Label ( abalak1, Text= 'b?')
szoveg3 = Label ( abalak1, Text= 'c?')
gomb1 = Button(abalak1, Text= 'Kiszamitas',command = ujablak)
mezo1 = Entry(abalak1)
mezo2 = Entry(abalak1)
mezo3 = Entry(abalak1)

#laptores griddel
szoveg1.grid(row = 1)
szoveg2.grid(row = 2)
szoveg3.grid(row = 3)
gomb1.grid(row = 4, column = 2, sticky = W)
mezo1.grid(row = 1, column = 2, sticky = W)
mezo2.grid(row = 2, column = 2, sticky = W)
mezo3.grid(row = 3, column = 2, sticky = W)



abalak1.mainloop()

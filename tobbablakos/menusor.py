from tkinter import *

#Névjegy ablak 

def nevjegy():
    abl2= Toplevel(foablak)
    uz2 = Message(abl2, text='Készítette: Oroszlán Mihály\nBaja\n2022.04.12', width=300)
    gomb2 = Button(abl2, text='Kilép', command = abl2.destroy)
    uz2.pack()
    gomb2.pack() 
    abl2.mainloop
    #Névjegy ablak vége

#Felszin 
def felszin():
    def szamit():
    a = eval(mezol get())
    b=eval(mezo2.get())
    c= eval(mezo3.get())
    felszin = 2*(a*b+a*c+bc)
    mezo4.delete(0,END)
    mezo4.insert(0,str(felszin))
    
abl3 = Toplevel(foablak)
abl3.title('A téglatest felszíne') 
abl3.minsize(width=600, height=200)
szoveg1= Label(ab13, text='a:')
szoveg2=Label(ab13, text='b:')
szoveg3=Label(ab13, text='c:") szoveg4 Label(abl3, text='Eredmény:')
gombl-Button(ab13, text='Számítás', command=szamit) mezol- Entry(ab13)
mezo2= Entry(ab13) mezo3 = Entry(ab13)
mezo4 = Entry(abl3)
szoveg.grid row =1) szoveg2.grid(row =2)
szoveg3.grid(row =3)
szoveg4.grid(row =5)
gombl.grid(row-4, column-2, sticky
mezo2.grid(row-2, column=2, sticky =W)
mezol.grid(row =1, column =2, sticky =W)
mezo3.grid(row =3, column=2, sticky =W)
mezo4.grid(row =5, column -2, sticky =W)
abl3.mainloop
#Felszín ablak vége

#Térfogat ablak 

def terfogat:
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a*b*c
        mezo4.delete(0, END)
        mezo4.insert(0,str(terfogat))
        
    abl3 = Toplevel(foablak)
    abl3.title(' A teglatest terfogata')
    abl3.minsize(width = 300, height = 200)
    szoveg1 = Label(abl3, text = 'a')
    szoveg2 = Label(abl3, text = 'b')
    szoveg3 = Label(abl3, tetx = 'c')
    szoveg4 =Label(abl3, text = 'Eredmeny') 
    gomb1 = Button(abl3, text = 'Szamitani', command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 4)
    
from tkinter import *

def osszeg():
    a = int(mezo1.get())

    b = int (mezo2.get())

    c=a+b

    mezo3.delete(0, END)
    mezo3.insert(0,'Összeg ' +str(c))

foablak = Tk() 
can1 = Canvas(foablak, width = 460, height = 460, bg = "white")
photo = PhotoImage(file = "D:\IkT\Python xd\cica.gif")
item = can1.create_image(80, 80, image = photo)
can1.pack(side = "top")

cimke = Label (foablak, text='Szia Uram! Kutyádat sétáltatod?!', fg='black')
cimke.pack(side = TOP)
gomb1 = Button(foablak, text = 'OK')
gomb1.pack(side = RIGHT) 
gomb2 = Button(foablak, text = 'Mégse')
gomb2.pack(side = RIGHT)
gomb3 = Button(foablak, text = 'Alahh ahbar puff', command = foablak.destroy)
gomb3.pack(side = RIGHT)
mezo1 = Entry(foablak)
mezo1.pack(side = RIGHT)
mezo2 = Entry(foablak)
mezo2.pack(side = RIGHT)
gomb4 = Button(foablak, text = 'Osszead', command = osszeg)
gomb4.pack(side = RIGHT)


# kivonas
def kivonas():
 
    a = int(mezo1.get())
    b = int (mezo2.get())
    c=a-b
    mezo3.delete(0, END)
    mezo3.insert(0,'Kivonas összege ' +str(c))

gomb5 = Button(foablak, text = 'Kivonas', command = kivonas)
gomb5.pack()

#szorzas
def szorzas():
    a = int(mezo1.get())
    b = int (mezo2.get())
    c= a*b
    mezo3.delete(0, END)
    mezo3.insert(0,'Szorzas osszege:' +str(c))

gomb6 = Button(foablak, text = 'Szorzas', command = szorzas)
gomb6.pack(side = RIGHT)
#osztas
def osztas():
    a = int(mezo1.get())
    b = int (mezo2.get())
    c= a//b
    mezo3.delete(0, END)
    mezo3.insert(0,'Osztas osszege:' +str(c))

gomb7 = Button(foablak, text = 'Osztas', command = osztas)
gomb7.pack(side = RIGHT)

#gyokvonas
def gyok():
    import math 
    a = int(mezo1.get())
    c = math.sqrt(a)
    mezo3.delete(0, END)
    mezo3.insert(0, "Gyokvonas osszege: " +str(c))

gomb8 = Button(foablak, text = 'Gyokvonas', command = gyok)
gomb8.pack(side = RIGHT)

#negyzetre emeles

mezo3 = Entry(foablak)
mezo3.pack(side = RIGHT)



foablak.mainloop()
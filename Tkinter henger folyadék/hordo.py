from tkinter import *

ablak1 = Tk()
ablak1.geometry('500x500')
ablak1.title('Hordoka szamolo')
be1 = ablak1.entry()
be1.pack()

hordo = 140
felirat = Label(foablak1('A horodba', hordo,'fer bele'))
felirat.pack(side = 'left')

ablak1.mainloop()

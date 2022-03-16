from tkinter import * 
ablak1 = Tk()
gyoker = "D:\\IkT\\Python\\IKT-orai-munka\\"
ablak1.geometry('500x500')
ablak1.title("IKT Tkinter")
icon = PhotoImage(file = gyoker + "cica.gif")
ablak1.iconphoto(True, icon)
ablak1.config(background = "white")


cimke = Label (foablak, text='Szia Uram! Kutyádat sétáltatod?!', fg='black')
cimke.pack(side = TOP)

ablak1.mainloop()           


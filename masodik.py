from tkinter import * 
ablak1 = Tk()
gyoker = "D:\\IkT\\Python\\IKT-orai-munka\\"
ablak1.geometry('800x600')
ablak1.title("IKT Tkinter")
icon = PhotoImage(file = gyoker + "cica.gif")
ablak1.iconphoto(True, icon)
ablak1.config(background = "white")
elsokep = PhotoImage(file = gyoker + "cica.gif")
cimke = Label(ablak1,
            text = "Szia Uram!, macskádat sétálatod?!",
            fg = "#fffaef",
            bg = "#c3cee0", 
            font = ("Arial", 35, "bold"),
            bd = 10,
            relief = RAISED,
            padx = 25, 
            pady = 30, 
            image = elsokep,
            compound = "center").pack()

ablak1.mainloop()
sf
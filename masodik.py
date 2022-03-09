from tkinter import * 
ablak1 = Tk()
gyoker = "D:\\IkT\\Python\\IKT-orai-munka\\"
ablak1.geometry('500x500')
ablak1.title("IKT Tkinter")
icon = PhotoImage(file = gyoker + "cica.gif")
ablak1.iconphoto(True, icon)
ablak1.config(background = "white")
elsokep = PhotoImage(file = gyoker + "cica.gif", width = 500, height = 500)
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
            #button widget


gomb = Button(ablak1,
                text= ('Kattintsa ma!'),
                fg = 'blue',
                font = ('Arial', 20, 'bold'),
                bg = 'Purple',
                relief =SUNKEN,
                bd = 10,
                command = klikk,
                padx = 12,
                pady = 12,
                Image = gombkep,
                compound = 'bottom',
                activebackgound = 'blue',
                activeforground = 'yellow',
                state = DISABLED).pack()
ablak1.mainloop()

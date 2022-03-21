from tkinter import * 
ablak1 = Tk()
gyoker = "D:\\IkT\\Python\\IKT-orai-munka\\"
ablak1.geometry('500x500')
ablak1.title("IKT Tkinter")
icon = PhotoImage(file = gyoker + "cica.gif")
ablak1.iconphoto(True, icon)
ablak1.config(background = "white")
elsokep = PhotoImage(file = gyoker + "cica.gif", width = 500, height = 500)

cimke = Label (ablak1, 
               text='Szia Uram! Kutyádat sétáltatod?!',
               fg='black',
                bg = "#c3cee0").pack()

name_var=tk.StringVar()
passw_var=tk.StringVar()
 
def submit():
     
    name=name_var.get()
    password=passw_var.get()
     
    print("The name is : " + name)
    print("The password is : " + password)
     
    name_var.set("")
    passw_var.set("")




ablak1.mainloop()           


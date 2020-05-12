from tkinter import *

def click():
    ola = "Bom Dia " + ety1.get()
    lbl1 = Label(root, text=ola)
    lbl1.pack()
    pass

root = Tk()

ety1 = Entry(root, width=50, bg="green", fg="white", borderwidth=10)
ety1.pack()
ety1.insert(0,"Insira seu nome: ")

btn1 = Button(root, text="Digite seu nome", padx=50, pady=10, command=click, fg="yellow", bg="blue")
btn1.pack()

root.mainloop()
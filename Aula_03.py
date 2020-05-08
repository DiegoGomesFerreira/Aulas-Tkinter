from tkinter import *

def click():
    lbl1 = Label(root, text="Olhe! Você clicou em um Botão")
    lbl1.pack()
    pass

root = Tk()

btn1 = Button(root, text="Me Click", padx=50, pady=10, command=click, fg="yellow", bg="blue")
btn1.pack()

root.mainloop()
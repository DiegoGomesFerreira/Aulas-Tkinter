from tkinter import *

def abrir():
    global lbl
    global btnD
    top = Toplevel()
    top.title("Minha segunda Janela")
    top.geometry("300x300+100+100")
    top.iconbitmap("Terminal.ico")
    lbl = Label(top, text = "Top Windows").pack()
    btnD = Button(top, text="Fechar janela", command=top.destroy).pack()
    pass

root = Tk()
root.title("Aula 14 Windows")
root.geometry("300x300+100+100")
root.iconbitmap("Terminal.ico")

btn = Button(root, text="Abrir segunda janela", command=abrir).grid()

root.mainloop()
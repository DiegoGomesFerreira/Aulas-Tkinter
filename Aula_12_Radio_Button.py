from tkinter import *

def clicado(valor):
    lbl = Label(root, text = valor)
    lbl.pack()
    pass

root = Tk()
root.title("Radio Button")
root.iconbitmap("Terminal.ico")
root.geometry("500x500+100+100")

MODES = [
        ("Queijo","Queijo"),
        ("Pizza", "Pizza"),
        ("Pastel", "Pastel"),
        ("Lasanha", "Lasanha")
        ]

comida = StringVar()
comida.set("Queijo")

for texto, modo in MODES:
    Radiobutton(root, text=texto, variable=comida, value=modo).pack(anchor=W)

#variavel = IntVar()
#variavel.set("2")

#Radiobutton(root, text="Opção 1", variable=variavel, value=1, command=lambda : clicado(variavel.get())).pack()
#Radiobutton(root, text="Opção 2", variable=variavel, value=2, command=lambda : clicado(variavel.get())).pack()

#lbl = Label(root, text=comida.get())
#lbl.pack()

btn = Button(root, text="Clique me", command=lambda : clicado(comida.get()))
btn.pack()



root.mainloop()
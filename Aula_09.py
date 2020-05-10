from tkinter import *
from PIL import ImageTk,Image

def direita(numero_imagem):
    global lbl
    global btnEsquerdo
    global btnDireta

    lbl.grid_forget()

    lbl = Label(image=imagem_lista[numero_imagem-1])
    btnDireta = Button(root, text="Direita", command=lambda: direita(numero_imagem+1))
    btnEsquerdo = Button(root, text="Esquerda", command=lambda: esquerda(numero_imagem-1))

    if numero_imagem == 3:
        btnDireta = Button(root, text="Direita", state=DISABLED)
        pass

    lbl.grid(row=0, column=0, columnspan=3)
    btnDireta.grid(row=1, column=2)
    btnEsquerdo.grid(row=1, column=0)
    pass

def esquerda(numero_imagem):
    global lbl
    global btnEsquerdo
    global btnDireta

    lbl.grid_forget()

    lbl = Label(image=imagem_lista[numero_imagem+1])
    btnDireta = Button(root, text="Direita", command=lambda: direita(numero_imagem+1))
    btnEsquerdo = Button(root, text="Esquerda", command=lambda: esquerda(numero_imagem-1))

    if numero_imagem == 0:
        btnEsquerdo = Button(root, text="Esquerdo", state=DISABLED)
        pass

    lbl.grid(row=0, column=0, columnspan=3)
    btnDireta.grid(row=1, column=2)
    btnEsquerdo.grid(row=1, column=0)
    pass

root = Tk()
root.iconbitmap("Terminal.ico")

img1 = ImageTk.PhotoImage(Image.open("labrador-head.png"))
img2 = ImageTk.PhotoImage(Image.open("mite-alt.png"))
img3 = ImageTk.PhotoImage(Image.open("monkey.png"))
img4 = ImageTk.PhotoImage(Image.open("panda.png"))

imagem_lista = [img1, img2, img3, img4]

lbl = Label(image=imagem_lista[1])
lbl.grid(row=0, column=0, columnspan=3)

btnEsquerdo = Button(root, text="Esquerda", command= lambda: esquerda(0))
btnEsquerdo.grid(row=1, column=0)

btnSair = Button(root, text="Sair", command=root.quit)
btnSair.grid(row=1, column=1)

btnDireta = Button(root, text="Direita", command= lambda: direita(0))
btnDireta.grid(row=1, column=2)

root.mainloop()
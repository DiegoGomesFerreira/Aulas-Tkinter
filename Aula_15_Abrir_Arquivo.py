from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

def open():
    global lbl
    global img_lbl
    global  imagem
    root.filename = filedialog.askopenfilename(initialdir = "/Aulas-Tkinter", title = "Selecionar Arquivo",
    filetypes = (("png files", "*.png"), ("all files", "*.*")))
    lbl = Label(root, text = root.filename).pack()
    imagem = ImageTk.PhotoImage(Image.open(root.filename))
    img_lbl = Label(image = imagem).pack()
    pass

root = Tk()
root.title("Aula 15")
root.iconbitmap("Terminal.ico")



btn = Button(root, text="Abrir Arquivo", command=open).pack()

root.mainloop()
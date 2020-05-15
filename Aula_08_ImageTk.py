from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Apredendo Tkinter!")
root.iconbitmap("Terminal.ico")
root.geometry("300x300")

img = ImageTk.PhotoImage(Image.open("labrador-head.png"))
label = Label(image=img)
label.pack()

botao_sair = Button(root, text="Sair", command=root.quit)
botao_sair.pack()

print("Diego")

root.mainloop()
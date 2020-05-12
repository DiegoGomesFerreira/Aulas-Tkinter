from tkinter import *

root = Tk()
root.title("Aula 11")
root.geometry("500x500+300+100")
root.iconbitmap("Terminal.ico")

frm = LabelFrame(root, text="Meu FRAME", padx=50, pady=50)
frm.pack(padx=100, pady=100)

btn = Button(frm, text="Não click aqui!", padx=10, pady=10)
btn.pack(padx=10, pady=10)

btn1 = Button(frm, text="Não click aqui!", padx=10, pady=10)
btn1.pack(padx=10, pady=10)

root.mainloop()
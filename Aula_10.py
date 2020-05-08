from tkinter import *

root = Tk()

lbl1 = Label(root, text="Exemplo 1")
lbl1.grid(row=0 , column=0)
lbl1.lift()

lbl2 = Label(root, text="Exemplo 2")
lbl2.grid(row=0 , column=0)
lbl2.lower()

lbl3 = Label(root, text="Exemplo 3")
lbl3.grid(row=0 , column=0)
lbl3.lower()

root.mainloop()
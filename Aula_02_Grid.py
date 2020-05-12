from tkinter import * 

root = Tk()

lbl1 = Label(root, text="Olá mundo!")
lbl2 = Label(root, text="Meu nome é Diego Gomes")
lbl3 = Label(root, text="Outro Label")

lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)
lbl3.grid(row=2, column=1)

root.mainloop()
from tkinter import *

def label2():
    print("label2")
    lbl1.grid_forget()
    lbl3.grid_forget()
    lbl2.grid(row=1, column=0)

def label1():
    print("label1")
    lbl2.grid_forget()
    lbl3.grid_forget()
    lbl1.grid(row=0, column=0)

def label3():
    print("label3")
    lbl1.grid_forget()
    lbl2.grid_forget()
    lbl3.grid(row=0, column=0)


root = Tk()

lbl1 = Label(root, text="Exemplo1")
lbl2 = Label(root, text= "Exemplo2")
lbl3 = Label(root, text= "Exemplo2")

lbl1.grid(row=0, column=0)
lbl2.grid(row=0, column=0)
lbl3.grid(row=0, column=0)

btn1 = Button(root, text="Vá para o Label 2", command=label2)
btn1.grid(row=1, column=0)

btn2 = Button(root, text="Vá para o Label 1", command=label1)
btn2.grid(row=1, column=1)

btn3 = Button(root, text="Vá para o Label 3", command=label3)
btn3.grid(row=1, column=2)
root.mainloop()
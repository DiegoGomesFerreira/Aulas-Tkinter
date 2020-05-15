from tkinter import *
from tkinter import messagebox

def popup():
    # messagebox.showinfo showwarning showerror askquestion askokcancel askyesno
    resposta = messagebox.askquestion("Este é meu popup", "Olá Mundo")

    Label(root, text=resposta).pack()

    """if resposta == 1:
        Label(root, text="Você clicou em Sim").pack()
    else:
        Label(root, text="Você clicou em Não").pack()"""
    pass

root = Tk()
root.title("Aula 13 Message Box")
root.iconbitmap("Terminal.ico")
root.geometry("300x300+100+100")

Button(root, text="Popup", command=popup).pack()

root.mainloop()
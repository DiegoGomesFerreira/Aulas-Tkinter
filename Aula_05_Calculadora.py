from tkinter import *


def botao_igualdade():
    segundo_numero = ety1.get()
    ety1.delete(0, END)

    if matematica == "adicionar":
        ety1.insert(0, int(p_numero) + int(segundo_numero))

    if matematica == "subtrair":
        ety1.insert(0, int(p_numero) - int(segundo_numero))

    if matematica == "multiplicar":
        ety1.insert(0, int(p_numero) * int(segundo_numero))

    if matematica == "dividir":
        ety1.insert(0, int(p_numero) / int(segundo_numero))
    pass

def botao_adicionar():
    primeiro_numero = ety1.get()
    global p_numero
    global matematica
    matematica = "adicionar"
    p_numero = str(primeiro_numero)
    ety1.delete(0, END)
    pass

def botao_subtrair():
    primeiro_numero = ety1.get()
    global p_numero
    global matematica
    matematica = "subtrair"
    p_numero = str(primeiro_numero)
    ety1.delete(0, END)
    pass

def botao_multiplicar():
    primeiro_numero = ety1.get()
    global p_numero
    global matematica
    matematica = "multiplicar"
    p_numero = str(primeiro_numero)
    ety1.delete(0, END)
    pass

def botao_dividir():
    primeiro_numero = ety1.get()
    global p_numero
    global matematica
    matematica = "dividir"
    p_numero = str(primeiro_numero)
    ety1.delete(0, END)
    pass

def botao_limpar():
    ety1.delete(0, END)
    pass

def botao_click(numero):
    valor_atual = ety1.get()
    ety1.delete(0, END)
    ety1.insert(0, str(valor_atual) + str(numero))
    pass


root = Tk()
root.title("Calculadora")

ety1 = Entry(root)
btn0 = Button(root, text="0", padx=15, pady=10, command=lambda: botao_click(0))
btn1 = Button(root, text="1", padx=15, pady=10, command=lambda: botao_click(1))
btn2 = Button(root, text="2", padx=15, pady=10, command=lambda: botao_click(2))
btn3 = Button(root, text="3", padx=15, pady=10, command=lambda: botao_click(3))
btn4 = Button(root, text="4", padx=15, pady=10, command=lambda: botao_click(4))
btn5 = Button(root, text="5", padx=15, pady=10, command=lambda: botao_click(5))
btn6 = Button(root, text="6", padx=15, pady=10, command=lambda: botao_click(6))
btn7 = Button(root, text="7", padx=15, pady=10, command=lambda: botao_click(7))
btn8 = Button(root, text="8", padx=15, pady=10, command=lambda: botao_click(8))
btn9 = Button(root, text="9", padx=15, pady=10, command=lambda: botao_click(9))

btnLimpar = Button(root, text="Limpar", padx=10, pady=10, command=botao_limpar)

btnAdicionar = Button(root, text="+", padx=25, pady=10, command=botao_adicionar)
btnSubtrarir = Button(root, text="-", padx=25, pady=10, command=botao_subtrair)
btnMultiplicar = Button(root, text="*", padx=25, pady=10, command=botao_multiplicar)
btnDividir = Button(root, text="/", padx=25, pady=10, command=botao_dividir)

btnIgualdade = Button(root, text="=", padx=36, pady=10, command=botao_igualdade)

ety1.grid(row=0, column=0, columnspan=3)
btn0.grid(row=4 ,column=0)
btn1.grid(row=3 ,column=0)
btn2.grid(row=3 ,column=1)
btn3.grid(row=3 ,column=2)
btn4.grid(row=2 ,column=0)
btn5.grid(row=2 ,column=1)
btn6.grid(row=2 ,column=2)
btn7.grid(row=1 ,column=0)
btn8.grid(row=1 ,column=1)
btn9.grid(row=1 ,column=2)

btnLimpar.grid(row=0, column=3)

btnAdicionar.grid(row=1, column=3)
btnSubtrarir.grid(row=2, column=3)
btnMultiplicar.grid(row=3, column=3)
btnDividir.grid(row=4, column=3)

btnIgualdade.grid(row=4, column=1, columnspan=2)

root.mainloop()
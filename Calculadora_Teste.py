from tkinter import *

Calculadora = Tk()

Calculadora.title("Calculadora Python")

Calculadora.geometry("400x400+450+150")

Calculadora.resizable(False, False)

Calculadora['bg'] = "#B0C4DE"

bordaBotao = 7
Fonte = "Arial 28"

def Botao_Num(Numero):
	Click = Resposta.get()
	Resposta.delete(0,END)
	Resposta.insert(END, str(Click) + str(Numero))
def Botao_Virgula():
	Resposta.insert(END, ".")

def Botao_Deleta():
	Resposta.delete(0,END)

def Botao_Soma():
	P1N = Resposta.get()
	global Pnum
	global mat
	mat = "Soma"
	Pnum = float(P1N)
	Resposta.delete(0,END)

def Botao_Subtracao():
	P1N = Resposta.get()
	global Pnum
	global mat
	mat = "Subtracao"
	Pnum = float(P1N)
	Resposta.delete(0,END)

def Botao_Divisao():
	P1N = Resposta.get()
	global Pnum
	global mat
	mat = "Divisao"
	Pnum = float(P1N)
	Resposta.delete(0,END)

def Botao_Multiplica():
	P1N = Resposta.get()
	global Pnum
	global mat
	mat = "Multiplica"
	Pnum = float(P1N)
	Resposta.delete(0,END)

def Botao_Igual():
	S1N = Resposta.get()
	Resposta.delete(0,END)
	if mat == "Soma":
		Resposta.insert(0, Pnum + float(S1N))
	if mat == "Subtracao":
		Resposta.insert(0, Pnum - float(S1N))
	if mat == "Divisao":
		Resposta.insert(0, Pnum / float(S1N))
	if mat == "Multiplica":
		Resposta.insert(0, Pnum * float(S1N))				

Resposta = Entry(Calculadora,cursor= "arrow", text = "Resposta", width = 10 , font = Fonte, bd=10, relief = "sunken")

Botao0 = Button(Calculadora, text = "0", padx=5, font= "ArialBlack 24", bd = bordaBotao, relief="raised", command=lambda: Botao_Num(0))
Botao1 = Button(Calculadora, text = "1", font = Fonte, bd = bordaBotao, relief = "raised", command=lambda: Botao_Num(1))
Botao2 = Button(Calculadora, text = "2", font = Fonte, bd = bordaBotao, relief = "raised", command=lambda: Botao_Num(2))
Botao3 = Button(Calculadora, text = "3", font = Fonte, bd = bordaBotao, relief = "raised", command=lambda: Botao_Num(3))
Botao4 = Button(Calculadora, text = "4", font = Fonte, bd = bordaBotao, relief = "raised", command=lambda: Botao_Num(4))
Botao5 = Button(Calculadora, text = "5", font = Fonte, bd = bordaBotao, relief = "raised", command=lambda: Botao_Num(5))
Botao6 = Button(Calculadora, text = "6", font = Fonte, bd = bordaBotao, relief = "raised", command=lambda: Botao_Num(6))
Botao7 = Button(Calculadora, text = "7", font = Fonte, bd = bordaBotao, relief = "raised", command=lambda: Botao_Num(7))
Botao8 = Button(Calculadora, text = "8", font = Fonte, bd = bordaBotao, relief = "raised", command=lambda: Botao_Num(8))
Botao9 = Button(Calculadora, text = "9", font = Fonte, bd = bordaBotao, relief = "raised", command=lambda: Botao_Num(9))
BotaoSoma = Button(Calculadora, text = "+",width = 0 , font = Fonte, bd = bordaBotao, relief = "raised", command=Botao_Soma)
BotaoMenos = Button(Calculadora, text = "-",width = 2 , font = Fonte, bd = bordaBotao, relief = "raised", command=Botao_Subtracao)
Botaox = Button(Calculadora, text = "x",width = 0 , font = Fonte, bd = bordaBotao, relief = "raised", command=Botao_Multiplica)
BotaoDivide = Button(Calculadora, text = "/",width = 2 , font = Fonte, bd = bordaBotao, relief = "raised", command=Botao_Divisao)
BotaoIgual = Button(Calculadora, text = "=",width = 0 , font = Fonte, bd = bordaBotao, relief = "raised", command=Botao_Igual)
BotaoApaga = Button(Calculadora, text = "C", padx=20, pady=20, bd = bordaBotao, relief="raised", command=Botao_Deleta)
BotaoVirgula = Button(Calculadora, text = ",", padx=10,font= "ArialBlack 24", bd = bordaBotao, relief="raised", command=Botao_Virgula)

Resposta.place(x=51, y=5)
Botao0.place(x=211, y=325)
Botao1.place(x=71, y=240)
Botao2.place(x=141, y=240)
Botao3.place(x=211, y=240)
Botao4.place(x=71, y=160)
Botao5.place(x=141, y=160)
Botao6.place(x=211, y=160)
Botao7.place(x=71, y=80)
Botao8.place(x=141, y=80)
Botao9.place(x=211, y=80)
BotaoSoma.place(x = 300, y = 0)
BotaoMenos.place(x=300, y = 80)
Botaox.place(x=300, y = 160)
BotaoDivide.place(x=300, y = 240)
BotaoIgual.place(x=300, y = 320)
BotaoApaga.place(x=71, y = 325)
BotaoVirgula.place(x=141, y=325)

J = Label(Calculadora, text="J", padx = 5, pady = 0, font="Verdana 56", bd = 1, relief="ridge", bg="#4169E1")
e = Label(Calculadora, text="E", padx = 5, pady = 0, font="Verdana 46", bd = 1, relief="ridge", bg="#363636") 
su = Label(Calculadora, text="S", padx = 5, pady = 0, font="Verdana 46", bd = 1, relief="ridge", bg="#00CED1")
u = Label(Calculadora, text="U", padx = 5, pady = 0, font="Verdana 46", bd = 1, relief="ridge", bg="#BC8F8F")
ss = Label(Calculadora, text="S", padx = 5, pady = 0, font="Verdana 46", bd = 1, relief="ridge", bg="#FFD700")

J.place(x=1, y= 2)
e.place(x=2, y=100)
su.place(x=2, y=170)
u.place(x=2, y= 240)
ss.place(x=2 , y= 320)

Calculadora.mainloop()

# By Gabriel Logan
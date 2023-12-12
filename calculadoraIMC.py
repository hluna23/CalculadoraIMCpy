from tkinter import *
from tkinter import ttk

#colores----

cor0 = '#773186'
cor1 = '#7FFFD4'
cor2 = '#FFDB80'

calculadoraIMC = Tk()
calculadoraIMC.title('')
calculadoraIMC.geometry('300x240')
calculadoraIMC.configure(bg='#7FFFD4')

#-------dividiendo la ventana en dos partes------

frame_arriba = Frame(calculadoraIMC, width=350, height=50, bg=cor1, pady= 0, padx=0, relief='flat')
frame_arriba.grid(row=0, column=0, sticky=NSEW)

frame_abajo= Frame(calculadoraIMC, width=350, height=50, bg=cor1, pady= 0, padx=0, relief='flat')
frame_abajo.grid(row=1, column=0, sticky=NSEW)

#-----configurando frame arriba-----

nombre_App = Label(frame_arriba, text='Calculadorea IMC', width=23, height=1, relief='flat', anchor='center', font=('arial 16 bold'), bg=cor1, fg=cor0)
nombre_App.place(x=0, y=0)

nombre_linea = Label(frame_arriba, width=400, relief='flat', anchor='center', font=('arial 1'), bg=cor0, fg=cor0)
nombre_linea.place(x=0, y=35)

    #----calculos----
def calcular():
    peso = float(peso_e.get())
    altura = float(altura_e.get())
    imc = peso / altura**2
    resultado = imc
    if resultado < 18.5:
        resultado_text_l['text'] = 'você esta baixo de Peso (garu 0)'
    elif resultado >= 18.5 and resultado <= 25:
        resultado_text_l['text'] = 'você tem um peso normal (garu 0)'
    elif resultado >= 25 and resultado <=30:
        resultado_text_l['text'] = 'você tem sobre peso (garu I)'
    elif resultado >=30 and resultado <= 35:
        resultado_text_l['text'] = 'vocé tem Obesidade (garu II)'   
    else:
        resultado_text_l['text'] = 'você tem Obesidade Grave (garu III)'

    resultado_l['text'] = "{:.{}f}".format(resultado, 2)

#-----configurando frame abajo-----
peso_l = Label(frame_abajo, text='Peso(Kg)', height=1, relief='flat', anchor='center', font=('arial 10'), bg=cor1, fg=cor0)
peso_l.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

peso_e = Entry(frame_abajo, width=5, relief='solid', font=('arial 10'), justify='center')
peso_e.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

altura_l = Label(frame_abajo, text='Altura(M)', height=1, relief='flat', anchor='center', font=('arial 10'), bg=cor1, fg=cor0)
altura_l.grid(row=1, column=0, sticky=NSEW, pady=1, padx=3)

altura_e = Entry(frame_abajo, width=5, relief='solid', font=('arial 10'), justify='center')
altura_e.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

resultado_l = Label(frame_abajo, text='', width=7, height=1, padx=6, pady=16, relief='flat', anchor='center', font=('arial 24 bold'), bg=cor2, fg=cor0)
resultado_l.place(x=130, y=10)

resultado_text_l = Label(frame_abajo, text='seu imc é', width=37, height=1, padx=0, pady=20, relief='flat', anchor='center', font=('arial 10 bold'), bg=cor1, fg=cor0)
resultado_text_l.place(x=0, y=85)

b_calcular = Button(frame_abajo, command=calcular, text='Calcular', width=34, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('arial 10 bold'), bg=cor1, fg=cor0)
b_calcular.grid(row=4, column=0, sticky=NSEW, padx=8, pady=60, columnspan=30)


calculadoraIMC.mainloop()
 
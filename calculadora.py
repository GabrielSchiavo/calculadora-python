from tkinter import *
from tkinter import ttk

# Cores
color1 = "#202020"
color2 = "#ffffff"
color3 = "#323232"
color4 = "#3c3c3c"
color5 = "#4cc2ff"
color6 = "#47b1e8"
color7 = "#000000"

# Configuração da janela
window = Tk()
window.iconbitmap("./assets/img/icon.ico")
window.title("Calculadora")
window.geometry("323x440")
window.config(bg=color1)

# Fremes
frameDisplay = Frame(window, width=323, height=120, bg=color2)
frameDisplay.grid(row=0, column=0)

frameKeyboard = Frame(window, width=323, height=295, bg=color1)
frameKeyboard.grid(row=1, column=0)

frameFooter = Frame(window, width=323, height=15, bg=color1)
frameFooter.grid(row=2, column=0)


# Funções
showValue = StringVar()
values = ''

def inputValue(event):
   global values
   
   values = values + str(event)
   
   #Exibe o resultado na tela
   showValue.set(values)


def calculate():
   global values
   
   result = eval(values)
   showValue.set(str(result))
   values = str(result)


def clean():
   global values
   
   values = ''
   showValue.set('')
   

# Label
labelScreen = Label(frameDisplay, textvariable=showValue, bg=color1, fg=color2, font=("Ivy 24 bold"), width=16, padx=8, pady=40, justify="right", anchor="e", relief="flat")
labelScreen.pack()

labelFooter = Label(frameFooter, text="V.: 1.2.4", bg=color1, fg=color2, font=("Ivy 9"), width=44, padx=8, justify="right", anchor="e")
labelFooter.pack()


# Botões
btn19 = Button(frameKeyboard, command = lambda: inputValue('MC'), text="MC", width=7, height=2, bg=color1, fg=color2, font=("Ivy 10 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn19.place(x=0, y=5)

btn19 = Button(frameKeyboard, command = lambda: inputValue('MR'), text="MR", width=7, height=2, bg=color1, fg=color2, font=("Ivy 10 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn19.place(x=65, y=5)

btn20 = Button(frameKeyboard, command = lambda: inputValue('M-'), text="M-", width=7, height=2, bg=color1, fg=color2, font=("Ivy 10 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn20.place(x=130, y=5)

btn21 = Button(frameKeyboard, command = lambda: inputValue('M+'), text="M+", width=7, height=2, bg=color1, fg=color2, font=("Ivy 10 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn21.place(x=195, y=5)


btn1 = Button(frameKeyboard, command = clean, text="C", width=17, height=2, bg=color3, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn1.place(x=0, y=49)

btn2 = Button(frameKeyboard, command = lambda: inputValue('%'), text="%", width=8, height=2, bg=color3, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn2.place(x=162, y=49)

btn3 = Button(frameKeyboard, command = lambda: inputValue('/'), text="/", width=8, height=2, bg=color3, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn3.place(x=243, y=49)


btn4 = Button(frameKeyboard, command = lambda: inputValue('7'), text="7", width=8, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn4.place(x=0, y=98)

btn5 = Button(frameKeyboard, command = lambda: inputValue('8'), text="8", width=8, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn5.place(x=81, y=98)

btn6 = Button(frameKeyboard, command = lambda: inputValue('9'), text="9", width=8, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn6.place(x=162, y=98)

btn7 = Button(frameKeyboard, command = lambda: inputValue('*'), text="x", width=8, height=2, bg=color3, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn7.place(x=243, y=98)


btn8 = Button(frameKeyboard, command = lambda: inputValue('4'), text="4", width=8, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn8.place(x=0, y=147)

btn9 = Button(frameKeyboard, command = lambda: inputValue('5'), text="5", width=8, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn9.place(x=81, y=147)

btn10 = Button(frameKeyboard, command = lambda: inputValue('6'), text="6", width=8, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn10.place(x=162, y=147)

btn11 = Button(frameKeyboard, command = lambda: inputValue('-'), text="-", width=8, height=2, bg=color3, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn11.place(x=243, y=147)


btn12 = Button(frameKeyboard, command = lambda: inputValue('1'), text="1", width=8, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn12.place(x=0, y=196)

btn13 = Button(frameKeyboard, command = lambda: inputValue('2'), text="2", width=8, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn13.place(x=81, y=196)

btn14 = Button(frameKeyboard, command = lambda: inputValue('3'), text="3", width=8, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn14.place(x=162, y=196)

btn15 = Button(frameKeyboard, command = lambda: inputValue('+'), text="+", width=8, height=2, bg=color3, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn15.place(x=243, y=196)


btn16 = Button(frameKeyboard, command = lambda: inputValue('0'), text="0", width=17, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn16.place(x=0, y=245)

btn17 = Button(frameKeyboard, command = lambda: inputValue('.'), text=".", width=8, height=2, bg=color4, fg=color2, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn17.place(x=162, y=245)

btn18 = Button(frameKeyboard, command = calculate, text="=", width=8, height=2, bg=color5, fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color6, activeforeground=color7, highlightthickness=0, borderwidth=0)
btn18.place(x=243, y=245)


window.mainloop()

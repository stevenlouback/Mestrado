from tkinter import *

def Tela():
    hello.set("Olá, Mundo!")

gui = Tk()

gui.title("Titulo da Tela")
gui.geometry("400x300")

btn = Button(gui, text="Tela", command=Tela)
btn.pack()

hello = StringVar()
lbl = Label(gui, textvariable=hello)
lbl.pack()

gui.mainloop()
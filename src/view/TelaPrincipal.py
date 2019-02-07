from tkinter import *




class TelaPrincipal(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        # Configuração da janela principal
        self.master.title('Tela Principal')
        self.master.geometry('800X600')
        self.configure(borderwidth=4)
        self.configure(background='white')

        for name in ("Amostras", "Modelos", "Análise"):
            self.button = Button(self, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Empacotamos o frame principal
        self.pack(fill='both', expand=True)



        def handle_event(self, event):
            btn_name = event.widget.cget('text')
            if btn_name.endswith('Amostras'):
                #window = a
               # window.mainloop()



mainWindow = TelaPrincipal()
mainWindow.mainloop()


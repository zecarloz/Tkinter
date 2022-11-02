from tkinter import *

janela = Tk()
janela.title('Olá Mundo')
janela.geometry('600x250')
janela.config(bg='#f9ec54')

janela.iconphoto(False, PhotoImage(file='logo.png'))
janela.resizable(width=False , height=False)

janela.mainloop()
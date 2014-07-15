#! -*- coding: cp1252 -*-

from metrometro import Metrometro
from tkinter import *

class Gui_metrometro(object):

    def __init__(self, instancia_de_Tk):
        self.estado_metrometro = False
        #--- inicializa os fremes -------
        self.frameTitle = Frame(instancia_de_Tk)
        self.frameTitle.pack()

        self.frameN2 = Frame(instancia_de_Tk)
        self.frameN2.pack()
        self.frameMedia = Frame(instancia_de_Tk)
        self.frameMedia.pack()
        
        #---- titulo ---
        cor = '#660066'
        fonteNomes = ('Verdana', '10', 'bold')
        fonteCampos = ('Verdana', '8')
        Label(self.frameTitle, text = 'Metrometro', fg = '#3366FF', height = 3, width = 20,
              font = ('Verdana', '14')).pack()
 
        #---- Frequencia ----
        Label(self.frameN2, text = 'Frequicia ', font = fonteNomes, fg = cor,
              width = 10).pack(side = LEFT)
        self.campoN2 = Entry(self.frameN2, font = fonteCampos, width = 3)
        self.campoN2.pack(side = LEFT)
        
        #---- Botoes  -------
        self.botComecar = Button(self.frameMedia, text = 'Começar', font = fonteNomes,
                               bg = '#CCCCCA',  width = 8, command = self.metro)
        self.botComecar.pack(side = LEFT)
        self.botParar = Button(self.frameMedia, text = 'Parar', font = fonteNomes,
                              bg = '#CCCCCA', width = 8, command = self.pare)
        self.botParar.pack(side = LEFT)

    def metro(self):
        
        self.ap_metrometro = Metrometro(float(self.campoN2.get()))
        self.ap_metrometro.start()
        
        

    def pare(self):
        self.ap_metrometro.pare = False


raiz = Tk()
Gui_metrometro(raiz)
raiz.mainloop()

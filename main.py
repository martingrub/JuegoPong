#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import pygame
from pygame.locals import *
opcion = ""

def setopcion(op): 
	global opcion
	opcion=op
	global window
	if opcion=="1":
		window.destroy()
		import PongIA.py		
		
	elif opcion=="2":
		window.destroy()
		import PongMultiplayer.py
			
""" ######################### 
            WINDOW 
    ######################### 
"""  
  
# Declarem l'objecte Tkinter a la variable window.  
window = Tk()  
  
# Títol de la finestra  
window.title("La meva primera interfície")  
  
# Permet la redirecció de la finestra  
window.resizable(True, True) #(1,0) / (True False)  
  
# El mètode config ens permet canviar molts aspectes de la nostra finestra  
window.config(bg="white")  
  
# Mida de la finestra  
window.geometry("400x200")

""" ######################### 
            FRAME 
    ######################### 
"""  
textLog = StringVar() 
# Contenidor de widgets que ha d'anar dins de l'arrel de la interfície. S'adaptarà a la mida del contenidor "pare"  
frame = Frame()  
frame.pack()  
# Empaquetar el frame dins l'arrel window.   
frame.pack(expand="True")  
  
# Configuracions del frame. 
frame.config(bg="black")

""" ######################### 
            BUTTON 
    ######################### 
"""  
def callback():  
    print('click!')
button = Button(frame,background="orange", text="Un Jugador",command=lambda:setopcion("1"), width=15) 
button.grid(row=0, column=0,padx=2)

button = Button(frame,background="orange", text="Multiplayer",command=lambda:setopcion("2"), width=15) 
button.grid(row=1, column=0,padx=2) 

    
window.mainloop()

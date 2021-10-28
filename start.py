#IMPORTING THE REQUIRED MODULES
from tkinter import *
import random
from tkinter import messagebox

#DEFINING GUI WINDOW
window=Tk()
window.title("STONE PAPER SCISSOR GAME")
window.geometry("350x250")

#DEFINING FRAMES
frame1=Frame(window)
frame1.pack(side=TOP)

frame2=Frame(window)
frame2.pack(side=TOP)

#DEFINING FUNCTIONS
def start():
	window.destroy()
	import gui
	
def Exit():
		ans=messagebox.askyesnocancel("Confirmation","Are you sure want to exit?")
		if(ans==True):
			window.destroy()
	
#LABELES AND BUTTONS
Label1=Label(frame1,fg="Dark blue",text="STONE PAPER SCISSOR",font=('algerian',20,'bold'))
Label1.grid(row=1,column=1)

Start_button=Button(frame2,text="START",fg="Yellow",bg="Black",activebackground="Green",command=start)
Start_button.grid(row=1,column=1)

Exit_button=Button(frame2,text="EXIT",fg="YELLOW",bg="BLACK",activebackground="GREEN",command=Exit)
Exit_button.grid(row=2,column=1)

window.mainloop()
#IMPORTING REQUIRED MODULES
from tkinter import *
import random
from tkinter import messagebox

#DEFINING GUI WINDOW
window=Tk()
window.title("Gaming window")
window.geometry("850x400")

#FRAMES FOR GUI WINDOW
frame1=Frame(window)
frame1.pack(side=TOP)

frame2=Frame(window)
frame2.pack(side=TOP)

#DECLARING VARIABLES
ScoreMe_variable=IntVar()
ScoreComp_variable=IntVar()
#INITIALIZING VARIABLES
ScoreMe_variable.set('0')
ScoreComp_variable.set('0')
click=True

Rock=PhotoImage(file="Rock.png")
Paper=PhotoImage(file="Paper.png")
Scissor=PhotoImage(file="Scissor.png")

Rockpic=PhotoImage(file="rocks.png")
Paperpic=PhotoImage(file="papers.png")
Scissorpic=PhotoImage(file="scissors.png")

Tie=PhotoImage(file="Tie.png")
Youwin=PhotoImage(file="win.png")
Youloose=PhotoImage(file="loose.png")

#DEFINING FUNCTIONS
def Back():
	ans=messagebox.askyesnocancel("Confirmation","Are you sure want to back?")
	if(ans==True):
		window.destroy()
		import start
		
def Comp_Choice():
		choice=random.choice(['rock','paper','scissor'])
		return choice
		
def Exit():
		ans=messagebox.askyesnocancel("Confirmation","Are you sure want to exit?")
		if(ans==True):
			window.destroy()


def Endgame(a):
	
	#IF ANYONE(HUMAN OR COMPUTER) REACHES 3 WINS FIRST THEN GAME ENDS AND WINNER DECLARED
	if(a==3):
		b=messagebox.askyesnocancel("WIN","HURRAH YOU WON,Do you want to play again?")
		if(b):
			window.destroy()
			import gui
		else:
			window.destroy()
			import start
	else:
		b=messagebox.askyesnocancel("LOOSE","OOPS YOU LOOSE,Do you want to play again?")
		if(b):
			window.destroy()
			import gui
		else:
			window.destroy()
			import start


def startgame(Yourchoice):
	global click
	compchoice=Comp_Choice()
	
	if(click==True):
		if(Yourchoice=="rock"):
			Button1.configure(image=Rockpic)
			click=False
			if(compchoice=="rock"):
				Button2.configure(image=Rockpic)
				Button3.configure(image=Tie)
			elif(compchoice=="paper"):
				Button2.configure(image=Paperpic)
				Button3.configure(image=Youloose)
				ScoreComp_variable.set(ScoreComp_variable.get()+1)
			else:
					Button2.configure(image=Scissorpic)
					Button3.configure(image=Youwin)
					ScoreMe_variable.set(ScoreMe_variable.get()+1)
		if(Yourchoice=="paper"):
			Button1.configure(image=Paperpic)
			click=False
			if(compchoice=="paper"):
				Button2.configure(image=Paperpic)
				Button3.configure(image=Tie)
			elif(compchoice=="rock"):
				Button2.configure(image=Rockpic)
				Button3.configure(image=Youwin)
				ScoreMe_variable.set(ScoreMe_variable.get()+1)
			else:
				Button2.configure(image=Scissorpic)
				Button3.configure(image=Youloose)
				ScoreComp_variable.set(ScoreComp_variable.get()+1)
				
		if(Yourchoice=="scissor"):
			Button1.configure(image=Scissorpic)
			click=False
			if(compchoice=="scissor"):
				Button2.configure(image=Scissorpic)
				Button3.configure(image=Tie)
			elif(compchoice=="rock"):
				Button2.configure(image=Rockpic)
				Button3.configure(image=Youloose)
				ScoreComp_variable.set(ScoreComp_variable.get()+1)
			else:
				Button2.configure(image=Paperpic)
				Button3.configure(image=Youwin)
				ScoreMe_variable.set(ScoreMe_variable.get()+1)
	else:
		Button1.configure(image=Rock)
		Button2.configure(image=Paper)
		Button3.configure(image=Scissor)
		click=True
	if(ScoreMe_variable.get()==3 or ScoreComp_variable.get()==3):
		Endgame(ScoreMe_variable.get())
	


	
#DEFINING LABELS ENTRYFIELDS AND BUTTONS
Label1=Label(frame1,fg="BLUE",text="YOUR SCORE:",font=('algerian',10,'bold'))
Label1.grid(row=1,column=1)
Label_MyScore=Label(frame1,textvariable=ScoreMe_variable)
Label_MyScore.grid(row=1,column=2)

Label2=Label(frame1,fg="GREEN",text="COMPUTER SCORE:",font=('algerian',10,'bold'))
Label2.grid(row=2,column=1)
Label_CompScore=Label(frame1,textvariable=ScoreComp_variable)
Label_CompScore.grid(row=2,column=2)

Label3=Label(frame1,fg="BLACK",text="Choose your choice",font=('bold',10,'bold'))
Label3.grid(row=3,column=1)

Button1=Button(frame2,image=Rock,fg="Yellow",bg="Black",activebackground="Green",command=lambda:startgame("rock"))
Button1.grid(row=2,column=1)

Button2=Button(frame2,image=Paper,fg="Yellow",bg="Black",activebackground="Green",command=lambda:startgame("paper"))
Button2.grid(row=2,column=2)

Button3=Button(frame2,image=Scissor,fg="Yellow",bg="Black",activebackground="Green",command=lambda:startgame("scissor"))
Button3.grid(row=2,column=3)

Back_button=Button(frame2,text="BACK",fg="Yellow",bg="Black",activebackground="Green",command=Back)
Back_button.grid(row=3,column=2)

Exit_button=Button(frame2,text="EXIT",fg="YELLOW",bg="BLACK",activebackground="GREEN",command=Exit)
Exit_button.grid(row=3,column=3)

window.mainloop()

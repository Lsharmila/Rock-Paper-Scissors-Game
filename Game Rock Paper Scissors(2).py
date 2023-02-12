#Welcome to Game Rock Paper and Scissors!
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from random import randint
window = Tk()
window.title("Game Rock Paper and Scissor")
window.configure(background="hotpink3")
#images
image_rock1=ImageTk.PhotoImage(Image.open("rock2.png"))
image_paper1=ImageTk.PhotoImage(Image.open("paper2.png"))
image_scissor1=ImageTk.PhotoImage(Image.open("scissor2.png"))
image_rock2=ImageTk.PhotoImage(Image.open("rock1.png"))
image_paper2=ImageTk.PhotoImage(Image.open("paper1.png"))
image_scissor2=ImageTk.PhotoImage(Image.open("scissor1.png"))
#label
label_player=Label(window,image=image_scissor1)
label_computer=Label(window,image=image_scissor2)
label_computer.grid(row=1,column=1)
label_player.grid(row=1,column=3)
#score
computer_score=Label(window,text=0,font=('arial',60,"bold"),fg="darkorchid3")
computer_score.grid(row=0,column=1)
player_score=Label(window,text=0,font=('arial',60,"bold"),fg="darkorchid3")
player_score.grid(row=0,column=3)
#indicator
player_indicator=Label(window,text="PLAYER",font=('arial',40,"bold"),bg="purple",fg="violet")
player_indicator.grid(row=0,column=4)
computer_indicator=Label(window,text="COMPUTER",font=('arial',40,"bold"),bg="purple",fg="violet")
computer_indicator.grid(row=0,column=0)
#final result updation
def updateMessage(a):
    final_message['text']=a
#computer score updation
def computer_update():
    final=int(computer_score['text'])
    final+=1
    computer_score["text"]=str(final)
#player score updation
def player_update():
    final =int(player_score['text'])
    final +=1
    player_score["text"]=str(final)
#Deciding the Winner
def winner_check(p,c):
    if p==c:
        updateMessage("It's a tie!!")
    elif p=="rock":
        if c=="paper":
            updateMessage("Computer Wins!!")
            computer_update()
        else:
            updateMessage("Player Wins!!")
            player_update()
    elif p=="paper":
        if c=="scissor":
            updateMessage("Computer Wins!!")
            computer_update()
        else:
            updateMessage("Player Wins!!")
            player_update()
    elif p == "scissor":
        if c == "rock":
            updateMessage("Computer Wins!!")
            computer_update()
        else:
            updateMessage("Player Wins!!")
            player_update()
    else:
        pass

to_select=["rock","paper","scissor"]
def choice_update(a):
    choice_computer = to_select[randint(0,2)]
    if choice_computer=="rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer=="paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)
        
    if a=="rock":

        label_player.configure(image=image_rock1)
    elif a=="paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)
        
    winner_check(a, choice_computer)            
#results
final_message= Label(window,font=("arial",25,"bold"),bg="purple",fg="pink")
final_message.grid(row=4,column=2)
#buttons
button_rock=Button(window,width=16, height=3,text="ROCK",
                   font=("arial",20,"bold"),bg="pink",fg="purple",command=lambda:choice_update("rock")).grid(row=2,column=1)
button_paper=Button(window,width=16,height=3,text="PAPER",
                font=("arial",20,"bold"),bg="pink",fg="purple",command=lambda:choice_update("paper")).grid(row=2,column=2)
button_scissor=Button(window,width=16,height=3,text="SCISSOR",
                 font=("arial",20,"bold"),bg="pink",fg="purple",command=lambda:choice_update("scissor")).grid(row=2,column=3)
window.mainloop()

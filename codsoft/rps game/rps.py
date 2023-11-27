from tkinter import *
from PIL import Image, ImageTk
from random import choice

window = Tk()
window.title("Rock paper scissor game by dhanush")
window.config(background="#9EB8D9")

image_rock1 = ImageTk.PhotoImage(Image.open("rright.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("pright.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("sright.png"))

image_rock2 = ImageTk.PhotoImage(Image.open("rleft.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("pleft.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("sleft.png"))

label_player = Label(window, image=image_scissor1)
label_computer = Label(window, image=image_scissor2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

player_indicator = Label(window, font=("arial", 40, "bold"), text="PLAYER", bg="black", fg="orange")
computer_indicator = Label(window, font=("arial", 40, "bold"), text="COMPUTER", bg="black", fg="orange")
player_indicator.grid(row=0, column=3)
computer_indicator.grid(row=0, column=1)

def updateMessage(message):
    final_message['text'] = message

def Computer_Update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)

def player_Update():
    final = int(player_score['text'])
    final += 1
    player_score["text"] = str(final)

def winner_check(player_choice, computer_choice):
    if player_choice == computer_choice:
        updateMessage("It's a tie")
    elif player_choice == "rock":
        if computer_choice == "paper":
            updateMessage("Computer Wins")
            Computer_Update()
        else:
            updateMessage("Player wins")
            player_Update()
    elif player_choice == "paper":
        if computer_choice == "scissor":
            updateMessage("Computer wins")
            Computer_Update()
        else:
            updateMessage("Player wins")
            player_Update()
    elif player_choice == "scissor":
        if computer_choice == "rock":
            updateMessage("Computer wins")
            Computer_Update()
        else:
            updateMessage("Player wins")
            player_Update()

to_select = ["rock", "paper", "scissor"]

def choice_update(player_choice):
    computer_choice = choice(to_select)
    update_images(player_choice, computer_choice)
    winner_check(player_choice, computer_choice)

def update_images(player_choice, computer_choice):
    label_player.configure(image=eval(f"image_{player_choice}1"))
    label_computer.configure(image=eval(f"image_{computer_choice}2"))

final_message = Label(window, font=("arial", 40, "bold"), bg="green", fg="black")
final_message.grid(row=3, column=2)

computer_score = Label(window, text=0, font=('arial', 60, "bold"), fg="blue")
player_score = Label(window, text=0, font=('arial', 60, "bold"), fg="blue")
player_score.grid(row=1, column=3)
computer_score.grid(row=1, column=1)

button_rock = Button(window, width=16, height=3, text="ROCK", font=("arial", 20, "bold"), bg="black", fg="orange",
                     command=lambda: choice_update("rock")).grid(row=2, column=1)
button_paper = Button(window, width=16, height=3, text="PAPER", font=("arial", 20, "bold"), bg="black", fg="orange",
                      command=lambda: choice_update("paper")).grid(row=2, column=2)
button_scissors = Button(window, width=16, height=3, text="SCISSOR", font=("arial", 20, "bold"), bg="black",
                         fg="orange", command=lambda: choice_update("scissor")).grid(row=2, column=3)

window.mainloop()

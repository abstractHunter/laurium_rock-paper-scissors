
import random
import tkinter
from tkinter import ttk

from PIL import Image, ImageTk

possibilities = ('rock', 'paper', 'scissors')
player_score = 0
computer_score = 0


# *************************************** Functions *********************************************

# game logic
def final_result(player, computer):
    global computer_score, player_score, result

    if player == computer:
        result = "Draw"

    elif player == "rock":
        if computer == "paper":
            result = "You lose"
            computer_score += 1
        else:
            result = "You win"
            player_score += 1

    elif player == "paper":
        if computer == "scissors":
            result = "You lose"
            computer_score += 1
        else:
            result = "You win"
            player_score += 1

    elif player == "scissors":
        if computer == "rock":
            result = "You lose"
            computer_score += 1
        else:
            result = "You win"
            player_score += 1

    # configuring the window
    result_text.config(text=result)
    pl.config(text=f"Player:{player_score}")
    cp.config(text=f"Computer:{computer_score}")


# resize images
def image_resizing(file_path):
    img = Image.open(file_path)
    resized_image = img.resize((240, 240))
    image = ImageTk.PhotoImage(resized_image)
    return image


# computer choice
def computer_choice():
    comput = random.choice(possibilities)
    computer_image = image_resizing(f"images/{comput}.png")
    computer_result.config(image=computer_image)
    computer_result.image = computer_image
    return comput


# when the player chooses an image/option
def rock_chosen():
    player_image = image_resizing("images/rock.png")
    player_result.config(image=player_image)
    player_result.image = player_image
    player = "rock"

    # computer choice
    computer = computer_choice()

    final_result(player, computer)


def paper_chosen():
    player_image = image_resizing("images/paper.png")
    player_result.config(image=player_image)
    player_result.image = player_image
    player = 'paper'

    # computer choice
    computer = computer_choice()

    final_result(player, computer)


def scissors_chosen():
    player_image = image_resizing("images/scissors.png")
    player_result.config(image=player_image)
    player_result.image = player_image
    player = 'scissors'

    # computer choice
    computer = computer_choice()

    final_result(player, computer)


# *********************************** Application window *********************************************

root = tkinter.Tk()
root.title(" Rock - Paper - Scissors ")

# window dimensions
window_width = 800
window_height = 600

# screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# finding the center point of the screen
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# window size and position
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)


# ******************************************** Widgets *************************************************

# frame to display chosen options and result
result_frame = ttk.Frame(root)
result_frame.pack(expand=True)

player_result = ttk.Label(result_frame)
player_result.pack(padx=25, pady=20, ipadx=10, ipady=10, side="left")

result_text = ttk.Label(result_frame, font=('Courier', 30, 'bold'))
result_text.pack(side="left")

computer_result = ttk.Label(result_frame)
computer_result.pack(padx=25, pady=20, ipadx=10, ipady=10, side="right")


# frame to display scores
score_frame = ttk.Frame()
score_frame.pack(fill="x")

pl = ttk.Label(score_frame, text=f"Player:{player_score}", font=('Courier', 25, 'bold'))
pl.pack(side='left', expand=True)
cp = ttk.Label(score_frame, text=f"Computer:{computer_score}", font=('Courier', 25, 'bold'))
cp.pack(side='right', expand=True)


# frame to display choices that can be made
choice_frame = ttk.Frame()
choice_frame.pack()

rock_image = tkinter.PhotoImage(file="images/rock.png")
rock_choice = ttk.Button(choice_frame, image=rock_image, text="Rock", compound="top", command=rock_chosen)
rock_choice.pack(padx=30, pady=20, ipadx=10, ipady=10, side="left")

paper_image = tkinter.PhotoImage(file="images/paper.png")
paper_choice = ttk.Button(choice_frame, image=paper_image, text="Paper", compound="top", command=paper_chosen)
paper_choice.pack(padx=30, pady=20, ipadx=10, ipady=10, side="left")

scissors_image = tkinter.PhotoImage(file="images/scissors.png")
scissors_choice = ttk.Button(choice_frame, image=scissors_image, text="Scissors", compound="top", command=scissors_chosen)
scissors_choice.pack(padx=30, pady=10, ipadx=10, ipady=10, side="right")


# finally
root.mainloop()


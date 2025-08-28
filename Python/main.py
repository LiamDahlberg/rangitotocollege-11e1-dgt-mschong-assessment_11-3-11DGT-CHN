import tkinter
import invaders

# CONSTANTS
games = [
    invaders,
    invaders, # "Packman"
    "Pong",
    "Snake",
    "Tetris"
]

# NON CONSTANTS
inGame = False
curGameIndex = 0
alpha = 0

# DEFINITIONS
def escapeKey(event):
    global inGame
    if inGame:
        games[curGameIndex].quit()
        init()
        inGame = False

def leftKey(event):
    global curGameIndex
    if inGame == False:
        if curGameIndex > 0:
            curGameIndex -= 1
            if curGameIndex == 0:
                canvas.itemconfig("left_text", text="")
                canvas.itemconfig("left_box", state="hidden")
            else:
                canvas.itemconfig("left_text", text=games[curGameIndex - 1].getName())
                canvas.itemconfig("right_box", state="normal")

            canvas.itemconfig("middle_text", text=games[curGameIndex].getName())
            canvas.itemconfig("right_text", text=games[curGameIndex + 1].getName())
    else:
        games[curGameIndex].leftKey(event)

def rightKey(event):
    global curGameIndex
    if inGame == False:
        if curGameIndex < len(games) - 1:
            curGameIndex += 1
            if curGameIndex == len(games) - 1:
                canvas.itemconfig("right_text", text="")
                canvas.itemconfig("right_box", state="hidden")
            else:
                canvas.itemconfig("right_text", text=games[curGameIndex + 1].getName())
                canvas.itemconfig("left_box", state="normal")

            canvas.itemconfig("left_text", text=games[curGameIndex - 1].getName())
            canvas.itemconfig("middle_text", text=games[curGameIndex].getName())
    
    else:
        games[curGameIndex].rightKey(event)


def upKey(event):
    global inGame
    if inGame == False:
        global alpha
        alpha = 0
        startAnimation()
        games[curGameIndex].init(main, canvas)
        
        inGame = True
    else:
        games[curGameIndex].upKey(event)

def startAnimation():
    global alpha
    if alpha < 100:
        alpha += 5
        main.wm_attributes("-alpha", alpha / 100)
        main.after(50, startAnimation)

def init():
    global alpha
    alpha = 0
    startAnimation()

    canvas.create_text(512, 90, text=games[curGameIndex].getName(), fill="white", width=0, font=("Arial", 60, "bold"), tags="middle_text")

    #dimentions for the middle quater of the screen = 1024 * 0.25, 768 * 0.25 , 1024 * 0.75, 768 * 0.75
    canvas.create_rectangle(256, 192 , 768, 576, fill="white", width=0)

    #dimentions for the smaller boxes fith = 1024 * 0.4, 768 * 0.4, 1024 * 0.6, 768 * 0.6

    canvas.create_text(0, 266.4, text="", fill="white", width=0, font=("Arial", 26, "bold"), tags="left_text")
    canvas.create_rectangle(-102.4, 307.2, 102.4, 460.8, fill="white", width=0, tags="left_box", state="hidden")

    canvas.create_text(1024, 266.4, text=games[curGameIndex + 1].getName(), fill="white", width=0, font=("Arial", 26, "bold"), tags="right_text")
    canvas.create_rectangle(921.6, 307.2, 1126.4, 460.8, fill="white", width=0, tags="right_box")

    canvas.create_rectangle(276, 650 , 748, 768, fill="#FCD12A", width=0)
    canvas.create_text(512, 709, text="Leaderboard", fill="white", width=0, font=("Arial", 26, "bold"))

# MAIN
main = tkinter.Tk()
main.title("Classics")

main.geometry("1024x768")
main.resizable(0, 0)
canvas = tkinter.Canvas(main,bg="#000000")

#make an init for main menu to init after esc pressed
init()

canvas.pack(fill="both", expand=True) # fix canvas to the window size
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.bind('<Up>', upKey)
main.bind('<Escape>', escapeKey)
main.mainloop()
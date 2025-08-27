import tkinter
import invaders

inGame = False

games = [
    "Space Invaders",
    "PackMan",
    "Pong",
    "Snake",
    "Tetris"
]

curGameIndex = 0

def escapeKey(event):
    global inGame
    if inGame:
        match curGameIndex:
            case 0:
                invaders.quit()
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
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
                canvas.itemconfig("left_text", text=games[curGameIndex - 1])
                canvas.itemconfig("right_box", state="normal")

            canvas.itemconfig("middle_text", text=games[curGameIndex])
            canvas.itemconfig("right_text", text=games[curGameIndex + 1])
    else:
        #make case thing for game
        match curGameIndex:
            case 0:
                invaders.leftKey(event)
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass

def rightKey(event):
    global curGameIndex
    if inGame == False:
        if curGameIndex < len(games) - 1:
            curGameIndex += 1
            if curGameIndex == len(games) - 1:
                canvas.itemconfig("right_text", text="")
                canvas.itemconfig("right_box", state="hidden")
            else:
                canvas.itemconfig("right_text", text=games[curGameIndex + 1])
                canvas.itemconfig("left_box", state="normal")

            canvas.itemconfig("left_text", text=games[curGameIndex - 1])
            canvas.itemconfig("middle_text", text=games[curGameIndex])
    
    else:
        #make case thing for game
        match curGameIndex:
            case 0:
                invaders.rightKey(event)
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass


def upKey(event):
    global inGame
    if inGame == False:
        match curGameIndex:
            case 0:
                invaders.init(main, canvas)
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
        
        inGame = True
    else:
        match curGameIndex:
            case 0:
                invaders.upKey(event)
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass

def startAnimation():
    alpha = 0
    if alpha < 255:
        alpha += 5
        colour = '#%02x%02x%02x%02x' % (255, 255, 255, alpha)
        canvas.create_oval(256, 128, 768, 650, fill=colour, width=0, stipple="grey" + str(alpha)) #test
        main.after(500, startAnimation)

def init():
    startAnimation()

    canvas.create_text(512, 90, text=games[curGameIndex], fill="white", width=0, font=("Arial", 60, "bold"), tags="middle_text")

    #dimentions for the middle quater of the screen = 1024 * 0.25, 768 * 0.25 , 1024 * 0.75, 768 * 0.75
    canvas.create_rectangle(256, 192 , 768, 576, fill="white", width=0)

    #dimentions for the smaller boxes fith = 1024 * 0.4, 768 * 0.4, 1024 * 0.6, 768 * 0.6

    canvas.create_text(0, 266.4, text="", fill="white", width=0, font=("Arial", 26, "bold"), tags="left_text")
    canvas.create_rectangle(-102.4, 307.2, 102.4, 460.8, fill="white", width=0, tags="left_box", state="hidden")

    canvas.create_text(1024, 266.4, text=games[curGameIndex + 1], fill="white", width=0, font=("Arial", 26, "bold"), tags="right_text")
    canvas.create_rectangle(921.6, 307.2, 1126.4, 460.8, fill="white", width=0, tags="right_box")

    canvas.create_rectangle(276, 650 , 748, 768, fill="#FCD12A", width=0)
    canvas.create_text(512, 709, text="Leaderboard", fill="white", width=0, font=("Arial", 26, "bold"))

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
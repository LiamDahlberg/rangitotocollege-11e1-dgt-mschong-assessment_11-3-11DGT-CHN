import tkinter

games = [
    "Space Invaders",
    "PackMan",
    "Pong",
    "Snake",
    "Tetris"
]

curGameIndex = 0

def leftKey(event):
    global curGameIndex
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

def rightKey(event):
    global curGameIndex
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

def upKey(event):
    pass

main = tkinter.Tk()
main.title("Classics")

main.geometry("1024x768")
main.resizable(0, 0)
canvas = tkinter.Canvas(main,bg="#000000")

canvas.create_text(512, 90, text=games[curGameIndex], fill="white", width=0, font=("Arial", 70, "bold"), tags="middle_text")

#dimentions for the middle quater of the screen = 1024 * 0.25, 768 * 0.25 , 1024 * 0.75, 768 * 0.75
canvas.create_rectangle(256, 192 , 768, 576, fill="white", width=0)

#dimentions for the smaller boxes fith = 1024 * 0.4, 768 * 0.4, 1024 * 0.6, 768 * 0.6
if games[curGameIndex - 1]:
    canvas.create_text(0, 266.4, text=games[curGameIndex - 1], fill="white", width=0, font=("Arial", 28, "bold"), tags="left_text")
    canvas.create_rectangle(-102.4, 307.2, 102.4, 460.8, fill="white", width=0, tags="left_box")

if games[curGameIndex + 1]:
    canvas.create_text(1024, 266.4, text=games[curGameIndex + 1], fill="white", width=0, font=("Arial", 28, "bold"), tags="right_text")
    canvas.create_rectangle(921.6, 307.2, 1126.4, 460.8, fill="white", width=0, tags="right_box")

canvas.pack(fill="both", expand=True) # fix canvas to the window size
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.bind('<Up>', upKey)
main.mainloop()
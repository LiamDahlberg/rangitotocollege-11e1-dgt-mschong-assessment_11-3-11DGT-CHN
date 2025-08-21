import tkinter

games= {
    "test1",
    "test2",
    "test3"
}

main = tkinter.Tk()
main.title("Classics")

main.geometry("1024x768")
main.resizable(0, 0)
canvas = tkinter.Canvas(main,bg="#000000")

canvas.create_text(512, 90, text="Game", fill="white", width=0, font=("Arial", 70, "bold"))

#dimentions for the middle quater of the screen = 1024 * 0.25, 768 * 0.25 , 1024 * 0.75, 768 * 0.75
canvas.create_rectangle(256, 192 , 768, 576, fill="white", width=0)

#dimentions for the smaller boxes fith = 1024 * 0.4, 768 * 0.4, 1024 * 0.6, 768 * 0.6
canvas.create_rectangle(-102.4, 307.2, 102.4, 460.8, fill="white", width=0)
canvas.create_rectangle(921.6, 307.2, 1126.4, 460.8, fill="white", width=0)

canvas.pack(fill="both", expand=True) # fix canvas to the window size
#main.bind('<Left>', leftKey)
#main.bind('<Right>', rightKey)
#main.bind('<Up>', upKey)
main.mainloop()
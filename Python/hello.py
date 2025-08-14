import tkinter

def drawFace(offsetX, offsetY):
    canvas.create_oval(50 + offsetX, 50 + offsetY, 100 + offsetX, 100 + offsetY, tags="face", fill="black", width=2)
    canvas.create_oval(220 + offsetX, 50 + offsetY, 270 + offsetX, 100 + offsetY, tags="face", fill="black", width=2)
    canvas.create_line(120 + offsetX, 75 + offsetY, 140 + offsetX, 100 + offsetY, tags="face", fill="black", width=2)
    canvas.create_line(140 + offsetX, 100 + offsetY, 160 + offsetX, 75 + offsetY, tags="face", fill="black", width=2)
    canvas.create_line(160 + offsetX, 75 + offsetY, 180 + offsetX, 100 + offsetY, tags="face", fill="black", width=2)
    canvas.create_line(180 + offsetX, 100 + offsetY, 200 + offsetX, 75 + offsetY, tags="face", fill="black", width=2)

def callback(event):
    x, y = event.x, event.y
    #canvas.moveto("face", x - 110, y - 25)

main = tkinter.Tk()
main.title("eeby.. sleeby..")

main.geometry("640x480")
main.resizable(0, 0)
canvas = tkinter.Canvas(main,bg="#FF8FF6")

drawFace(0, 0)

canvas.bind('<Motion>', callback)
canvas.pack(fill="both", expand=True)
main.mainloop()
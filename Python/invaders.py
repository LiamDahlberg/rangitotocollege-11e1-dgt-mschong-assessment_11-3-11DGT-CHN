import tkinter

def drawShip(offsetX, offsetY, scale):
    canvas.create_rectangle(offsetX, 1 * scale + offsetY, 13 * scale + offsetX, 4 * scale + offsetY, tags="space_ship", fill="#00FF00", width=0)
    canvas.create_rectangle(1 * scale + offsetX, offsetY, 12 * scale + offsetX, 1 * scale + offsetY, tags="space_ship", fill="#00FF00", width=0)
    canvas.create_rectangle(5 * scale + offsetX, offsetY, 8 * scale + offsetX, -2 * scale + offsetY, tags="space_ship", fill="#00FF00", width=0)
    canvas.create_rectangle(6 * scale + offsetX, -2 * scale + offsetY, 7 * scale + offsetX, -3 * scale + offsetY, tags="space_ship", fill="#00FF00", width=0)

def drawProjectile(offsetX, offsetY, scale): # this is pre offset so the offset x can be the same as the ship one and be in correct position
    canvas.create_rectangle(6 * scale + offsetX, offsetY, 7 * scale + offsetX, 3 * scale + offsetY, tags="space_projectile", fill="#00FF00", width=0)

def drawInvader(offsetX, offsetY, scale, tag):
    # main body
    canvas.create_rectangle(2 * scale + offsetX, 2 * scale + offsetY, 9 * scale + offsetX, -2 * scale + offsetY, tags=tag, fill="#00FF00", width=0)
    canvas.create_rectangle(3 * scale + offsetX, -1 * scale + offsetY, 4 * scale + offsetX, offsetY, tags=tag, fill="#000000", width=0)
    canvas.create_rectangle(7 * scale + offsetX, -1 * scale + offsetY, 8 * scale + offsetX, offsetY, tags=tag, fill="#000000", width=0)

    # anteni
    canvas.create_rectangle(3 * scale + offsetX, -3 * scale + offsetY, 4 * scale + offsetX, -2 * scale + offsetY, tags=tag, fill="#00FF00", width=0)
    canvas.create_rectangle(7 * scale + offsetX, -3 * scale + offsetY, 8 * scale + offsetX, -2 * scale + offsetY, tags=tag, fill="#00FF00", width=0)
    # upper anteni
    canvas.create_rectangle(2 * scale + offsetX, -4 * scale + offsetY, 3 * scale + offsetX, -3 * scale + offsetY, tags=tag, fill="#00FF00", width=0)
    canvas.create_rectangle(8 * scale + offsetX, -4 * scale + offsetY, 9 * scale + offsetX, -3 * scale + offsetY, tags=tag, fill="#00FF00", width=0)

    # arm left
    canvas.create_rectangle(1 * scale + offsetX, -1 * scale + offsetY, 2 * scale + offsetX, 1 * scale + offsetY, tags=tag, fill="#00FF00", width=0)
    canvas.create_rectangle(offsetX,  offsetY, 1 * scale + offsetX, 3 * scale + offsetY, tags=tag, fill="#00FF00", width=0)
    # arm right
    canvas.create_rectangle(9 * scale + offsetX, -1 * scale + offsetY, 10 * scale + offsetX, 1 * scale + offsetY, tags=tag, fill="#00FF00", width=0)
    canvas.create_rectangle(10 * scale + offsetX,  offsetY, 11 * scale + offsetX, 3 * scale + offsetY, tags=tag, fill="#00FF00", width=0)

    # leg left
    canvas.create_rectangle(2 * scale + offsetX,  2 * scale + offsetY, 3 * scale + offsetX, 3 * scale + offsetY, tags=tag, fill="#00FF00", width=0)
    canvas.create_rectangle(3 * scale + offsetX,  3 * scale + offsetY, 5 * scale + offsetX, 4 * scale + offsetY, tags=tag, fill="#00FF00", width=0)
    # leg right
    canvas.create_rectangle(8 * scale + offsetX,  2 * scale + offsetY, 9 * scale + offsetX, 3 * scale + offsetY, tags=tag, fill="#00FF00", width=0)
    canvas.create_rectangle(6 * scale + offsetX,  3 * scale + offsetY, 8 * scale + offsetX, 4 * scale + offsetY, tags=tag, fill="#00FF00", width=0)

def leftKey(event):
    canvas.move("space_ship", -10, 0)

def rightKey(event):
    canvas.move("space_ship", 10, 0)

def init():
    drawShip(400, 700, 10)

if __name__ == "__main__":
    main = tkinter.Tk()
    main.title("eeby.. sleeby..")

    main.geometry("1024x768")
    main.resizable(0, 0)
    canvas = tkinter.Canvas(main,bg="#000000")

    init()

    drawProjectile(50, 50, 10)

    drawInvader(400, 100, 10, "invader")

    canvas.pack(fill="both", expand=True) # fix canvas to the window size
    main.bind('<Left>', leftKey)
    main.bind('<Right>', rightKey)
    main.mainloop()
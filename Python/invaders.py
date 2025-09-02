import time
import tkinter

name = "Space Invaders"
lastShotTime = time.time()
canvas = None
main = None
moveProjId = None
moveInvadersId = None
round = 1
entityList = []
invaderStage = 1

def getName():
    return name

def startRound(originX, originY, round):
    global invaderStage
    invaderStage = 1

    x = originX
    y = originY
    for i in range(round * 2): # for each round spawn * 2 amount of invaders with increasing tags (add to list for tracking)
        drawInvader(x, y, 10, "invader" + str(i))
        x += 120 # spacing between each invader
        entityList.append("invader" + str(i))

def drawShip(offsetX, offsetY, scale):
    canvas.create_rectangle(offsetX, 1 * scale + offsetY, 13 * scale + offsetX, 4 * scale + offsetY, tags="space_ship", fill="#00FF00", width=0)
    canvas.create_rectangle(1 * scale + offsetX, offsetY, 12 * scale + offsetX, 1 * scale + offsetY, tags="space_ship", fill="#00FF00", width=0)
    canvas.create_rectangle(5 * scale + offsetX, offsetY, 8 * scale + offsetX, -2 * scale + offsetY, tags="space_ship", fill="#00FF00", width=0)
    canvas.create_rectangle(6 * scale + offsetX, -2 * scale + offsetY, 7 * scale + offsetX, -3 * scale + offsetY, tags="space_ship", fill="#00FF00", width=0)

def drawProjectile(offsetX, offsetY, scale):
    canvas.create_rectangle(offsetX, offsetY, 1 * scale + offsetX, 3 * scale + offsetY, tags="space_projectile", fill="#00FF00", width=0)

#class Invader: maybe later make this a class?
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

def escapeKey(event):
    main.withdraw()

def leftKey(event):
    canvas.move("space_ship", -10, 0)

def rightKey(event):
    canvas.move("space_ship", 10, 0)

def upKey(event):
    global lastShotTime
    if time.time() - lastShotTime > 0.1:
        gunId = canvas.find_withtag("space_ship")[3]
        drawProjectile(canvas.coords(gunId)[0], canvas.coords(gunId)[1],10)
        lastShotTime = time.time()

def moveProj():
    global moveProjId
    for i in canvas.find_withtag("space_projectile"):
        canvas.move(i, 0, -10)
        if canvas.coords(i)[3] < 0:
            canvas.delete(i) # reduce amount of stuff game is keeping track of

    moveProjId = main.after(10, moveProj)

def moveInvaders():
    global moveInvadersId
    global invaderStage
    shouldNext = False

    for ent in entityList:
        for i in canvas.find_withtag(ent):
            if invaderStage % 2 != 0:
                canvas.move(i, 50, 0)
            else:
                canvas.move(i, -50, 0)
            coords = canvas.coords(ent)
            if coords[2] > 1024 - 100 or coords[0] < 100:
                shouldNext = True

    if shouldNext:
        invaderStage += 1
        print(ent)

    moveInvadersId = main.after(1000, moveInvaders)

def quit():
    canvas.delete("all")
    if moveProjId != None:
        main.after_cancel(moveProjId)
    if moveInvadersId != None:
        main.after_cancel(moveInvadersId)

def initRender():
    drawShip(400, 700, 10)
    startRound(50, 100, round)
    moveInvaders()

def init(main1, canvas1):
    global main
    global canvas
    main = main1 # setting globals for canvas and main so we dont make multiple canvases
    canvas = canvas1 
    canvas.delete("all")

    moveProj() # start proj move loop
    main.after(2000, initRender) # cancel this loop on escape thingie
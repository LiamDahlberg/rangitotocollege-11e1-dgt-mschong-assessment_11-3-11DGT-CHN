import time
import tkinter

name = "Space Invaders"
lastShotTime = time.time()
canvas = None
main = None
moveProjId = None
moveInvadersId = None
initId = None
round = 1
entityList = []
invaderStage = 1

def getName():
    return name

def startRound(originX, originY, round):
    global invaderStage
    invaderStage = 1
    invadersOnRow = 0
    x = originX
    y = originY

    canvas.itemconfig("round", text="Round: " + str(round))

    for i in range(round * 2): # for each round spawn * 2 amount of invaders with increasing tags (add to list for tracking)
        invadersOnRow += 1
        if invadersOnRow > 10:
            y += 50 # move invaders down if too many on screen
            invadersOnRow = 1 # reset count to one because otherwise we add 11 instead of 10 next time
            x = originX

        drawInvader(x, y, 5, "invader" + str(i))
        x += 60 # spacing between each invader
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

def leftKey(event):
    canvas.move("space_ship", -10, 0)

def rightKey(event):
    canvas.move("space_ship", 10, 0)

def upKey(event):
    global lastShotTime
    if time.time() - lastShotTime > 0.5:
        gunId = canvas.find_withtag("space_ship")[3]
        drawProjectile(canvas.coords(gunId)[0], canvas.coords(gunId)[1],10)
        lastShotTime = time.time()

def moveProj():
    global moveProjId

    for i in canvas.find_withtag("space_projectile"):
        hit = False
        hitEnt = None
        canvas.move(i, 0, -10)
        for ent in entityList:
            for a in canvas.find_withtag(ent):
                if canvas.coords(a)[0] < canvas.coords(i)[2] and canvas.coords(a)[2] > canvas.coords(i)[0] and canvas.coords(a)[1] < canvas.coords(i)[3] and canvas.coords(a)[3] > canvas.coords(i)[1]:
                    canvas.delete(i)
                    hit = True
                    hitEnt = ent
                    canvas.delete(ent)
                    break
            if hit:
                break

        if not hit:
            if canvas.coords(i)[3] < 0:
                canvas.delete(i) # reduce amount of stuff game is keeping track of
        else:
            entityList.remove(hitEnt)

    moveProjId = main.after(10, moveProj)

def moveInvaders():
    global moveInvadersId # get globals
    global invaderStage
    global round
    shouldNext = False

    if len(entityList) == 0:
        round += 1
        startRound(50, 100, round) # start new round if no more invaders

    else:
        for ent in entityList:
            for i in canvas.find_withtag(ent): # check all parts of the invaders
                if invaderStage % 2 != 0:
                    canvas.move(i, 50, 0)
                else:
                    canvas.move(i, -50, 0) # move left or right depending on stage

                coords = canvas.coords(ent)

                if coords[2] > 1024 - 25 or coords[0] < 25:
                    shouldNext = True # has reached left or right of screen

                if coords[1] > 768:
                    gameOver()

        if shouldNext: # left or right stages
            invaderStage += 1
            for ent in entityList:
                for i in canvas.find_withtag(ent):
                    if invaderStage % 2 != 0:
                        canvas.move(i, 50, 50)
                    else:
                        canvas.move(i, -50, 50) # move left or right depending on stage and down

    moveInvadersId = main.after(1000, moveInvaders) # loop to move invaders

def gameOver():
    canvas.delete("all") # gameover

    if moveProjId != None:
        main.after_cancel(moveProjId)
    if moveInvadersId != None:
        main.after_cancel(moveInvadersId)

    canvas.create_text(512, 285, text="GameOver", fill="red", width=0, font=("Arial", 80, "bold"))
    canvas.create_text(512, 485, text="Final Score: " + str(round), fill="red", width=0, font=("Arial", 80, "bold"))

def quit():
    canvas.delete("all") # quit script to go to main menu
    entityList.clear()
    if moveProjId != None:
        main.after_cancel(moveProjId)
    if moveInvadersId != None:
        main.after_cancel(moveInvadersId)
    if initId != None:
        main.after_cancel(initId)

def initRender():
    drawShip(400, 700, 10)
    startRound(50, 100, round)
    moveInvaders()
    canvas.create_text(512, 20, text="Round: " + str(round), fill="white", width=0, font=("Arial", 26, "bold"), tags="round")

def init(main1, canvas1):
    global main
    global canvas
    global round
    global initId

    main = main1 # setting globals for canvas and main so we dont make multiple canvases
    canvas = canvas1 
    canvas.delete("all")
    round = 1

    moveProj() # start proj move loop
    initId = main.after(2000, initRender) # cancel this loop on escape thingie
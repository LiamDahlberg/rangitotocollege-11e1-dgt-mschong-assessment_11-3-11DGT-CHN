import time
import tkinter

name = "Pong"
canvas = None
main = None
initId = None
leftScore = 0
rightScore = 0
startScreen = True
keysId = None
keysPressed = []
ballVeloX = 1
ballVeloY = 1

def getName():
    return name

def quit():
    canvas.delete("all") # quit script to go to main menu
    if initId != None:
        main.after_cancel(initId)
    if keysId != None:
        main.after_cancel(keysId)
    
def processMode(left):
    global startScreen
    if left and startScreen:
        # 1 player
        startScreen = False
        canvas.create_rectangle(50, 307.2, 100, 460.8, fill="white", width=0, tags="player1")
        canvas.create_rectangle(974, 307.2, 924, 460.8, fill="white", width=0, tags="playerAi")

    elif startScreen:
        # 2 player
        startScreen = False
        canvas.create_rectangle(50, 307.2, 100, 460.8, fill="white", width=0, tags="player1")
        canvas.create_rectangle(974, 307.2, 924, 460.8, fill="white", width=0, tags="player2")

        

def leftKey():
    processMode(True)

def rightKey():
    processMode(False)

def upKey():
    canvas.move("player2", 0, -10)

def downKey():
    canvas.move("player2", 0, 10)

def wKey():
    canvas.move("player1", 0, -10)

def sKey():
    canvas.move("player1", 0, 10)

def onKeyPress(event):
    if event.keysym not in keysPressed:
        keysPressed.append(event.keysym)

def onKeyRelease(event):
    if event.keysym in keysPressed:
        keysPressed.remove(event.keysym)

def initRender():
    checkKeys()
    canvas.create_text(512, 20, text=str(leftScore) + " - " + str(rightScore), fill="white", width=0, font=("Arial", 26, "bold"), tags="score")

def moveBall():
    # TODO
    pass

def checkKeys():
    global keysId
    if startScreen == False:
        if "w" in keysPressed:
            wKey()
        if "s" in keysPressed:
            sKey()
        if "Up" in keysPressed:
            upKey()
        if "Down" in keysPressed:
            downKey()
    else:
        if "Left" in keysPressed:
            leftKey()
        if "Right" in keysPressed:
            rightKey()
    keysId = main.after(25, checkKeys)

def setPressed(list):
    global keysPressed
    keysPressed = list

def init(main1, canvas1):
    global main
    global canvas
    global leftScore
    global rightScore
    global initId
    global startScreen

    startScreen = True
    leftScore = 0
    rightScore = 0

    main = main1 # setting globals for canvas and main so we dont make multiple canvases
    canvas = canvas1 
    canvas.delete("all")
    
    initId = main.after(2000, initRender) # cancel this loop on escape thingie
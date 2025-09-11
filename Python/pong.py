import time
import tkinter

name = "Pong"
canvas = None
main = None
initId = None
leftScore = 0
rightScore = 0
startScreen = True

def getName():
    return name

def quit():
    canvas.delete("all") # quit script to go to main menu
    if initId != None:
        main.after_cancel(initId)
    
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
        

def leftKey(event):
    processMode(True)

def rightKey(event):
    processMode(False)

def upKey(event):
    if startScreen == False:
        canvas.move("player1", 0, -10)

def downKey(event):
    if startScreen == False:
        canvas.move("player1", 0, 10)

def initRender():
    canvas.create_text(512, 20, text=str(leftScore) + " - " + str(rightScore), fill="white", width=0, font=("Arial", 26, "bold"), tags="score")

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
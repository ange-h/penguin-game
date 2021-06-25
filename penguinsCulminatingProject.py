#culminating project
#05/29/2021
#penguin drop down game

#import graphics, time, random 
from graphics import *
import time
from random import randint
import math

class FallFish:
    def __init__(self, location, dY, win):
        self.win = win
        self.location = location
        self.dY = 2.1

        self.parts = []
        self.body = Circle(location, 10)
        self.body.setFill("white")
        self.body.draw(win)

    def update(self):
        global score
        global scoreText
        global miss
        global missText
        global iMiss

        if intersectsWith(self.body, basketHandle):
            self.body.undraw()
            score = score+0.1
            iScore = math.ceil(score)
     
        else:
            self.body.move(0, self.dY)
            iScore = math.ceil(score)
        
        if intersectsWith(self.body, groundLine):
            self.body.undraw()
            miss = (miss+1/11)
            iMiss = int(round(float(miss)))
            iMiss = iMiss - iScore
               
        else:    
            self.body.move(0, self.dY)
            iMiss = int(round(float(miss)))
            iMiss = iMiss - iScore
       
        missText.setText("Misses: "+str(iMiss))
        scoreText.setText("Score: "+str(iScore))
#colours and draws objects
def colouring(thing, colour):
    thing.setOutline(colour)
    thing.setFill(colour)
    thing.draw(win)

#colours objects without drawing
def colourNoDraw(thingy, coloury):
    thingy.setOutline(coloury)
    thingy.setFill(coloury)
      
#functions
def icy(x): #drawing icicles
    icy1 = Polygon(Point(30+x, 0), Point(37+x, 50), Point(44+x, 0))
    icy2 = Polygon(Point(50+x, 0), Point(56+x, 90), Point(62+x, 0))
    icy3 = Polygon(Point(100+x, 0), Point(106+x, 60), Point(112+x, 0))
    icy4 = Polygon(Point(140+x, 0), Point(147+x, 110), Point(154+x, 0))
    
    #cakk colouring to turn into dodger blue and draw
    colouring(icy1, "dodger blue")
    colouring(icy2, "dodger blue")
    colouring(icy3, "dodger blue")
    colouring(icy4, "dodger blue")


#checking if click is in box
def containsPoint(graphicsObject, pointToCheck):
    x=pointToCheck.getX()
    y=pointToCheck.getY()

    leftX=graphicsObject.getP1().getX()
    rightX=graphicsObject.getP2().getX()
    topY=graphicsObject.getP1().getY()
    bottomY=graphicsObject.getP2().getY()

    if (x>=leftX and x<=rightX and y>=topY and y<=bottomY):
        return True # the point is in the box

    # the point is not in the bounding box
    return False

#function to see if objects intersect
def intersection(thing1, thing2):
    left=max(thing1.getP1().getX(),thing2.getP1().getX())
    right=min(thing1.getP2().getX(),thing2.getP2().getX())
    top=max(thing1.getP1().getY(),thing2.getP1().getY())
    bottom=min(thing1.getP2().getY(),thing2.getP2().getY())

    if (right<left or bottom<top):
        return None

    return Rectangle(Point(left,top),Point(right,bottom))
    
def intersectsWith(thing1,thing2):
    return intersection(thing1,thing2)!=None


#main program
#drawing the different parts of the penguin
head = Circle(Point(250, 200), 20)
body = Oval(Point(232, 210), Point(268, 258))
leftArm = Oval(Point(220, 215), Point(240, 227))
rightArm = Oval(Point(280, 215), Point(260, 227))
leftFoot = Polygon(Point(244, 252), Point(235, 263), Point(245, 263))
rightFoot = Polygon(Point(256, 252), Point(265, 263), Point(255, 263))
whiteHead = Circle(Point(250, 203), 13)
belly = Oval(Point(237, 215), Point(263, 253))
leftEye = Circle(Point(244, 199), 2)
rightEye = Circle(Point(256, 199), 2)
beak = Polygon(Point(246, 205), Point(254, 205), Point(250, 212))
basketHandle = Line(Point(232, 218), Point(268, 218))
basketHandle.setWidth(3) #make basket handle thicker
basket = Rectangle(Point(238, 218), Point(262, 233))

#new penguin
head2 = Circle(Point(250, 200), 20)
body2 = Oval(Point(232, 210), Point(268, 258))
leftArm2 = Oval(Point(220, 215), Point(240, 227))
rightArm2 = Oval(Point(280, 215), Point(260, 227))
leftFoot2 = Polygon(Point(244, 252), Point(235, 263), Point(245, 263))
rightFoot2 = Polygon(Point(256, 252), Point(265, 263), Point(255, 263))
whiteHead2 = Circle(Point(250, 203), 13)
belly2 = Oval(Point(237, 215), Point(263, 253))
leftEye2 = Circle(Point(244, 199), 2)
rightEye2 = Circle(Point(256, 199), 2)
beak2 = Polygon(Point(246, 205), Point(254, 205), Point(250, 212))
basketHandle2 = Line(Point(232, 218), Point(268, 218))
basketHandle2.setWidth(3) #make basket handle thicker
basket2 = Rectangle(Point(238, 218), Point(262, 233))

#calling function to colour penguin parts
colourNoDraw(rightFoot, "gold")
colourNoDraw(leftFoot, "gold")    
colourNoDraw(head, "gray")
colourNoDraw(body, "gray")
colourNoDraw(leftArm, "gray")
colourNoDraw(rightArm, "gray")
colourNoDraw(whiteHead, "white")
colourNoDraw(belly, "white")
colourNoDraw(leftEye, "black")
colourNoDraw(rightEye, "black")
colourNoDraw(beak, "gold")
colourNoDraw(basketHandle, "sienna")
colourNoDraw(basket, "sienna")

penguinList = [rightFoot, leftFoot, head, body, leftArm, rightArm, whiteHead, belly, leftEye, rightEye, beak, basketHandle, basket]

#have fish fall on from random x axis
randomFall = randint(-243, 229)

#fish parts
fishBody = Oval(Point(243+randomFall, 10), Point(257+randomFall, 30))
tail = Polygon(Point(243+randomFall, 0), Point(257+randomFall, 0), Point(250+randomFall, 10))

#call function for colouring fish
colourNoDraw(fishBody, "lime")
colourNoDraw(tail, "lime")

fish = [fishBody, tail]
#draw window
win = GraphWin("Woo",500, 300, autoflush=False)

#make background look good
win.setBackground("alice blue")

#add icicles and repeat by calling icy function
icy(0)
icy(200)
icy(350)

#draw play button
play = Rectangle(Point(200, 130), Point(300, 170))
colouring(play, "dodger blue")

#write text
playText = Text(Point(250, 150), "Play")
playText.draw(win)

instructions = Text(Point(250, 200), "Use left and right keys to move")
instructions.draw(win)

gameStarted = False

scoreTextX = 400
scoreTextY = 15

fallingFish = []
spawnCounter = 100
spawnStep = 0
scoreText = Text(Point(scoreTextX, scoreTextY), "Score: 0")
score = 0
missText = Text(Point(300, 15), "Misses: 0")
miss = 0
iMiss = 0

# Main loop
while True:
    # Check to see if the user clicked anything
    pointClicked=win.checkMouse()
    if (pointClicked !=None):
        if (containsPoint(play,pointClicked)): #draw the in game background
            inGame = Rectangle(Point(0,0), Point(500, 300))#sky
            colouring(inGame, "alice blue")

            ground = Rectangle(Point(0, 250), Point(500, 300))
            ground.setFill("white")
            ground.setOutline("white")
            ground.draw(win)

            groundLine = Line(Point(0, 250), Point(500, 250))
            colouring(groundLine, "white")
            

            #draw parts of characters
            for part in penguinList:
                part.draw(win)

            #for partt in fish:
                #partt.draw(win)
            time.sleep(0.5)
           
            gameStarted = True
            
    if gameStarted:
        
        keyPressed = win.checkKey()#checking which key is pressed
        fishSpeed = 2 #assign speed fo fish

                
        for partt in fish: #get fish to move
            partt.move(0, fishSpeed)
            
        if (keyPressed == "Left"):
            for part in penguinList:
                part.move(-10, 0)

        if (keyPressed == "Right"):
            for part in penguinList:
                part.move(10, 0)

        if (spawnStep == 0):
            fallingFish.append(FallFish(Point(randint(25, 475), 0), 5, win))
            scoreText.draw(win)
            missText.draw(win)
            spawnStep = 1

        if (intersectsWith(basket, fishBody)):
            for partt in fish:
                partt.undraw()

        if (intersectsWith(fishBody, ground)):
            for partt in fish:
                partt.undraw()

                                     
    for curFish in fallingFish:
        curFish.update()

    spawnCounter = spawnCounter-spawnStep
    if (spawnCounter == 0):
        spawnCounter = randint(50, 100)
        fallingFish.append(FallFish(Point(randint(25, 475), 0), 5, win))

    if iMiss == 3:
        break

    update(36)
    
#undraw everything
inGame.undraw()
ground.undraw()

scoreText.undraw()
missText.undraw()
for part in penguinList:
    part.undraw()


#redraw things     
inGame.draw(win)
ground.draw(win)

colouring(rightFoot2, "gold")
colouring(leftFoot2, "gold")    
colouring(head2, "gray")
colouring(body2, "gray")
colouring(leftArm2, "gray")
colouring(rightArm2, "gray")
colouring(whiteHead2, "white")
colouring(belly2, "white")
colouring(leftEye2, "black")
colouring(rightEye2, "black")
colouring(beak2, "gold")
colouring(basketHandle2, "sienna")
colouring(basket2, "sienna")

leftEyebrow = Line(Point(240, 193), Point(248, 197))
leftEyebrow.setWidth(2)
leftEyebrow.draw(win)

rightEyebrow = Line(Point(260, 193), Point(252, 197))
rightEyebrow.setWidth(2)
rightEyebrow.draw(win)

scoreText.move(-150, 0)
scoreText.setSize(18)
scoreText.draw(win)

over = Text(Point(250, 100), "Game Over")
over.setSize(24)
over.draw(win)


                        
                    
            

        
        


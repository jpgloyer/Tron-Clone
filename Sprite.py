

class Sprite:
    def __init__(self,xStartInPixels,yStartInPixels,shape:str='r',width:int = 0,height:int = 0,radius:int = 0,availableDirections:int = 4,latchMove:bool = False,speed:int = 1,lives:int = 0,primaryColor:tuple=(0,0,0,0),secondaryColor:tuple=(0,0,0,0)):
        self.xHome = xStartInPixels
        self.yHome = yStartInPixels
        self.x = xStartInPixels
        self.y = yStartInPixels
        self.currentDirection = 'n'
        self.availableDirections = availableDirections
        self.orientation = 'u'
        self.latchMove = latchMove
        self.shape = shape
        self.width = width
        self.height = height
        self.speed = speed
        self.lives = lives
        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor



        self.updateOptions = {
            "up":self.moveUp,
            "down":self.moveDown,
            "left":self.moveLeft,
            "right":self.moveRight,
            "right-up":self.moveRightUp,
            "right-down":self.moveRightDown,
            "left-up":self.moveLeftUp,
            "left-down":self.moveLeftDown,
            "n":self.nothing,
            'L0':self.nothing,
            'L+1':self.addLife,
            'L-1':self.removeLife

        }

    
    def update(self,updateOptions:dict = {}):
        if not self.latchMove:
            self.currentDirection = 'n'

        for i in updateOptions:
            self.updateOptions[updateOptions[i]]()
        


    def moveRight(self):
        self.currentDirection = 'right'
        self.orientation = 'r'
        self.x+=1
    def moveLeft(self):
        self.currentDirection = 'left'
        self.orientation = 'l'
        self.x-=1
    def moveUp(self):
        self.currentDirection = 'up'
        self.orientation = 'u'
        self.y-=1
    def moveDown(self):
        self.currentDirection = 'down'
        self.orientation = 'd'
        self.y+=1
    def moveRightUp(self):
        self.currentDirection = 'right-up'
        self.x+=1
        self.orientation = 'r'
        if self.availableDirections == 8:
            self.y-=1
    def moveRightDown(self):
        self.currentDirection = 'right-down'
        self.x+=1
        self.orientation = 'r'
        if self.availableDirections == 8:
            self.y+=1
    def moveLeftUp(self):
        self.currentDirection = 'left-up'
        self.x-=1
        self.orientation = 'l'
        if self.availableDirections == 8:
            self.y-=1
    def moveLeftDown(self):
        self.currentDirection = 'left-down'
        self.x-=1
        self.orientation = 'l'
        if self.availableDirections == 8:
            self.y+=1
    


    def nothing(self):
        pass

    def removeLife(self):
        self.lives-=1

    def addLife(self):
        self.lives+=1
        

    def reset(self):
        self.x = self.xHome
        self.y = self.yHome
        self.currentDirection = 'n'
        self.orientation = 'u'
        
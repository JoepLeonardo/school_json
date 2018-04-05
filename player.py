class Player():
    # postition variabeles
    posX = posY = 0
    # size of the players bad
    sizeX = sizeY = 0
    # min and max position bad can be in the y-axis
    minY = maxY = 0
    # points scored
    points = 0
    
    def __init__(self, inX, inSizeX, inSizeY, inMinY, inMaxY):
        # all variable(s) that need te be set once
        self.posX = inX
        self.sizeX = inSizeX
        self.sizeY = inSizeY
        self.maxY = inMaxY
        self.minY = inMinY
        self.points = 0
        
    def reset(self, inPosY):
        # all variable(s) that need te be set at the begin of each game
        self.posY = inPosY
        
    def getPosX(self):
        return self.posX
    
    def getPosY(self):
        return self.posY
    
    def getSizeX(self):
        return self.sizeX
    
    def getSizeY(self):
        return self.sizeY
    
    def getPoints(self):
        return self.points
    
    def addPoint(self):
        self.points = self.points + 1
    
    def move(self, direction):
        # check direction
        if (direction > 0):
            # going down
            if (self.posY + direction < self.maxY):
                self.posY += direction
            else:
                self.posY = self.maxY
        else:
            # going up
            if (self.posY + direction > self.minY):
                self.posY += direction
            else:
                self.posY = self.minY
            
   

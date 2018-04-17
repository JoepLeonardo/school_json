class Player():
       
    def __init__(self, inX, inWidth, inHeight, inMinY, inMaxY):
        # points scored
        self.points = 0
        # position
        self.posX = inX
        self.posY = 0
        # size of the players bad
        self.width = inWidth
        self.height = inHeight
        # min and max position bad can be in the y-axis
        self.maxY = inMaxY
        self.minY = inMinY        
        
    def reset(self, inPosY):
        # all variable(s) that need te be set at the begin of each game
        self.posY = inPosY
        
    def getPosX(self):
        return self.posX
    
    def getPosY(self):
        return self.posY
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
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
            
   

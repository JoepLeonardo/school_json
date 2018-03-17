class Player():
    # postition variabeles
    posX = posY = 0
    # size of the players bad
    sizeX = sizeY = 0
    # min and max position bad can be in the y-axis
    minY = maxY = 0
    # points scored
    points = 0
    
    def __init__(self, inX, inY, inSizeX, inSizeY, inMinY, inMaxY):
        self.posX = inX
        self.posY = inY
        self.sizeX = inSizeX
        self.sizeY = inSizeY
        self.maxY = inMaxY
        self.minY = inMinY
        
    def getPosX(self):
        return self.posX
    
    def getPosY(self):
        return self.posY
    
    def getSizeX(self):
        return self.sizeX
    
    def getSizeY(self):
        return self.sizeY
    
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
            
    
    def setPosY(self, inPosY):
        self.posY = inPosY

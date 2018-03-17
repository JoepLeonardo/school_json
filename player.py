class Player():
    # postition variabeles
    posX = posY = 0
    # size of the players bad
    sizeX = sizeY = 0
    # max position bad can be in the y-axis
    maxY = 0
    # points scored
    points = 0
    
    def __init__(self, inX, inY, inSizeX, inSizeY, inMaxY):
        self.posX = inX
        self.posY = inY
        self.sizeX = inSizeX
        self.sizeY = inSizeY
        self.maxY = inMaxY
        
    def getPosX(self):
        return self.posX
    
    def getPosY(self):
        return self.posY
    
    def getSizeX(self):
        return self.sizeX
    
    def getSizeY(self):
        return self.sizeY
    
    def move(self, direction):
        #TODO: make this safe
        self.posY += direction
    
    def setPosY(self, inPosY):
        self.posY = inPosY

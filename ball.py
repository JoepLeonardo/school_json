class Ball():
    # postition variabeles
    posX = posY = 0
    # direction of the ball
    dirX = dirY = 0
    # size of the ball
    size = 0
    # speed of the ball
    speed = 0
    
    def __init__(self, inX, inY, inDirX, inDirY, inSize, inSpeed):
        self.posX = inX
        self.posY = inY
        self.dirX = inDirX
        self.dirY = inDirY
        self.size = inSize
        self.speed = inSpeed
        
    def getPosX(self):
        return self.posX
    
    def getPosY(self):
        return self.posY
    
    def getDirX(self):
        return self.dirX
    
    def getDirY(self):
        return self.dirY
    
    def getSize(self):
        return self.size
    
    def getSpeed(self):
        return self.speed
    
    def updatePos(self, inX, inY):
        self.posX = inX
        self.posY = inY
        
    def updateDir(self, inDirX, inDirY):
        self.dirX = inDirX
        self.dirY = inDirY    
        
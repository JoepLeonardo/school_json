class Ball():
    # postition variabeles
    posX = posY = 0
    # direction of the ball
    dirX = dirY = 0
    # size of the ball
    size = 0
    # speed of the ball
    speed = 0
    
    def __init__(self, inSize, inSpeed):
        # all variable(s) that need te be set once
        self.size = inSize
        self.speed = inSpeed
    
    def reset(self, inX, inY, inDirX, inDirY):
        # all variable(s) that need te be set at the begin of each game
        self.posX = inX
        self.posY = inY
        self.dirX = inDirX
        self.dirY = inDirY
        
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
    
    def updatePos(self):
        self.posX += self.dirX
        self.posY += self.dirY
        
    def updateDir(self, inDirX, inDirY):
        self.dirX = inDirX
        self.dirY = inDirY
        
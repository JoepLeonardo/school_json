class Ball():
       
    def __init__(self, inSize):
        # direction of the ball
        self.size = inSize
        # speed of the ball
        self.speed = 0
        # position and direction
        self.posX = 0
        self.posY = 0
        self.dirX = 0
        self.dirY = 0
    
    def reset(self, inX, inY, inDirX, inDirY, inSpeed):
        # all variable(s) that need te be set at the begin of each game
        self.posX = inX
        self.posY = inY
        self.dirX = inDirX
        self.dirY = inDirY
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
    
    def increaseSpeed(self, increase):
        self.speed = self.speed + increase
    
    def updatePos(self):
        self.posX += self.dirX
        self.posY += self.dirY
        
    def updateDir(self, inDirX, inDirY):
        self.dirX = inDirX
        self.dirY = inDirY
        
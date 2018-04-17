class Ball():
       
    def __init__(self, inSize, inMinY, inMaxY):
        # direction of the ball
        self.size = inSize
        # min and max position bad can be in the y-axis
        self.maxY = inMaxY
        self.minY = inMinY
        # speed of the ball
        self.speed = 0
        # position and direction
        self.posX = float(0.0)
        self.posY = float(0.0)
        self.dirX = float(0.0)
        self.dirY = float(0.0)
    
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
        # update x-axis
        self.posX += self.dirX
        # update y-axis
        # check direction
        if (self.dirY > 0):
            # going down
            if (self.posY + self.dirY < self.maxY):
                self.posY += self.dirY
            else:
                self.posY = self.maxY
        else:
            # going up
            if (self.posY + self.dirY > self.minY):
                self.posY += self.dirY
            else:
                self.posY = self.minY
        
    def updateDir(self, inDirX, inDirY):
        self.dirX = inDirX
        self.dirY = inDirY
        
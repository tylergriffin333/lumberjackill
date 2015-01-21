from positionEntity import PositionEntity
import utils

class DynamicEntity(PositionEntity):
    def __init__(self, game, x, y):
        PositionEntity.__init__(self, game, x, y)
        self.xVel=0#current velocity
        self.yVel=0
        
    def moveVector(self, xVel, yVel):
        self.x+=xVel*self.game.delta
        self.y+=yVel*self.game.delta
        
    def move(self):
        self.moveVector(self.xVel, self.yVel)
        
    def run(self):
        self.move()
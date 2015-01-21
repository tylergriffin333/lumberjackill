from posDimEntity import PosDimEntity
from dynamicEntity import DynamicEntity
from rectColliderDynamic import RectColliderDynamic
from imageRenderer import ImageRenderer
import utils

class Tree(PosDimEntity, ImageRenderer, RectColliderDynamic, DynamicEntity):#TODO: should inherit from FallingEntity
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, 1.12, 1.68)
        DynamicEntity.__init__(self, game, x, y)
        RectColliderDynamic.__init__(self, game.collisionSystem)
        ImageRenderer.__init__(self, game.graphicsRenderer, "tree.png", -.13, -.20)
        self.speed=.0081
        self.xVel=self.speed
        
    def hitBottom(self, otherCollider):#called if your bottom hits something else's top (you've landed on the "ground"
        if self.yVel>0:#is falling
            self.yVel=0#stop falling
        
    def hitTop(self, otherCollider):
        if self.yVel<0:
            self.yVel=0
            
    def hitLeft(self, otherCollider):
        if self.xVel<0:
            self.xVel=0
            
        self.xVel=self.speed
    
    def hitRight(self, otherCollider):
        if self.xVel>0:
            self.xVel=0
        
        self.xVel=-self.speed
        
    def run(self):
        DynamicEntity.run(self)
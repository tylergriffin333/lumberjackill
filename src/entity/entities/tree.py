from posDimEntity import PosDimEntity
from fallingEntity import FallingEntity
from rectColliderDynamic import RectColliderDynamic
from imageRenderer import ImageRenderer

class Tree(PosDimEntity, ImageRenderer, RectColliderDynamic, FallingEntity):#TODO: should inherit from FallingEntity
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, 1.12, 1.68)
        FallingEntity.__init__(self, game, x, y)
        RectColliderDynamic.__init__(self, game.collisionSystem)
        ImageRenderer.__init__(self, game.graphicsRenderer, "tree.png", -.13, -.11)
        self.leftImage=self.image
        self.rightImage=self.graphicsRenderer.loadImage("tree2.png")
        self.speed=.0085
        self.xVel=-self.speed
        
    def hitLeft(self, otherCollider):
        self.xVel=self.speed
        self.image=self.rightImage
        
    def hitRight(self, otherCollider):
        self.xVel=-self.speed
        self.image=self.leftImage
        
    def hitTop(self, otherCollider):
        if self.yVel<0:
            self.yVel=0
        
    def run(self):
        FallingEntity.run(self)
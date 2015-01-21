from posDimEntity import PosDimEntity
from fallingEntity import FallingEntity
from rectColliderDynamic import RectColliderDynamic
from imageAnimationRenderer import ImageAnimationRenderer

class Tree(PosDimEntity, ImageAnimationRenderer, RectColliderDynamic, FallingEntity):#TODO: should inherit from FallingEntity
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, 1.07, 1.52)
        FallingEntity.__init__(self, game, x, y)
        RectColliderDynamic.__init__(self, game.collisionSystem)
        ImageAnimationRenderer.__init__(self, game.graphicsRenderer, "evil_tree/running.animation")#TODO: need to make all things shared between instances static
        self.speed=.0085
        self.xVel=-self.speed
        
    def hitLeft(self, otherCollider):
        self.xVel=self.speed
        
    def hitRight(self, otherCollider):
        self.xVel=-self.speed
        
    def hitTop(self, otherCollider):
        if self.yVel<0:
            self.yVel=0
        
    def run(self):
        FallingEntity.run(self)
from posDimEntity import PosDimEntity
from fallingEntity import FallingEntity
from rectColliderDynamic import RectColliderDynamic
from imageAnimationRenderer import ImageAnimationRenderer
from imageAnimation import ImageAnimation

class EvilTree(PosDimEntity, ImageAnimationRenderer, RectColliderDynamic, FallingEntity):
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, 1.07, 1.67)
        ImageAnimationRenderer.__init__(self, game.graphicsRenderer)#TODO: need to make all things shared between instances static
        self.runningAnimation=ImageAnimation(game.graphicsRenderer, "evil_tree/running.animation")
        self.curAnimation=self.runningAnimation
        FallingEntity.__init__(self, game, x, y)
        RectColliderDynamic.__init__(self, game.collisionSystem)
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
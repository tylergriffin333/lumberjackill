from posDimEntity import PosDimEntity
from fallingEntity import FallingEntity
from rectColliderDynamic import RectColliderDynamic
from imageAnimationRenderer import ImageAnimationRenderer
from imageAnimationLooping import ImageAnimationLooping
from evilFirewood import EvilFirewood
import utils

class EvilTree(PosDimEntity, ImageAnimationRenderer, RectColliderDynamic, FallingEntity):
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, 1.07, 1.67)#TODO: make evilTree bigger
        ImageAnimationRenderer.__init__(self, game.graphicsRenderer, -.20, -.10)#TODO: need to make all things shared between instances static
        
        self.runningAnimation=ImageAnimationLooping(game.graphicsRenderer, "evil_tree/running.animation", 1)
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
            
        if otherCollider.team=="jack":#TODO: Should have a "baddie" class or a "stompable" class that holds this functionality.
            self.game.removeEntity(self)
            
            for x in range(utils.getRandomIntInRange(2, 4)):
                self.game.addEntity(EvilFirewood(self.game, self.x+utils.getRandom()*.1, self.y+utils.getRandom()*.1))
        
    def run(self):
        FallingEntity.run(self)
        ImageAnimationRenderer.run(self)
from posDimEntity import PosDimEntity
from fallingEntity import FallingEntity
from rectColliderDynamic import RectColliderDynamic
from imageAnimationRenderer import ImageAnimationRenderer
from imageAnimationLooping import ImageAnimationLooping
from baddie import Baddie
import utils

class EvilFirewood(PosDimEntity, ImageAnimationRenderer, RectColliderDynamic, FallingEntity, Baddie):
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, .3, 1.0)
        Baddie.__init__(self, game)
        ImageAnimationRenderer.__init__(self, game.graphicsRenderer, -.1, -.1)#TODO: need to make all things shared between instances static
        
        self.runningAnimation=ImageAnimationLooping(game.graphicsRenderer, "evil_firewood/running.animation", .25)
        self.curAnimation=self.runningAnimation
        
        FallingEntity.__init__(self, game, x, y)
        RectColliderDynamic.__init__(self, game.collisionSystem)
        self.jumpSpeed=-.011#your speed in the upward direction when when you jump
        self.speed=.0085
        self.xVel=self.speed
        if utils.getRandomIntZeroMax(1)>0:
            self.xVel=-self.speed
        
    def hitLeft(self, otherCollider):
        Baddie.hitLeft(self, otherCollider)
        self.xVel=self.speed
        
    def hitRight(self, otherCollider):
        Baddie.hitRight(self, otherCollider)
        self.xVel=-self.speed
        
    def hitTop(self, otherCollider):
        Baddie.hitTop(self, otherCollider)
        FallingEntity.hitTop(self, otherCollider)
        
    def hitBottom(self, otherCollider):
        FallingEntity.hitBottom(self, otherCollider)
        self.jump()#TODO: evilFirewood and Jack should both inherit from a Jumping entity that shares this method
        
    def jump(self):
        self.yVel=self.jumpSpeed
        
    def run(self):
        FallingEntity.run(self)
        ImageAnimationRenderer.run(self)
        #TODO: make evilFirewood jump randomly
        #TODO: evilFirewood and evilTree should have a common ancestor
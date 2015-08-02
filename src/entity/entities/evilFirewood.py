from posDimEntity import PosDimEntity
from fallingEntity import FallingEntity
from rectColliderDynamic import RectColliderDynamic
from imageAnimationRenderer import ImageAnimationRenderer
from imageAnimationLooping import ImageAnimationLooping

class EvilFirewood(PosDimEntity, ImageAnimationRenderer, RectColliderDynamic, FallingEntity):
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, .3, 1.0)
        ImageAnimationRenderer.__init__(self, game.graphicsRenderer, -.1, -.1)#TODO: need to make all things shared between instances static
        
        self.runningAnimation=ImageAnimationLooping(game.graphicsRenderer, "evil_firewood/running.animation", .25)
        self.curAnimation=self.runningAnimation
        
        FallingEntity.__init__(self, game, x, y)
        RectColliderDynamic.__init__(self, game.collisionSystem)
        self.speed=.0085
        self.xVel=0
        
    def hitLeft(self, otherCollider):
        pass#self.xVel=self.speed
        
    def hitRight(self, otherCollider):
        pass#self.xVel=-self.speed
        
    def hitTop(self, otherCollider):
        if self.yVel<0:
            self.yVel=0#TODO: this should be in fallingEntity
            
        if otherCollider.team=="jack":#TODO: Should have a "baddie" class or a "stompable" class that holds this functionality.
            pass#self.game.removeEntity(self)
        
    def run(self):
        FallingEntity.run(self)
        ImageAnimationRenderer.run(self)
        #TODO: make evilFirewood jump randomly
        #TODO: evilFirewood and evilTree should have a common ancestor
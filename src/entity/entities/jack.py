from posDimEntity import PosDimEntity
from dynamicEntity import DynamicEntity
from rectColliderDynamic import RectColliderDynamic
from imageAnimationRenderer import ImageAnimationRenderer
from imageAnimationLooping import ImageAnimationLooping
from imageAnimationNonLooping import ImageAnimationNonLooping
from fallingEntity import FallingEntity
import utils
import constants
import input

class Jack(PosDimEntity, ImageAnimationRenderer, RectColliderDynamic, FallingEntity):
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, .6, 1.4)
        FallingEntity.__init__(self, game, x, y)
        RectColliderDynamic.__init__(self, game.collisionSystem)
        ImageAnimationRenderer.__init__(self, game.graphicsRenderer, -.04, -.035)#TODO: need to make all things shared between instances static
        
        self.runningAnimation=ImageAnimationLooping(game.graphicsRenderer, "jack/running.animation", .5)
        self.curAnimation=self.runningAnimation
        
        self.input=self.game.input
        
        self.xVel=0
        self.yVel=0
        self.maxSpeed=.008#can't run left or right faster than this
        self.walkSpeed=self.maxSpeed*.6
        self.jumpSpeed=-.012#your speed in the upward direction when when you jump
        
        self.game.graphicsRenderer.jack=self
        
    #def hitBottom(self, otherCollider):#called if your bottom hits something else's top (you've landed on the "ground"
        #print(self.onGround)
        #FallingEntity.hitBottom(self, otherCollider)
        #print(self.onGround)
        #print()
        
    def updateFromInputs(self):
        curMaxSpeed=self.walkSpeed
        if self.input.running: curMaxSpeed=self.maxSpeed
        
        self.xVel=self.input.joyAxisX*curMaxSpeed
        
        if self.input.right: self.xVel=curMaxSpeed
        elif self.input.left: self.xVel=-curMaxSpeed
        
        if self.input.jump and self.onGround:#TODO: why is self.onGround always false here?
            self.yVel=self.jumpSpeed
        
    def run(self):
        self.updateFromInputs()
        FallingEntity.run(self)
        ImageAnimationRenderer.run(self)
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
        
        self.game.graphicsRenderer.jack=self
        
    def updateFromInputs(self):
        self.xVel=self.input.joyAxisX*self.maxSpeed
        
        if self.input.right: self.xVel=self.maxSpeed
        elif self.input.left: self.xVel=-self.maxSpeed
        
    def run(self):
        FallingEntity.run(self)
        ImageAnimationRenderer.run(self)
        self.updateFromInputs()
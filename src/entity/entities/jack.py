from posDimEntity import PosDimEntity
from rectColliderDynamic import RectColliderDynamic
from imageAnimationRenderer import ImageAnimationRenderer
from imageAnimationLooping import ImageAnimationLooping
from fallingEntity import FallingEntity
import utils

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
        self.maxSpeed=.01#can't run left or right faster than this
        self.walkSpeed=.006
        self.jumpSpeed=-.017#your speed in the upward direction when when you jump
        self.xGroundAccel=.00006#how much you can accelerate in the x direction per millisecond when on the ground
        self.xAirAccel=.000025#how much you can accelerate in the x direction per millisecond when in the air
        self.xGroundFrictionDecel=.00004#how fast you slow down to a stop when on the ground and not running or walking.
        
        self.game.graphicsRenderer.jack=self
    
    def hitTop(self, otherCollider):
        FallingEntity.hitTop(self, otherCollider)
        
    def hitBottom(self, otherCollider):#called if your bottom hits something else's top (you've landed on the "ground"
        FallingEntity.hitBottom(self, otherCollider)#must manually call FallingEntity.hitBottom() to clear up ambiguity.  there are other classes that Jack inherits from who have a hitBottom() function.
        
    def updateFromInputs(self):
        curAccel=self.xGroundAccel
        
        if self.onGround:
            if self.input.jump:
                self.yVel=self.jumpSpeed
            if (self.input.right and self.input.left) or not (self.input.right and self.input.left):#no or both direction arrows are down.  don't accelerate. decelerate.
                decelerateRate=self.xGroundFrictionDecel*self.game.delta
                if utils.abs(self.xVel)<=decelerateRate:
                    self.xVel=0
                else:
                    if self.xVel>0:
                        self.xVel-=decelerateRate
                    else:
                        self.xVel+=decelerateRate
                
        else:#not on ground
            if not self.input.jump and self.yVel<0:#if you've let off of the jump button before you hit the peak of your jump
                self.yVel=0#stop rising
            curAccel=self.xAirAccel
            
        if self.input.right: self.xVel+=curAccel*self.game.delta
        if self.input.left: self.xVel-=curAccel*self.game.delta
        
        #self.xVel=self.input.joyAxisX*curMaxSpeed
            
        curMaxSpeed=self.walkSpeed
        if self.input.running: curMaxSpeed=self.maxSpeed
        
        if self.xVel>curMaxSpeed: self.xVel=curMaxSpeed#cap speed
        elif self.xVel<-curMaxSpeed: self.xVel=-curMaxSpeed
        
    def run(self):
        self.updateFromInputs()
        FallingEntity.run(self)
        ImageAnimationRenderer.run(self)
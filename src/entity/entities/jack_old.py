from posDimEntity import PosDimEntity
from dynamicEntity import DynamicEntity
from rectColliderDynamic import RectColliderDynamic
from imageAnimationRenderer import ImageAnimationRenderer
from imageAnimationLooping import ImageAnimationLooping
from imageAnimationNonLooping import ImageAnimationNonLooping
import utils
import constants

class Jack(PosDimEntity, ImageAnimationRenderer, RectColliderDynamic, DynamicEntity):#TODO: should inherit from FallingEntity
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, .6, 1.4)
        DynamicEntity.__init__(self, game, x, y)
        RectColliderDynamic.__init__(self, game.collisionSystem)
        ImageAnimationRenderer.__init__(self, game.graphicsRenderer, -.04, -.035)
        
        self.walkingAnimation=ImageAnimationLooping(game.graphicsRenderer, "jack/walking.animation", .5)
        self.runningAnimation=ImageAnimationLooping(game.graphicsRenderer, "jack/running.animation", .5)
        self.restingAnimation=ImageAnimationLooping(game.graphicsRenderer, "jack/resting.animation", .5)
        self.jumpingAnimation=ImageAnimationNonLooping(game.graphicsRenderer, "jack/jumping.animation", .5)
        self.landingAnimation=ImageAnimationNonLooping(game.graphicsRenderer, "jack/landing.animation", .5)
        self.choppingAnimation=ImageAnimationNonLooping(game.graphicsRenderer, "jack/chopping.animation", .5)
        self.curAnimation=self.walkingAnimation
        
        self.maxSpeed=.008#can't run left or right faster than this
        self.walkSpeed=self.maxSpeed*.6
        self.termVel=1#.01#max fall speed
        self.xAccel=self.maxSpeed/300#how much you accelerate left or right per millisecond
        self.frictionDeccel=self.maxSpeed/100.0#decceleration caused by friction.  how much to slow down by every millisecond
        self.gravAccel=constants.gravAccel#how fast you fall (acceleration due to gravity per millisecond)
        self.inAirMoveRatio=.5#xAccel*inAirMoveRatio is how fast you can accelerate via controls when in-air
        self.jumpSpeed=-.012#your speed in the upward direction when when you jump 
        self.onGround=False
        self.game.graphicsRenderer.jack=self
        #self.rightImage=self.image
        #self.leftImage=self.graphicsRenderer.loadImage("jack2.png")
        self.releasedJumpBtnSinceLastJump=True
        
    def hitBottom(self, otherCollider):#called if your bottom hits something else's top (you've landed on the "ground"
#         if not self.onGround:#are we landing?
#             self.curAnimation=self.landingAnimation
#             self.landingAnimation.reset()#TODO: need a function switchAnimation(newCurAnimaiton) so I'm not setting the current animation and resetting them manually every time.
        if self.yVel>0:#is falling
            self.yVel=0#stop falling
            self.onGround=True
        
    def hitTop(self, otherCollider):
        if self.yVel<0:
            self.yVel=0
            
    def hitLeft(self, otherCollider):
        if self.xVel<0:
            self.xVel=0
    
    def hitRight(self, otherCollider):
        if self.xVel>0:
            self.xVel=0
        
    def run(self):
        DynamicEntity.run(self)
        ImageAnimationRenderer.run(self)
        
        if not self.releasedJumpBtnSinceLastJump:
            if not self.game.input.jump:
                self.releasedJumpBtnSinceLastJump=True
        
        curXAccel=self.xAccel
        
        if self.onGround:
            if (not (self.game.input.left or self.game.input.right) and utils.abs(self.game.input.joyAxisX)<.25) or ((self.xVel<0 and (self.game.input.right or self.game.input.joyAxisX>0)) or (self.xVel>0 and (self.game.input.left or self.game.input.joyAxisX<0))):
                slowDownAmt=self.frictionDeccel*self.game.delta#slow down from friction
                if utils.abs(self.xVel)<utils.abs(slowDownAmt):
                    self.xVel=0#this is as slow as you can get
                else:
                    if self.xVel<0:
                        self.xVel+=slowDownAmt
                    else:
                        self.xVel-=slowDownAmt
            
            if self.game.input.jump and self.releasedJumpBtnSinceLastJump:#jump #TODO: do mario-style jump where you can control how high you jump based on how long you hold the button.  to do a full-height jump, you should have to hold the jump button until you reach the pinnacle of your jump.
                self.yVel=self.jumpSpeed
                self.releasedJumpBtnSinceLastJump=False
                self.curAnimation=self.jumpingAnimation
                self.jumpingAnimation.reset()
                
            #if self.xVel>0: self.image=self.rightImage
            #elif self.xVel<0: self.image=self.leftImage
        else:
            self.yVel+=self.gravAccel*self.game.delta
            curXAccel*=self.inAirMoveRatio#your ability to manuver is less when you're in the air
        
        if self.game.input.left: self.xVel-=curXAccel*self.game.delta#move
        if self.game.input.right: self.xVel+=curXAccel*self.game.delta
        
        self.xVel+=self.game.input.joyAxisX*curXAccel*self.game.delta
        
        if self.game.input.running:
            curMaxSpeed=self.maxSpeed
        else:
            curMaxSpeed=self.walkSpeed
        
        if self.xVel<-curMaxSpeed: self.xVel=-curMaxSpeed#limit horizontal speed
        if self.xVel>curMaxSpeed: self.xVel=curMaxSpeed
        if self.yVel>self.termVel: self.yVel=self.termVel
        
        if self.onGround and self.jumpingAnimation.isAnimationOver() and self.landingAnimation.isAnimationOver() and self.choppingAnimation.isAnimationOver():
            if utils.abs(self.xVel)>self.walkSpeed:
                self.curAnimation=self.runningAnimation
            elif utils.abs(self.xVel)>0:
                self.curAnimation=self.walkingAnimation
            else:
                self.curAnimation=self.restingAnimation
            
        self.onGround=False
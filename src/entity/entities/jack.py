from posDimEntity import PosDimEntity
from rectColliderDynamic import RectColliderDynamic
from imageRenderer import ImageRenderer
import utils

class Jack(PosDimEntity, ImageRenderer, RectColliderDynamic):#TODO: should inherit from DynamicEntity
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, .48, .75)
        RectColliderDynamic.__init__(self, game.collisionSystem)
        ImageRenderer.__init__(self, game.graphicsRenderer, "jack.png")
        
        self.maxSpeed=.008#can't run left or right faster than this
        self.walkSpeed=self.maxSpeed*.6
        self.termVel=.01#max fall speed
        self.xAccel=.0001#how fast you accelerate left or right per millisecond
        self.frictionDeccel=.999#decceleration caused by friction
        self.gravAccel=.00005#how fast you fall (acceleration due to gravity per millisecond) TODO: this should be in a util class as a universal constant
        self.jumpSpeed=-.012#your speed in the upward direction when when you jump 
        self.onGround=False
        self.xVel=0#current velocity
        self.yVel=0
        self.game.graphicsRenderer.jack=self
        self.rightImage=self.image
        self.leftImage=self.graphicsRenderer.loadImage("jack2.png")
        self.releasedJumpBtnSinceLastJump=True
        
#     def isCollidingWithRect(self, otherRect):
#         isColliding=RectColliderDynamic.isCollidingWithRect(self, otherRect)
#           
#         if isColliding:
#             self.image=self.image1
#             print(str(self.game.delta))
#         else:
#             self.image=self.image2
#           
#         return isColliding
        
    def getAccel(self, accel, milliseconds):
        accel*=milliseconds
            
        return accel
    
    def getDeccel(self, deccel, milliseconds):
        for millisecond in range(milliseconds-1):
            deccel*=deccel
            
        return deccel
        
    def hitBottom(self, otherCollider):#called if your bottom hits something else's top (you've landed on the "ground"
        if self.yVel>0:#is falling
            self.yVel=0#stop falling
            self.onGround=True
        
#     def hitTop(self, otherCollider):
#         if(self.yVel>0):#if falling
#             self.yVel=0#stop falling
#             self.y=otherCollider.top+self.height#prevent fall-through
#             self.onGround=True
        
    def run(self):
        if self.game.input.left: self.xVel-=self.getAccel(self.xAccel, self.game.delta)#move
        if self.game.input.right: self.xVel+=self.getAccel(self.xAccel, self.game.delta)
        #if self.game.input.left or self.game.input.joyAxisX<0: self.xVel-=self.getAccel(self.xAccel, self.game.delta)#move
        #if self.game.input.right or self.game.input.joyAxisX>0: self.xVel+=self.getAccel(self.xAccel, self.game.delta)
        self.xVel+=self.game.input.joyAxisX*self.getAccel(self.xAccel, self.game.delta)
        
        if not self.releasedJumpBtnSinceLastJump:
            if not self.game.input.up:
                self.releasedJumpBtnSinceLastJump=True
        
        if self.onGround:
            if not (self.game.input.left or self.game.input.right) and utils.abs(self.game.input.joyAxisX)<.25:
                self.xVel*=self.getDeccel(self.frictionDeccel, self.game.delta)#slow down from friction
            
            if self.game.input.up and self.releasedJumpBtnSinceLastJump:#jump
                self.yVel=self.jumpSpeed
                self.releasedJumpBtnSinceLastJump=False
        else:
            self.yVel+=self.getAccel(self.gravAccel, self.game.delta)
        
        if self.game.input.running: curMaxSpeed=self.maxSpeed
        else: curMaxSpeed=self.walkSpeed
        
        if self.xVel<-curMaxSpeed: self.xVel=-curMaxSpeed#limit horizontal speed
        if self.xVel>curMaxSpeed: self.xVel=curMaxSpeed
        if self.yVel>self.termVel: self.yVel=self.termVel
        
        self.y+=self.yVel*self.game.delta
        self.x+=self.xVel*self.game.delta
        
        if self.xVel>0: self.image=self.rightImage
        elif self.xVel<0: self.image=self.leftImage
        
        self.onGround=False
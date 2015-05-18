from posDimEntity import PosDimEntity
from rectColliderDynamic import RectColliderDynamic
from imageAnimationRenderer import ImageAnimationRenderer
from imageAnimationLooping import ImageAnimationLooping
from fallingEntity import FallingEntity

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
    
    def hitTop(self, otherCollider):
        FallingEntity.hitTop(self, otherCollider)
        
    def hitBottom(self, otherCollider):#called if your bottom hits something else's top (you've landed on the "ground"
        FallingEntity.hitBottom(self, otherCollider)#must manually call FallingEntity.hitBottom() to clear up ambiguity.  there are other classes that Jack inherits from who have a hitBottom() function.
        
    def updateFromInputs(self):
        curMaxSpeed=self.walkSpeed
        if self.input.running: curMaxSpeed=self.maxSpeed
        
        self.xVel=self.input.joyAxisX*curMaxSpeed
        
        if self.input.right: self.xVel=curMaxSpeed
        elif self.input.left: self.xVel=-curMaxSpeed
        
        if self.input.jump and self.onGround:
            self.yVel=self.jumpSpeed
        
        if not self.input.jump and not self.onGround and self.yVel<0:#if you've let off of the jump button before you hit the peak of your jump
            self.yVel=0#stop rising
        
    def run(self):
        self.updateFromInputs()
        FallingEntity.run(self)
        ImageAnimationRenderer.run(self)
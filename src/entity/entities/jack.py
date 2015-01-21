from entity import Entity

class Jack(Entity):
    def __init__(self, game, x, y):
        Entity.__init__(self, game)
        self.x=x
        self.y=y
        self.xVel=0
        self.yVel=0
        self.jumpSpeed=1.5
        self.accel=.001
        self.maxSpeed=.5
        self.slowDown=.9999
        self.fallAccel=.005
        self.onGround=False
        
    def run(self):
        accelerating=False
        
        if self.game.input.left: 
            self.xVel-=self.accel*self.game.delta
            accelerating=True
        if self.game.input.right: 
            self.xVel+=self.accel*self.game.delta
            accelerating=True
        if self.game.input.up: 
            if self.onGround:
                self.yVel=-self.jumpSpeed
                self.y-=5
                self.onGround=False
                accelerating=True
        if self.game.input.down: 
            pass#self.y+=self.speed*self.game.delta
        
        if not accelerating: self.xVel*=self.slowDown*self.game.delta
        
        self.x+=self.xVel*self.game.delta
        self.y+=self.yVel*self.game.delta
        
        if self.y<225:
            self.yVel+=self.fallAccel*self.game.delta
        else:
            self.yVel=0
            self.onGround=True
            self.y=225
            
        if self.xVel<-self.maxSpeed: self.xVel=-self.maxSpeed
        elif self.xVel>self.maxSpeed: self.xVel=self.maxSpeed
from dynamicEntity import DynamicEntity
import utils

class FallingEntity(DynamicEntity):
    def __init__(self, game, x, y):
        DynamicEntity.__init__(self, game, x, y)
        self.termVel=1#.01#max fall speed
        self.onGround=False
        
    def hitBottom(self, otherCollider):#called if your bottom hits something else's top (you've landed on the "ground"
        if self.yVel>0:#is falling
            self.yVel=0#stop falling
            self.onGround=True
            
    def run(self):
        DynamicEntity.run(self)
        
        if not self.onGround:
            self.yVel+=utils.gravAccel*self.game.delta
            
        if self.yVel>self.termVel: self.yVel=self.termVel
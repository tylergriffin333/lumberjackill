from dynamicEntity import DynamicEntity
import constants

class FallingEntity(DynamicEntity):
    def __init__(self, game, x, y):
        DynamicEntity.__init__(self, game, x, y)
        self.termVel=.01#max fall speed
        self.onGround=False
    
    def hitTop(self, otherCollider):#called if your top hits something else's bottom (you've hit your head on the "ceiling")
        if self.yVel<0:#is rising
            self.yVel=0#stop rising
        #TODO: need to figure out why this isn't working.  I thought this function would fix the bug where jack's head temporarily sticks to the ceiling while his yVel decelerates over time due to gravity.
        
    def hitBottom(self, otherCollider):#called if your bottom hits something else's top (you've landed on the "ground"
        if self.yVel>0:#is falling
            self.yVel=0#stop falling
            self.onGround=True
            
            
    def run(self):
        DynamicEntity.run(self)
        
        if not self.onGround:
            self.yVel+=constants.gravAccel*self.game.delta
            
        if self.yVel>self.termVel: self.yVel=self.termVel
        
        self.onGround=False
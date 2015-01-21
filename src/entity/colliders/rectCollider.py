from collider import Collider

class RectCollider(Collider):
    def __init__(self, collisionSystem):
        Collider.__init__(self, collisionSystem)
        
    def isCollidingWith(self, otherCollider):
        return otherCollider.isCollidingWithRect(self)
    
    def isCollidingWithRect(self, otherRect):
        return self.collisionSystem.isRectCollidingWithRect(self, otherRect)
    
    @property
    def left(self):
        return self.x-self.width/2
    
    @property
    def right(self):
        return self.x+self.width/2
    
    @property
    def bottom(self):
        return self.y+self.height/2
    
    @property
    def top(self):
        return self.y-self.height/2
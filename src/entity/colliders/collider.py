class Collider():
    def __init__(self, collisionSystem):
        self.collisionSystem=collisionSystem
        
    def hitRight(self, otherCollider): pass
    def hitLeft(self, otherCollider): pass
    def hitTop(self, otherCollider): pass
    def hitBottom(self, otherCollider): pass
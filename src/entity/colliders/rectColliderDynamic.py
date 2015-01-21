from rectCollider import RectCollider

class RectColliderDynamic(RectCollider):
    def __init__(self, collisionSystem):
        RectCollider.__init__(self, collisionSystem)
        
    def handleCollision(self, otherCollider):
        otherCollider.handleDynamicRectCollision(self)
        
    def handleDynamicRectCollision(self, otherDynamicRect):
        self.collisionSystem.handleDynamicRectVsDynamicRectCollision(self, otherDynamicRect)
        
    def handleStaticRectCollision(self, staticRect):
        self.collisionSystem.handleDynamicRectVsStaticRectCollision(self, staticRect)
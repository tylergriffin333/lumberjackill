from rectCollider import RectCollider

class RectColliderStatic(RectCollider):
    def __init__(self, collisionSystem):
        RectCollider.__init__(self, collisionSystem)
        
    def handleCollision(self, otherCollider):
        otherCollider.handleStaticRectCollision()
        
    def handleDynamicRectCollision(self, dynamicRect):
        self.collisionSystem.handleDynamicRectVsStaticRectCollision(dynamicRect, self)
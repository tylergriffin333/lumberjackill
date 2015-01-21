from rectCollider import RectCollider

class RectColliderStatic(RectCollider):
    def __init__(self, collisionSystem, pushLeft=True, pushDown=True, pushRight=True, pushUp=True):
        RectCollider.__init__(self, collisionSystem)
        self.pushLeft=pushLeft
        self.pushDown=pushDown
        self.pushRight=pushRight
        self.pushUp=pushUp
        
    def handleCollision(self, otherCollider):
        otherCollider.handleStaticRectCollision(self)
        
    def handleDynamicRectCollision(self, dynamicRect):
        self.collisionSystem.handleDynamicRectVsStaticRectCollision(dynamicRect, self)
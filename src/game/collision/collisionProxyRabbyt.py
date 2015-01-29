import rabbyt

class CollisionProxyRabbyt():
    def __init__(self):
        pass
    
    def runGroupVsSelfCollisionDetection(self, colliders):
        return rabbyt.collisions.aabb_collide(colliders)
    
    def runGroupVsGroupCollisionDetection(self, group1, group2):
        return rabbyt.collisions.aabb_collide_groups(group1, group2)
    
    def runSingleVsGroupCollisionDetection(self, singleCollider, group):
        return rabbyt.collisions.aabb_collide_single(singleCollider, group)
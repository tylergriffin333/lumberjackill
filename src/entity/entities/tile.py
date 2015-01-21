from entity import Entity
from rectColliderStatic import RectColliderStatic

class Tile(Entity):
    def __init__(self, game, x, y):
        Entity.__init__(self, game)
        RectColliderStatic.__init__(self, game.collisionSystem)
        self.x=x
        self.y=y
        self.width=1
        self.height=1
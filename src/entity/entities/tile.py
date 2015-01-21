from posDimEntity import PosDimEntity
from rectColliderStatic import RectColliderStatic

class Tile(PosDimEntity, RectColliderStatic):
    def __init__(self, game, x, y):
        PosDimEntity.__init__(self, game, x, y, 1.0, 1.0)
        RectColliderStatic.__init__(self, game.collisionSystem)
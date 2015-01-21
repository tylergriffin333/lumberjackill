from tile import Tile
from imageRenderer import ImageRenderer

class TileStone(Tile, ImageRenderer):
    def __init__(self, game, x, y):
        Tile.__init__(self, game, x, y)
        ImageRenderer.__init__(self, game.graphicsRenderer, "stone.png")#"stone_translucent.png")
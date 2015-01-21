from tile import Tile
from imageRenderer import ImageRenderer

class TileStone(Tile):
    def __init__(self, game, x, y):
        Tile.__init__(self, game, x, y)
        ImageRenderer.__init__(self, "stone.png")
#this type of entity has both position and dimension

from positionEntity import PositionEntity
from dimensionEntity import DimensionEntity

class PosDimEntity(PositionEntity, DimensionEntity):
    def __init__(self, game, x, y, width, height):
        PositionEntity.__init__(self, game, x, y)
        DimensionEntity.__init__(self, game, width, height)
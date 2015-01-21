#this kind of entity has width and height (dimension)

from entity import Entity

class DimensionEntity(Entity):
    def __init__(self, game, width, height):
        Entity.__init__(self, game)
        self.width=width
        self.height=height
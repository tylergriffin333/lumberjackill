#this type of entity has x, and y coordinates (position)

from entity import Entity

class PositionEntity(Entity):
    def __init__(self, game, x, y):
        Entity.__init__(self, game)
        self.x=x
        self.y=y
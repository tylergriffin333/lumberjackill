class GameModule():
    def __init__(self, game):
        self.game=game
        self.entities=[]
        self.tiles=[]
    
    def instantiateTilesArray(self, width, height):
        self.tiles=[]

        for x in range(width):
            column=[]
            for y in range(height):
                column.append(None)
            self.tiles.append(column)
            
    def addTile(self, tile, x, y):
        if hasattr(tile, self.reqAttr):
            self.tiles[x][y]=tile
        
    def addEntity(self, entity):
        if hasattr(entity, self.reqAttr):
            self.entities.append(entity)
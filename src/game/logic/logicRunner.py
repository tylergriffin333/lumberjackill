class LogicRunner():
    def __init__(self, game):
        self.game=game
        self.entities=[]#renderers
        self.tiles=[]
    
    def instantiateTilesArray(self, width, height):#TODO: this is replicated between gameMain, collisionSystem, and graphicsRenderer
        self.tiles=[]

        for x in range(width):
            column=[]
            for y in range(height):
                column.append(None)
            self.tiles.append(column)
            
    def addTile(self, tile, x, y):#TODO: this is replicated between gameMain, collisionSystem, and graphicsRenderer
        if hasattr(tile, "run"):
            self.tiles[x][y]=tile
        
    def addEntity(self, entity):#TODO: this is replicated between gameMain, collisionSystem, and graphicsRenderer
        if hasattr(entity, "run"):
            self.entities.append(entity)
            
    def run(self):
        for entity in self.game.entities:
            entity.run()
            
        for column in self.tiles:
            for tile in column:
                if tile != None:
                    tile.run()
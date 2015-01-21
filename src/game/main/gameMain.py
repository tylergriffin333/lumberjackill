from graphicsRenderer import GraphicsRenderer
from collisionSystem import CollisionSystem
from logicRunner import LogicRunner
from input import Input
import utils
import assetLoader

class GameMain():
    def __init__(self):
        self.graphicsRenderer=GraphicsRenderer(self)
        self.collisionSystem=CollisionSystem(self)
        self.logic=LogicRunner(self)
        
        self.input=Input(self)
        
        self.entities=[]
        self.tiles=None
        mapFileName="map1.map"#"map_single_tile.map"
        mapDimensions=assetLoader.getMapDimensionsFromMapFile(mapFileName)
        self.instantiateTilesArrays(mapDimensions[0], mapDimensions[1])
        assetLoader.loadMap(mapFileName, self)
        
        self.delta=0
        self.lastFrameStartTime=utils.getCurMilliseconds()
        
    def addTile(self, tile, x, y):
        self.tiles[x][y]=tile
        self.graphicsRenderer.addTile(tile, x, y)
        self.collisionSystem.addTile(tile, x, y)
        self.logic.addTile(tile, x, y)
        
    def addEntity(self, entity):
        self.entities.append(entity)
        self.graphicsRenderer.addEntity(entity)
        self.collisionSystem.addEntity(entity)
        self.logic.addEntity(entity)
        
    def instantiateTilesArrays(self, width, height):
        self.tiles=[]
        
        for x in range(width):
            column=[]
            for y in range(height):
                column.append(None)
            self.tiles.append(column)
            
        self.graphicsRenderer.instantiateTilesArray(width, height)
        self.collisionSystem.instantiateTilesArray(width, height)
        self.logic.instantiateTilesArray(width, height)
        
    def run(self):
        while True:#main game loop
            self.delta=utils.getCurMilliseconds()-self.lastFrameStartTime
            self.lastFrameStartTime=utils.getCurMilliseconds()
            
            self.input.run()
            self.collisionSystem.run()
            self.graphicsRenderer.run()
            self.logic.run()
#this class should be the only class that knows about graphicsProxy.  
#This class should do all the scaling.  
#this class should not care what drawing/windowing library graphicsProxy uses.

from graphicsProxy import GraphicsProxy
from jack import Jack

class GraphicsRenderer():
    def __init__(self, game):
        self.game=game
        self.graphicsProxy=GraphicsProxy()
        
        screenHeight=20.0#this is the screen-height in game-units
        pixelToGameUnitRatio=100.0#for each image, there should be a 100 to 1 pixel to game unit ratio
        self.scale=self.graphicsProxy.heightPix/screenHeight#game unit to screen pixel ratio
        screenWidth=self.graphicsProxy.widthPix/self.scale
        self.pixScale=self.scale/pixelToGameUnitRatio#this is what we should scale images by when loading them in
        #print(self.pixScale)
        self.screenX=0#the current screen position on the map
        self.screenY=0
        
        self.tiles=[]
        self.entities=[]#renderers
        #self.jackImage=self.graphicsProxy.loadImage("jack.png", 4)
        #self.jack=Jack(self.game, 0, 0)
        
    def gamePosToScreenPixPos(self, x, y):#accepts a game units position, scales it properly, and transforms it according to the current screen position
        x-=self.screenX
        y-=self.screenY
        x*=self.scale
        y*=self.scale
        return x, y
        
    def loadImage(self, filename):
        return self.graphicsProxy.loadImage(filename, self.pixScale)
        
    def drawImage(self, imageIndex, x, y):
        screenPixelPos=self.gamePosToScreenPixPos(x, y)
        self.graphicsProxy.drawImage(imageIndex, screenPixelPos[0], screenPixelPos[1])
        
    def drawRect(self, rect):
        self.graphicsProxy.drawRectangle(rect.left*100, rect.top*100, rect.width*100, rect.height*100, self.graphicsProxy.black, 1)
        
    def instantiateTilesArray(self, width, height):
        self.tiles=[]

        for x in range(width):
            column=[]
            for y in range(height):
                column.append(None)
            self.tiles.append(column)
            
    def addTile(self, tile, x, y):
        if hasattr(tile, "render"):
            self.tiles[x][y]=tile
        
    def addEntity(self, entity):
        if hasattr(entity, "render"):
            self.entities.append(entity)
        
    def run(self):
        self.render()
        
    def render(self):
        #self.jack.run()
        self.graphicsProxy.fillBackground(self.graphicsProxy.white)
        #self.graphicsProxy.drawRectangle(0, 280, 500, 1, self.graphicsProxy.black, 1)
        #self.graphicsProxy.drawImage(self.jack.x, self.jack.y, 1, self.jackImage)
        for entity in self.game.entities:
            if not entity.hidden:
                entity.render()#TODO: should I pass GraphicsRenderer to renderer.render(), rather than passing GraphicsRenderer to renderer in it's constructor?
            
        for column in self.tiles:
            for tile in column:
                if tile != None:
                    if not tile.hidden:
                        tile.render()
        
        #self.drawImage(self.jackImage, 3, 5)
        
        self.graphicsProxy.swapBuffer()
#this class should be the only class that knows about graphicsProxy.  
#This class should do all the scaling.  
#this class should not care what drawing/windowing library graphicsProxy uses.

#TODO: should only render items that are on/near screen.

from graphicsProxyRabbyt import GraphicsProxyRabbyt
#from graphicsProxyPygame import GraphicsProxyPygame
from gameModule import GameModule
import constants

class GraphicsRenderer(GameModule):
    def __init__(self, game):
        GameModule.__init__(self, game)
        self.reqAttr="render"#required attribute for entities to have to be added to entities or tiles lists
        self.graphicsProxy=GraphicsProxyRabbyt()
        #self.graphicsProxy=GraphicsProxyPygame()
        
        self.screenHeight=20.0#this is the screen-height in game-units
        self.scale=self.graphicsProxy.heightPix/self.screenHeight#game unit to screen pixel ratio
        self.screenWidth=self.graphicsProxy.widthPix/self.scale
        self.pixScale=self.scale/constants.pixelToGameUnitRatio#this is what we should scale images by when loading them in
        #print(self.pixScale)
        self.screenX=0#the current screen position on the map
        self.screenY=0
        self.screenScroolSpeed=.005
        #self.jackImage=self.graphicsProxy.loadImage("jack.png", 4)
        #self.jack=Jack(self.game, 0, 0)
        
    def gamePosToScreenPixPos(self, x, y):#accepts a game units position, scales it properly, and transforms it according to the current screen position
        x-=self.screenX
        y-=self.screenY
        x*=self.scale
        y*=self.scale
        return x, y
        
    def loadImageFlippedHorizontally(self, filename, scale):
        return self.graphicsProxy.loadImageFlipHorizontally(filename, self.pixScale*scale)
        
    def loadImage(self, filename, scale):
        return self.graphicsProxy.loadImage(filename, self.pixScale*scale)
        
    def loadImages(self, filenames, scale):
        images=[]
        
        for filename in filenames:
            images.append(self.loadImage(filename, scale))
            
        return images
            
    def loadImagesFlippedHorizontally(self, filenames, scale):
        images=[]
        
        for filename in filenames:
            images.append(self.loadImageFlippedHorizontally(filename, scale))
            
        return images
        
    def drawImage(self, imageIndex, x, y, width, height):
        screenPixelPos=self.gamePosToScreenPixPos(x, y)
        self.graphicsProxy.drawImage(imageIndex, screenPixelPos[0], screenPixelPos[1], width*self.scale, height*self.scale)
        
    def drawImageFlippedHorizontally(self, imageIndex, x, y, width, height):
        screenPixelPos=self.gamePosToScreenPixPos(x, y)
        self.graphicsProxy.drawImageFlippedHorizontally(imageIndex, screenPixelPos[0], screenPixelPos[1], width*self.scale, height*self.scale)
        
    def drawRect(self, rect):
        self.graphicsProxy.drawRectangle(rect.left*100, rect.top*100, rect.width*100, rect.height*100, self.graphicsProxy.black, 1)
        
    def run(self):
        targetScreenXPos=self.jack.x-self.screenWidth/2
        targetScreenYPos=self.jack.y-self.screenHeight/2
        
        self.screenX=targetScreenXPos
        self.screenY=targetScreenYPos
        
#         if utils.abs(self.screenX-targetScreenXPos)>1:
#             if self.screenX<targetScreenXPos: self.screenX+=self.screenScroolSpeed*self.game.delta
#             elif self.screenX>targetScreenXPos: self.screenX-=self.screenScroolSpeed*self.game.delta
#         if utils.abs(self.screenY-targetScreenYPos)>1:
#             if self.screenY<targetScreenYPos: self.screenY+=self.screenScroolSpeed*self.game.delta
#             elif self.screenY>targetScreenYPos: self.screenY-=self.screenScroolSpeed*self.game.delta
        
        self.render()
        
    def render(self):
        #self.jack.run()
        self.graphicsProxy.fillBackground(self.graphicsProxy.white)
        #self.graphicsProxy.drawRectangle(0, 280, 500, 1, self.graphicsProxy.black, 1)
        #self.graphicsProxy.drawImage(self.jack.x, self.jack.y, 1, self.jackImage)
        for entity in self.entities:
            if not entity.hidden:
                entity.render()#TODO: should I pass GraphicsRenderer to renderer.render(), rather than passing GraphicsRenderer to renderer in it's constructor?
            
        for column in self.tiles:
            for tile in column:
                if tile != None:
                    if not tile.hidden:
                        tile.render()
        
        #self.drawImage(self.jackImage, 3, 5)
        
        self.graphicsProxy.swapBuffer()
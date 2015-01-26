#this class will be the proxy between whatever graphics rendering system I'm using (rabbyt in this case) and the gameRenderer
#this class should know nothing about scaling.  it only knows about 1-to-1 unit-pixel drawing.
import rabbyt
import pygame
import os
import assetLoader

class GraphicsProxyRabbyt():
    def __init__(self):
        rabbyt.data_directory = os.path.dirname(__file__)#rabbyt
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (2080, 1450)#position window
        pygame.init()
        screenSize = self.widthPix, self.heightPix = 300, 200#1920, 1080#1680, 1050#TODO: need to get native screen res and set to that.
        pygame.display.set_mode(screenSize, pygame.OPENGL | pygame.DOUBLEBUF)# | pygame.FULLSCREEN)#rabbyt
        rabbyt.set_viewport(screenSize)#rabbyt
        rabbyt.set_default_attribs()#rabbyt
        
        self.white=[1, 1, 1]
        
        self.images=[]
        
    def drawText(self, color, x, y, text):
        pass
        
    def drawEllipse(self, x, y, width, height, color):#works just like drawRectangle
        pass
        
    def drawRectangle(self, x, y, width, height, color, scale):
        pass
        
    def fillBackground(self, color):
        rabbyt.clear(color)
        
    def swapBuffer(self):
        pygame.display.flip()
        
    def loadImageFlipHorizontally(self, filename, scale):#TODO: prevent loading duplicate images
        imageIndex=self.loadImage(filename, scale)
        self.images[imageIndex].scale_x*=-1
        return imageIndex
    
    def loadImage(self, filename, scale):#TODO: prevent loading duplicate images
        image=assetLoader.loadRabbytImage(filename)
        image.scale=scale
        self.images.append(image)
        return len(self.images)-1#return imageIndex
    
    def drawImage(self, imageIndex, x, y, width, height):
        image=self.images[imageIndex]
        image.x=x+width/2-self.widthPix/2
        image.y=-y-height/2+self.heightPix/2
        image.render()
        
    def drawImageFlippedHorizontally(self, imageIndex, x, y, width, height):
        image=self.images[imageIndex]
        image.x=x+width/2-self.widthPix/2
        image.y=-y-height/2+self.heightPix/2
        image.scale_x*=-1#flip
        image.render()
        image.scale_x*=-1#flip back
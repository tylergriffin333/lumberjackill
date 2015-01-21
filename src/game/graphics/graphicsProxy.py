#this class will be the proxy between whatever graphics rendering system I'm using (pygame in this case) and the gameRenderer
#this class should know nothing about scaling.  it only knows about 1-to-1 unit-pixel drawing.

import pygame
import utils
import assetLoader

class GraphicsProxy():
    def __init__(self):
        pygame.init()
        
        shrink=False
        
        if shrink:
            import os
            os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1680, 1480)#(960, 540)
            self.heightPix=200#in pixels
            self.widthPix=300
            self.screen=pygame.display.set_mode([self.widthPix, self.heightPix])
            self.lineThickness=1
        else:
            self.screen=pygame.display.set_mode([0,0], pygame.FULLSCREEN, 32)
            self.heightPix=int(pygame.display.Info().current_h)#in pixels
            self.widthPix=int(pygame.display.Info().current_w)
            self.lineThickness=2
        
        self.font=pygame.font.SysFont(None, int(35))
        self.screenDiag=utils.dist(0, 0, self.widthPix, self.heightPix)
        
        self.white=[255,255,255,255]
        self.black=[0,0,0,255]
        self.red=[255,0,0,255]
        self.green=[0,255,0,255]
        self.darkGreen=[0,128,0,255]
        self.blue=[0,0,255,255]
        self.darkRed=[102,0,0,255]
        self.transRed=[255,0,0,77]
        self.cyan=[0,255,255,255]
        self.darkCyan=[0,77,77,255]
        
        self.images=[]
        
    def drawText(self, color, x, y, text):
        text=self.font.render(text, True, color)
        textRect = text.get_rect()
        pos=utils.transformPoint(x, y, 0, self.scale, 1, [0,0])
        textRect.x=pos[0]
        textRect.y=pos[1]
        self.screen.blit(text, textRect)
        
    def drawEllipse(self, x, y, width, height, color):#works just like drawRectangle
        pos=utils.transformPoint(x, y, 0, self.scale, 1, [0,0])
        pygame.draw.ellipse(self.screen, color, [pos[0], pos[1], width*self.scale, height*self.scale], self.lineThickness)
        
    def drawRectangle(self, x, y, width, height, color, scale):
        pos=utils.transformPoint(x, y, 0, scale, 1, [0,0])
        pygame.draw.rect(self.screen, color, [pos[0], pos[1], width*scale, height*scale], self.lineThickness)
        
    def fillBackground(self, color):
        self.screen.fill(color)
        
    def swapBuffer(self):
        pygame.display.update()
        
    def loadImage(self, filename, scale):#TODO: prevent loading duplicate images
        image=assetLoader.loadImage(filename)
        rect=image.get_rect()
        image=pygame.transform.scale(image, [int(scale*rect.width), int(scale*rect.height)])
        self.images.append(image)
        return len(self.images)-1#return imageIndex
    
    def drawImage(self, imageIndex, x, y):
        rect=self.images[imageIndex].get_rect()
        rect.x=x
        rect.y=y
        self.screen.blit(self.images[imageIndex], rect)
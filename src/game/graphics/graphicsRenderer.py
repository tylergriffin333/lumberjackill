#this class should be the only class that knows about graphicsProxy.  
#This class should do all the scaling.  
#this class should not care what drawing/windowing library graphicsProxy uses.

from graphicsProxy import GraphicsProxy
from jack import Jack

class GraphicsRenderer():
    def __init__(self, game):
        self.game=game
        self.graphicsProxy=GraphicsProxy()
        self.jackImage=self.graphicsProxy.loadImage("jack.png", 4)
        self.jack=Jack(self.game, 0, 0)
        
    def run(self):
        self.jack.run()
        self.graphicsProxy.fillBackground(self.graphicsProxy.white)
        self.graphicsProxy.drawRectangle(0, 280, 500, 1, self.graphicsProxy.black, 1)
        self.graphicsProxy.drawImage(self.jack.x, self.jack.y, 1, self.jackImage)
        self.graphicsProxy.swapBuffer()
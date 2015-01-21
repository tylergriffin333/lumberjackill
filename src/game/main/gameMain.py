from graphicsRenderer import GraphicsRenderer
from input import Input
import utils

class GameMain():
    def __init__(self):
        self.graphicsRenderer=GraphicsRenderer(self)
        self.input=Input(self)
        self.delta=0
        self.lastFrameStartTime=utils.getCurMilliseconds()
        
        while True:
            self.delta=utils.getCurMilliseconds()-self.lastFrameStartTime
            self.lastFrameStartTime=utils.getCurMilliseconds()
            self.input.run()
            self.graphicsRenderer.run()